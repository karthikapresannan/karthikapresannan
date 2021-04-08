# map() map is use to find sqaure or cube of the 'n' number in the list
# filter()
# reduce()


lst=[1,2,3,4,5,6,7,8,9]
sq=list(map(lambda num:num**2,lst))
print(sq)


even=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda num:num%2==0,lst))
print(evens)


number_greater_than_3=[1,2,3,4,5,6,7,8,9]
number_greater_than_3=list(filter(lambda num:num>3,lst))
print(number_greater_than_3)



