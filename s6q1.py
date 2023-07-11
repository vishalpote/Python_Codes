s1=set()
s2=set()
for i in range(1,11):
    s1.add(i)
for j in range(11,21):
    s2.add(j)
print(s1)
print(s2)
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
s6=s1.symmetric_difference(s2)
print(s6)

