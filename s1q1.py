s=input("enter the string:")
x=""
for i in range(len(s)):
    if i%2:
        x=x+s[i]
print(x)