from app import db, Student, Course

# student0 = Student(name="Steve", gender="Female")
# student1 = Student(name="Wilson", gender="Female")
# student2 = Student(name="Bill", gender="Male")
# student3 = Student(name="Luke", gender="Male")
# student4 = Student(name="Michael", gender="Male")
# student5 = Student(name="Louis", gender="Female")
# student6 = Student(name="Ben", gender="Male")
# student7 = Student(name="Tim", gender="Female")
# student8 = Student(name="Ken", gender="Male")
# student9 = Student(name="Kevin", gender="Male")
#
# course0 = Course(name="Math")
# course1 = Course(name="English")
# course2 = Course(name="Physic")
# course3 = Course(name="Chemistry")
# course4 = Course(name="Computer Science")
# course5 = Course(name="Gym")
#
# db.session.add_all(
#     [student0, student1, student2, student3, student4, student5, student6, student7, student8, student9, course0,
#      course1, course2, course3, course4, course5])
# db.session.commit()
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
