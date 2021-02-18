lst=[1,2,3,4,5,6]
no=int(input("enter the number"))
st=set(lst)
out=set()
for num in st:#1
    op=no-num#6-4
    if op in st: #(op in st)&(op!=num) another condition
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))
print(out)
