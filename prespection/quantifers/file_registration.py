from re import*
rule="KL\d{2}[A-Z]{2}\d{1,4}"
f=open("reg")
lst=[]
for regno in f:
    regno=regno.rstrip("\n")
    matcher=fullmatch(rule,regno)
    if matcher!=None:
        lst.append(regno)
print(lst)r