class employee:
    company_name="ctc"

    def __init__(self,age,name):
        self.age=age
        self.name=name

    def __str__(self):
        return str(self.age)+" "+self.name

emp=employee(24,"aravind")
print(emp)

