"""acquiring all the properties from base parent class to derived classes"""
class parent():
    def pa(self):
        print("this is parent class")
class child1(parent):
    def ch1(slef):
        print("this is child1 ")
class child2(parent):
    def ch2(self):
        print("thsi is child 2")
obj1=ch1()
obj2=ch2()
obj1.pa()
obj2.pa()
obj1.ch1()
obj2.ch2()
