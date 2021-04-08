employees=[
    {"name":"akshay","desig":"devop","salary":48000,"join":2000,"resign":2000},
    {"name":"aswin","desig":"devop","salary":30000,"join":1989,"resign":1995},
    {"name":"vivek","desig":"QA","salary":28000,"join":2004,"resign":2010},
    {"name":"anju","desig":"QA","salary":32000,"join":2005,"resign":2015},
    {"name":"veena","desig":"mrkt","salary":35000,"join":2010,"resign":2020},
]


#highest salary

max_salary=max(map(lambda emp:emp["salary"],employees))
print(max_salary) #maximum salary

high_salary_emp=max(filter(lambda emp:emp["salary"]==max_salary,employees))
print(high_salary_emp) # highest salary employee

experience=list(filter(lambda emp:emp["resign"]-emp["join"]>8,employees))
print(experience) #above experience 8 years




