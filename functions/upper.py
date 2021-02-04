
num=int(input("enter the number"))
low=int(input("enter the low"))
upp=int(input("enter the upper"))
for i in range (1,(upp+1)):
    if i**num in range(low,(upp+1)):
        print(i**num)