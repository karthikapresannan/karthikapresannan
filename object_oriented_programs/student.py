class student:

    def set_student(self,id,name,total):
        self.id=id
        self.name =name
        self.total=total

    def print_student(self):
        print(self.id)
        print(self.name)
        print(self.total)

obj=student()
obj.set_student(1, "arun",40)
obj.print_student()

obj1=student()
obj1.set_student(2, "varun",50)
obj1.print_student()
