l=[]
x=int(input("how many element:"))
for i in range(x):
    l.append(input("enter the element:"))
t=tuple(l)
print(t)
k=int(input("which number u want :"))
c=t.count(k)
print(c)