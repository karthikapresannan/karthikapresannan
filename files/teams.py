f1=open("teams","r")
f2=open("drops","r")
st1=set(f1)
st2=set(f2)
lst=[]
for teams in f1:
    lst.append(teams.rstrip("\n"))
for drops in f2:
    lst.append(drops.rstrip("\n"))

st=set(lst)
Qualifers=st1.difference(st2)
print(Qualifers)


