lst=[3,4,2,6,7,8]
# for i in lst:
#     if i>5:
#         print(i+1,end=",")
#     else:
#         print(i-1,end=",")

num=[i-1 if i<5 else i+1 for i in lst] #print less than 5 in the list (so i-1)
                                        #print greater than 5 in the list (so i+1)
print(num)