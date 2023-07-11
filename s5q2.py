print("1.factorial number:\n")
print("2.revrese number:\n")
print("3.exit:\n")
c=int(input("enter your choice:"))
if(c==1):
    x=int(input("enter the number:"))
    f=1
    if x==1 and x==0:
        print(1)
    else:
        for i in range(1,x+1):
            f=f*i
        print(f)
elif(c==2):
    x=int(input("enter the number:"))
    rev=0
    while(x!=0):
        rev=rev*10+(x%10)
        x=x//10
    print(rev)
else:
    exit()
