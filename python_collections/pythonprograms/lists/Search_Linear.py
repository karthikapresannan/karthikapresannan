arr=[1,2,3,4]
element=int(input("enter the element"))
flg=0
for num in arr:
    if (element==num):
        flg==1
        break
if flg==0:
    print("element is not found")
else:
        print("element is found")
