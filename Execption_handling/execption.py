#no1=int(input("enter the number1"))#10
# no2=int(input("enter the number2"))#0
# try:
#     res=no1/no2
#     print(res)
# except Exception as e:
#     no2=int(input("enter th number"))#0
#     try:
#         res=no1/no2
#         print(res)
#     except Exception as e:
#         print(e.args)
#     finally:
#         print("data base operation")
#         print("file write")



# num=int(input("enter the num"))#10
#
# try:
#     if age<18: # actually this type expection is not found
#         raise Exception("invalid age")
# except Exception as e:
#     print(e.args)


num= int(input("enter the num"))
try:
    if num<0:
        raise Exception("invalid")
except Exception as e:
        print(e.args)


