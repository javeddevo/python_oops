#class=plan
#object=product
#attribute=variable and behaviour(method or function)
class Computer(object):
    def config(self):
        print("hello")
com1=Computer()
com2=Computer()
Computer.config(com1) #(config method belong to computer class and have to pass the object com1)
Computer.config(com2)
print("====================================================")
com2.config() #(where object is calling function and config method will take argument com2 and pass tthat in self)
com1.config()


#practice-1
"""class Replay(object):
    def review(self):
        print("Thank yoou very much for info")
student1=Replay()
student1.review()
"""

#practice-2
"""class Hello(object):
    def  info(self,name):
        print("hello",name)
ob1=Hello()
ob1.info("javeed")
    
"""
