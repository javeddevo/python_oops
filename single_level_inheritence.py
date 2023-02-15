"""acquring all the properties from the parent """

class one():
    def info(self):
        print("this is maim calss")
class two(one):
    def info_2(self):
        print("this is class2")
obj=two()
obj.info()
obj.info_2()