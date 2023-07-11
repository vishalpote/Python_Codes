m=int(input("enter the starting point:")) 
n=int(input("enter the ending point:"))
for v in range(m,n+1):
    for i in range(1,11):
        print(v,"x",i,"=",v*i,)
    print("\n")