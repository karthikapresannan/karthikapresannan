f=open("demo","reg")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)

st=set(lst)
print(st)


#name="luminar\n"
#name.rstrip("\n")
#print(name)
#

