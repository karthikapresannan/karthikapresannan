class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return book(self.pages + other.pages)
                                            #######obj.pages(100)+obj1.pages(200)
    def __sub__(self, other):
        return book(self.pages - other.pages)
                                            ######obj.pages(100)-obj1.pages(200)
    def __str__(self):
        return str(self.pages)

obj=book(100)
obj1=book(200)
obj2=book(300)
print(obj+obj1+obj2)
print(obj2-obj1-obj)
