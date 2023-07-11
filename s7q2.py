# Outer loop
for i in range(65,):
    k=i
    # Inner loop
    for j in range(65,i+1):
        print(chr(k),"\t",end="")
        k=k+1
    print()