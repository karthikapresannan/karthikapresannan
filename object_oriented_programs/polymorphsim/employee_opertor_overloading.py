class employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def print_details(self):
        print(self.eid,self.name,self.desig,self.sal,self.exp)
    def __str__(self):
        return self.name

f=open("employee","reg")
employees=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    eid=data[0]
    name=data[1]
    desig=data[2]
    sal=data[3]
    exp=data[4]
    obj=employee(eid,name,desig,sal,exp)
    employees.append(obj)
for emp in employees:
    print(emp)

highest_salary=[]
for emp in employees:
    highest_salary.append(emp.sal)
print("MAX SALARY=",max(highest_salary))
print(emp)


emp_name=list(map(lambda emp:emp.name,employees))
print(emp_name)

qacount=len(list(filter(lambda emp:emp.desig=="qa",employees)))
print(qacount)

devops=list(filter(lambda emp:emp.desig=="developer",employees))
enames=list(map(lambda emp:emp.name,devops))
print(enames)

#explist=list(filter(lambda emp:emp.exp>2,employees))
#ls=[]

high_salary=max(list(map(lambda emp:emp.sal,employees)))
print("max function",high_salary)

from functools import reduce
salary=list(map(lambda emp:emp.sal,employees))
high_salary=reduce(lambda sal1,sal2:sal if sal1>sal2 else sal2,salary)
print("using reduce",high_salary)

