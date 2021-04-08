# from  re import*
# rule="[a-kA-K][369][a-zA-Z0-9]*"
# variableename=input("enter variable  name")
#
# matcher=fullmatch(rule,variableename) #fullmatch means exact match
#
# if matcher!=None:
#     print("registration variable name")
# else:
#     print("invalid")



from re import*
rule='Kl\d{2}[A-Z]{2}\d{1,9}'
variablename=input("enter variable name")
matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("registration variable name")
else:
     print("invalid")