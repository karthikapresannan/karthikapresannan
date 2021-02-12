lst=[1,2,3,4]
low=0
pair=6
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp]
    if pair==total:
        print(lst[low],lst[upp])
        low+=1
    elif total>pair:
        upp-=1
    elif total<pair:
        low+=1