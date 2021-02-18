employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001: {"eid": 1001, "ename": "raj", "desig": "testing", "salary": 40000},
    1002: {"eid": 1002, "ename": "amit", "desig": "ba", "salary": 50000},
}
#eid=int(input("enter eid"))
#property=input("enter property values")
#if eid in employees:
 #   print(employees[eid]["salary"])
  #  if property in employees[eid]:
        #print(employees[eid][property])
   # else:
    #    print("invalid property")
#else:
 #   print("invalid employee")


def print_employee_details(**kwargs):  #kwrags={eid:1000}
    id=kwargs["eid"] #1000

    if id in employees:
        print(employees[id]["ename"])
        prop=kwargs["property"] #salary
        print(employees[id][prop])
    else:
        print("id not exist")

print_employee_details(eid=1000,property="salary")

print_employee_details(eid=1000,property="desig")
