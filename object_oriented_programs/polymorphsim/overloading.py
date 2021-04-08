class Maths:

    def add(self):
        print("inside no arg math method")

    def add(self,num1):
        print("inside single arg math method")

    def add(self,num1,num2):
        print("inside two arg math method")
        #last il koduthekuna arugument mathrame python run cheyathollu

math=Maths()
math.add(10,20)



#math.add(10) its not working bacause one argument is missing
#only obe class in overloading