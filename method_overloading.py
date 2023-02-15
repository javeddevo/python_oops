
# having the same method but diffrent parameters called method overloading

"""class hello():
    def hi(self):
        print("welcomes")
    def hi(self,firstname=""):
        print("welcome",firstname)
    def hi(self,lastname="",firstname=""):
        print("welcome",lastname,firstname)
obj=hello()
obj.hi()
# obj.hi()
obj.hi("javeed")
obj.hi("ma","javeed")
"""    
# the above code can be written as using method overlaoding 
class hello():
    def hi(self,firstname="",lastname=""):
        print("welcome",firstname,lastname)
        
obj=hello()
obj.hi()
obj.hi("javeed")
obj.hi("ma","javeed")