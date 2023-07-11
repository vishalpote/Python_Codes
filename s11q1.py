m=int(input("enter the starting point:"))
n=int(input("enter the ending point:"))
l=[]
for i in range(m,n):
    if(i%3==0 and i%7!=0):
        l.append(i)
print(l)