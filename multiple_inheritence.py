class father():
    def fa(self):
        print("this si father")
class mother():
    def mo(self):
        print("this is mother")
class child(father,mother):
    def ch(self):
        print("this is child class ")
obj=child()
obj.mo()
obj.fa()
obj.ch()