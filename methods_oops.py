class Hello(object):
    school="fuck"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):#(instance method works with static or instance varibles)
        return (self.m1+self.m2+self.m3/3)
    @classmethod
    def info(cls):#(class method works with class varables
        return cls.school
    def hi():#(static methid)
        print("hello")
c1=Hello(12,2,3)
c2=Hello(66,76,7)#(instance)
print(c1.avg())
print(c2.avg())
print(c1.info())#(class)
Hello.hi() #(static)
