d={}
x=int(input("how many element:"))
for i in range(x):
    k=input("enter the key:")
    v=input("enter the value:")
    d[k]=v
sorted(d)
print(d)
