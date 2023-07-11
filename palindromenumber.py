x=int(input("enter the number:"))
rev=0
c=x
while x!=0:
    rev=(rev*10)+(x%10)
    x=x//10
print("the given number is palindrome" if rev==c else "the given number are not palidrome")
