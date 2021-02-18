def add (num1,num2):
    return num1+num2
res=add(10,20)
print(res)

def add(*args):
    print(args)
add(10,20,30,40)

def add(*args): # single star tuple
    total=0
    for num in args:
        total+=num
    print(total)
add(10,20,30)


def print_emp_data(**args):  #double star means dictionary
   for k,v in args.items():
    print(k,v)
print_emp_data(eid=100,job="kakkand",resign="thirssur")

