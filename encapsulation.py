""" restriction of accesss of variable and method """

class A:
    _a=20
    __b=30
    def hello(self):
        print(self.__b)
obj=A()
obj.hello()
print(obj._a)
