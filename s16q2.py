class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        m=self.radius**2*3.14
        print("the area of the circle is:",m)    
    def circumferance(self):
        n=2*self.radius*3.14
        print("the circumfarnace of the circle is:",n)

NewCircle = Circle(int(input("enter the radius of circle:")))
print(NewCircle.area())
print(NewCircle.circumferance())
