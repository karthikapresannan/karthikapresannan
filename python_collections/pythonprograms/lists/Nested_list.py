employees=[
[101,"anu","developer",2500,1989,1999],
[101,"meera","testing",24000,1990,2005],
[103,"achu","ba",21000,1975,1988],
[104,"ammu","ba",20000,1990,1999]
]
for employee in employees:
     print(employee[1])

for employee in employees:
    print(employee[2]=="developer")
    print(employee)

total=0
for salary in employees:
    total+=employee[3]
print("total Salary=",total)

salary_list=[]
for high_salary in employees:
    salary_list.append(employee[3])
print("high_salary=",max(salary_list))

highest_experience=[]
for employee in employees:
    highest_experience.append(employee[5]-employee[4])
print("employee=",max(highest_experience))#highest experience
print(highest_experience) #sorting the experience