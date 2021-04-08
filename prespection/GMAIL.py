from re import*
rule="[a-zA-Z0-9]{1,64}@gmail.com"
emailid=input("enter the email")
matcher=fullmatch(rule,emailid)
if matcher!=None:
    print("registration email id ")
else:
     print("invalid")