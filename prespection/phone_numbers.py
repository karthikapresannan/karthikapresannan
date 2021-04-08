from re import*
rule='[0-9]{10}'
phone_number=input("enter the phone number")
matcher=fullmatch(rule,phone_number)
if matcher!=None:
    print("registration phone numbeer ")
else:
     print("invalid")