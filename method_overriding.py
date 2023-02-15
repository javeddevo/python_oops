# writing a same method name with same signature in both parent and child class 

class parent:
    def B(self):
        print("this is parent class")
class child(parent):
    def B(self):
        super().B() #if you want to acive parent method then you have to peform super method
        print("this is child class")
        #pass
obj=child()
obj.B()
