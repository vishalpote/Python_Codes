s=set()
x=int(input("how many element:"))
for i in range(x):
    s.add(int(input("enter the element:")))
print(s)
count=0
for j in s:
    count+=1
print("the length of the set is:",count)



# or
'''s={i for i in range(1,11)}
print(s)
count=0
for j in s:
    count+=1
print("the length of the  set is",count)'''