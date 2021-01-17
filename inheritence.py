class Parent(object):
    def __init__(self,name,rollno):
        self.anme=name
        self.rollno=rollno
    def display(self):
        print(self.anme)
        print(self.rollno)
class Student(object):
    def __init__(self,name,rollno,subject):
        Parent.__init__(self,name,rollno)
        #self.name=name
        #self.rollno=rollno
        self.subject=subject
    def display(self):
        Parent.display(self)
        #print(self.name)
        #print(self.rollno)
        print(self.subject)
class Teacher(object):
    def __init__(self,name,rollno,school):
        Parent.__init__(self,name,rollno)
        #self.name=name
        #self.rollno=rollno
        self.school=school
    def display(self):
     Parent.display(self)
     #print(self.name)
     #print(self.rollno)
     print(self.school)
        
s1=Student("javeed",33,"maths")
s1.display()
print("========================")
t1=Teacher("ram",334,"lbrce")
t1.display()
