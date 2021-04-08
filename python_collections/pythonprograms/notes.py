for row in range(1,6):
    for col in range (1,10):
        if (row==5) | (row+col==6) | (row-col==4):
            print("*",end="")
            print("*")
        print("*")
print("*",end="")