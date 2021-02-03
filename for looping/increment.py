#2+22=24
#3+33+333=369
#4+44+444+4444=



num=int(input("enter the number"))
pattern=""
total=0
for i in range(1,(num+1)):
    pattern=str(num)*i
    total+=int(pattern)
print(total)

