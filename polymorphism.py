class Student_info(object):
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age

    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.age)
class Teacher_info(object):
    def __init__(self,name,rollno,subject):
        self.name=name
        self.rollno=rollno
        self.subject=subject
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.subject)
      

m1=Student_info("javeed",33,33)
m1.display()
print("============================================")
t2=Teacher_info("deepika",44,"maths")
t2.display()
