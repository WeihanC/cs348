from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event
from sqlalchemy.engine import Engine
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"

db = SQLAlchemy(app)  # 实例化的数据库


# Set up SQLAlchemy engine and session with READ UNCOMMITTED
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], isolation_level="READ COMMITTED")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Student
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    gender = db.Column(db.Enum("Male", "Female"), nullable=False)
    courses = db.relationship("Course", secondary="student_to_course", backref="students")


# main table: Course management
class StudenToCourse(db.Model):
    __tablename__ = "student_to_course"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), index=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), index=True)


# Course
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


@app.route('/')
def index():  # put application's code here
    title = "CS348 Project"

    return render_template("index.html", title=title, students=Student.query.all())


@app.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update(student_id):
    student_to_update = Student.query.get(student_id)
    schedule = StudenToCourse.query.filter_by(student_id=student_id)
    return render_template('update.html', student=student_to_update, schedule=schedule)


@app.route('/adds', methods=['GET', 'POST'])
def adds():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    print("hi")
    stu = Student.query.get(student_id)
    course = Course.query.get(course_id)
    stu.courses.append(course)
    db.session.commit()

    return render_template("update.html", student=stu, schedule=StudenToCourse.query.filter_by(student_id=student_id))


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    schedule = StudenToCourse.query.get(id)
    student = Student.query.get(schedule.student_id)
    course = Course.query.get(schedule.course_id)
    student.courses.remove(course)
    db.session.commit()

    return redirect('/')
    # return render_template("update.html", student=student,
    #                        schedule=StudenToCourse.query.filter_by(student_id=student.id))



@app.route('/change/<int:id>', methods=['GET', 'POST'])
def change(id):

    schedule = StudenToCourse.query.get(id)

    schedule.course_id = request.form['course_id']
    db.session.commit()

    return redirect('/')

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        selected_ids = request.form.getlist('student_ids')
        selected_ids = [int(id) for id in selected_ids]  # Convert IDs to integers

        if selected_ids:
            # Prepare placeholders and parameters for SQL query
            placeholders = ",".join([":id" + str(i) for i in range(len(selected_ids))])  # Named placeholders
            parameters = {f"id{i}": selected_ids[i] for i in range(len(selected_ids))}  # Map placeholders to values
            parameters['count_ids'] = len(selected_ids)  # Additional parameter for the HAVING clause

            sql = text(f"""
            SELECT course.id, course.name, COUNT(DISTINCT student.id) as student_count
            FROM course
            JOIN student_to_course ON course.id = student_to_course.course_id
            JOIN student ON student.id = student_to_course.student_id
            WHERE student.id IN ({placeholders})
            GROUP BY course.id
            HAVING COUNT(DISTINCT student.id) = :count_ids;
            """)

            # Execute the query with named parameters
            result = db.session.execute(sql, parameters)
            common_courses = result.fetchall()

            # Process and display the fetched courses
            courses = [{'id': course['id'], 'name': course['name']} for course in common_courses]
            return render_template("results.html", common_courses=courses)
        else:
            return redirect('/filter')
    else:
        all_students = Student.query.all()
        return render_template("filter.html", students=all_students)




if __name__ == '__main__':
    # db.create_all()
    # db.drop_all()
    app.run()
