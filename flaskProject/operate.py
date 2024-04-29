from app import db, Student, Course

student0 = Student(name="Steve", gender="Female")
student1 = Student(name="Wilson", gender="Female")
student2 = Student(name="Bill", gender="Male")
student3 = Student(name="Luke", gender="Male")
student4 = Student(name="Michael", gender="Male")
student5 = Student(name="Louis", gender="Female")
student6 = Student(name="Ben", gender="Male")
student7 = Student(name="Tim", gender="Female")
student8 = Student(name="Ken", gender="Male")
student9 = Student(name="Kevin", gender="Male")
student10 = Student(name="Lorraine", gender="Female")

course0 = Course(name="Math", teacher="Dr.Chen", course_credit=3 )
course1 = Course(name="English", teacher="Dr.Green", course_credit=3 )
course2 = Course(name="Physic", teacher="Dr.Williams", course_credit=4 )
course3 = Course(name="Chemistry", teacher="Dr.Li", course_credit=4 )
course4 = Course(name="Computer Science", teacher="Dr.Lee", course_credit=3 )
course5 = Course(name="Gym", teacher="Dr.Wang", course_credit=1 )

db.session.add_all(
    [student0, student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, course0,
     course1, course2, course3, course4, course5])
db.session.commit()
#
# cs = Course.query.filter(Course.id >= 3).all()
# stu = Student.query.filter(Student.id >= 1).all()
# for s in stu:
#     s.courses = cs
#     db.session.add(s)
#
# db.session.commit()


# 学生查询课程
# stu = Student.query.get(1)
# for s in stu.courses:
#     print(s.name)
# print(stu.courses)

# print("===================")
#
# 课程查询学生
# c = Course.query.get(2)
# for s in c.students:
#     print(s.name)
