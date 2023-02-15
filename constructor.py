#with constructor
class hello:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
obj=hello("javed",343)
obj.info()

# without constructor
class hello:
    def hello(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
obj=hello()
obj.hello("javeed",333)
obj.info()