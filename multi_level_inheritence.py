"""Acquiring all the properties from level wise"""
class grand_father():
    def g_fa(self):
         print("this is grand  father")

class parent(grand_father):
    def fa(self):
        print("thsi is father")
class child(parent):
    def ch(self):
        print("this  is child")
obj=child()
obj.ch()
obj.fa()
obj.g_fa()