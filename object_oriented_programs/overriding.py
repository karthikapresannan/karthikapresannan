class parent:
    def phone(self):
        print("have nokia phone")
class child(parent):
    def phone(self):
        print("iphone")
ch=child()
ch.phone()
#######################################################################


class parent:
    def bike(self):
        print("passion pro")
    def car(self):
        print("seltos")

class child(parent):  #inhert parent
    def bike(self):
        print("re350")

ch=child()
ch.bike()
ch.car()

###################################################################

class person(object):
    def __init__(self,age,name): #__init__ constructor
        self.age=age
        self.name=name

    def __str__(self):
            return self.name+str(self.age)

p=person(25,"Aravind")
p1=person(26,"Aswanth")
print(p)
print(p1)


#two class