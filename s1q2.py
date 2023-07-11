n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
print("the given number is perfect" if(sum==n) else "the given number is not perfect")