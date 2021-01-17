class Car(object):
    wheels=5  #(class variable default for all objects)
    def __init__(self):
         self.name="bmw" #(this is called a instance variable)
         self.mil=33     #(same above)
c1=Car()
c2=Car()
c1.mil=22
print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c1.wheels)
#if u want to modify the class variable
Car.wheels=7
print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c1.wheels)

    
