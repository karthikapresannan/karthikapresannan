#keys id name desgination salary
#print employee name
#employee salary
#check for genter key s there if not add  gender ey values pairs
#iterate all keys values pairs

employee={"id":1000,"name":"karthika","desgintion":"software enginner", "salary":25000}
print(employee["name"])

print(employee["salary"])

if "gender" in employee:
    print("entry exist")
else:
    print("not exist")

employee["gender"]="female"
print(employee)

for k,v in employee.items():
    print(k,",",v)

