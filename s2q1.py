l=[]
# x=int(input("how many element:"))
# for i in range(x):
    # l.append(int(input("enter the element:")))
for i in range(1,11):
    l.append(i)
print(l)
a=[k for k in l if k%2==0]
print(a)
b=[j for j in l if j%2]
print(b)