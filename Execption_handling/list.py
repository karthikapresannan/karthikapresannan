lst=[1,2,3,4]
postion=int(input("enter the postion"))
try:
    print(lst[postion])

except:
     print("execption occure")

# except Exception as e:
#     print(e.args)  #('list index out of range',)