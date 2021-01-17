"""class Hello(object):
    def __init__(self):
        print("helloworld")
    def config(self):
        print("16gb,1tb")
        
object=Hello()
object.config()
"""
#prcatice-1
"""class Hello(object):
    def __init__(self,name,no):
        print(name,no)
    def hi(self):
        print("helloworld")
obj=Hello("javeed",33)
obj.hi()
"""
#practice-2
class Hello(object):
    def __init__(self,name,no):
        self.names=name
        self.number=no

    def hi(self):
        print(self.names)
        print(self.number)
obj=Hello("javeed",9986)
obj.hi()
