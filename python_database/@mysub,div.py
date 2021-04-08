def my_sub(func):
    def innerfunc(num1,num2):
        if(num1<num2):
            num1,num2=num2,num1
            return func(num1,num2)
    return innerfunc
@my_sub
def sub(num1,num2):
    return  num1-num2
print(sub(10,20))


def my_div(func):
    def innerfunc(num1,num2):
        if(num1<num2):
            num1,num2=num2,num1
            return func(num1,num2)
    return innerfunc
@my_div
def div(num1,num2):
    return  num1/num2
print(div(10,20))
