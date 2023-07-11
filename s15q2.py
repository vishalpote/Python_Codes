class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def delete(self):
        return 0
    def __del__(self):
        print("object delete")

x = Rectangle(l=float(input("enter the length:")), w=float(input("enter the width:")))
print(x.area())
print(x.perimeter())
del x
