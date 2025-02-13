class person:
    name = "siva"
    age = 10 
class student(person):
    studentid = 101 
class teacher(person):
    subject = "python"

t = teacher()
print("-------TEACHER DETAILS---------")
print("Teacher Subject : " , t.subject) 
print("Teacher's Student Name : ", t.name)
print("Teacher's Student Age :",t.age)

s = student()
print("-------STUDENT DETAILS---------")
print("Student id   : " , s.studentid) 
print("Student Name : " ,s.name)
print("Student Age :",s.age)
