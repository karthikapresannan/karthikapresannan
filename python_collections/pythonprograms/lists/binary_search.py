arr=[10,16,12,17,19,18,16,13,11,15,20]
element=(int(input("enter the element")))

arr.sort() #array sort cheyan

flg=0
low=0

upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2

    if (element>arr[mid]):
        low=mid+1

    elif(element<arr[mid]):
        upp=mid-1

    elif(element==arr[mid]):
        flg=1
        break

if flg==0:
        print("element is not found")     #enter the element1
                                         #element is not found
else:
        print("element is found")       #enter the element12
                                        #element is found


#middle value=first postion+last postion /2
