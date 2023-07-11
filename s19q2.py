class emp():
    def __init__(self):
        self.id=int(input("enter the id :"))
        self.n=input("enter the name :")
        self.dep=input("enter the department :")
        self.sal=int(input("enter the salry :"))
    def show(self):
        print("emp id:",self.id)
        print("emp name:",self.n)
        print("emp departement:",self.dep)
        print("emp salary:",self.sal)
class manager(emp):
    def __init__(self):
        emp.__init__(self)
        self.bonus=float(input("enter the bonus:"))
    def show1(self):
        emp.show(self)
        print("employee bonus:",self.bonus)
l=[]
n=int(input("how many manager you want:"))
m=0
k=0
for i in range(n):
    l.append(manager())

for i,j in enumerate(l):
    if m<j.sal+j.bonus:
        m=j.sal+j.bonus
        k=i
print("employee detail with max salary:")
print(l[k].show())