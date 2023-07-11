def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
n=gcd(x=int(input("enter the number:")),y=int(input("enter the number:")))
print("the gcd of two number is:",n)