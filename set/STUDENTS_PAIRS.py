students={"ajin","abin","aswathy","revathy","megha"}
fail={"ajin","aswathy","megha"}

passout=students.difference(fail)
print(passout)

lst=[10,20,"hello",30,50]
lst[1]=60
st=set(lst)
res=list(st)
print(res[2])

lst=[1,2,3,4]      #FINDING THE PAIR
no=int(input("enter number"))
st=set(lst)

for num in st: #1,5
    op=no-num #6-2=4
    if op in st:
            print(num,op)
            break