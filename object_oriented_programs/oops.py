class person:
    def set_person(self,age,name):
        self.name=name
        self.age =age

    def set_person(self, age, name):
        self.name = name
        self.age = age

obj=person()
obj.set_person(25,"ram")
obj.print_person()

obj1=person()
obj1.set_person(26,"varun")
obj1.print_person()