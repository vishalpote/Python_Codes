class stud():
    def __init__(self):
        self.id=int(input("enter student id:"))
        self.n=input("enter student name:")
        self.age=int(input("enter student age:"))
        self.g=input("enter student gender:")
    def show(self):
        print("student id:",self.id)
        print("student name:",self.n)
        print("student age:",self.age)
        print("student gender:",self.g)
class test(stud):
    def __init__(self):
        stud().__init__()
        self.p=int(input("enter the marks for python:"))
        self.w=int(input("enter the marks for web:"))
        self.ds=int(input("enter the marks for data structur:"))

    def show1(self):
        print("marks of pyhon:",self.p)
        print("marks of web:",self.w)
        print("marks of data structures:",self.ds)
    def perc(self):
        self.v=(self.p+self.w+self.ds)/3
        return self.v

l=[]
max=0
id=0
n=int(input("how many student:"))
for i in range(n):
    l.append(test())
for i,j in enumerate(l):
    if max<j.perc():
        max=j.perc()
        id=j
print("highest percente of the student is:")
print(l[id].show1())