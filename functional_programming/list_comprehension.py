lst1=[1,2,3]
lst2=[3,4,5,6,7]
#lst=[]
#for i in lst1:
#    for j in lst2:
#        lst.append ((i,j))
#print(lst)


op=[(i,j)for  i in lst1 for j in lst2]
print(op) #sqauare bracket is also included

op=[i**2 for  i in lst1]
print(op) # sqaure of lst1

op=[i**3 for i in lst2]
print(op) #cube of lst2

op=[i for i in lst1 if i%2==0]
print(op)

op=[i%2==0 for i in lst2]
print(op)

op=[i for i in lst1 for j in lst2 if i==j]
print(op) #common
