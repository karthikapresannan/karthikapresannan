class Employee:
    company_name="ctc"

    def __init__(self,age,name):
        self.age=age
        self.name=name

    def print_person(self):
        print(self.age)
        print(self.name)
        print(Employee.company_name)

emp=Employee(25,"arun")
print(emp.name)
print(Employee.company_name) #static