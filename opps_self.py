#use_self
class Hello(object):
    def __init__(self):
        self.name="javeed"
        self.no=90
    def update(self):#(by the help of self u will know to which object ur are calling and changing)
      self.no=44
    def compare(self,other):
        if self.no == self.no:
            return True
        else:
            return False
c1=Hello()
c2=Hello()
c1.name="ravi"
print(c1.name)
print(c2.name)
if c1.compare(c2):
    print("matched")
else:
    print("dismatched")
print(c1.no)
print(c2.no)
c1.update()#(self is a pointer to the object)
print(c1.no)
print(c2.no)

