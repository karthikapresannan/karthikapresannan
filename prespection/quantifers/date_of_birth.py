from re import*
rule="\d{1,31}\d{1,12}\d{4}"
dateofbirth=input("enter the date of birth")
matcher=fullmatch(rule,dateofbirth)
if matcher!=None:
    print("registration date of birth ")
else:
     print("invalid")