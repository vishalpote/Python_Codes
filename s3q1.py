import numpy as np
l=[]
for i in range(1,11):
    l.append(i)
x=np.array(l)
print("the original array is:")
print(x)
print("the reversed array is:")
y=np.flip(l)
print(y)