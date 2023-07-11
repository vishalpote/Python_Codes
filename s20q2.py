def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
    while low <= high:   
        mid = (high + low) // 2     
        if list1[mid] < n:  
            low = mid + 1  
        elif list1[mid] > n:  
            high = mid - 1   
        else:  
            return mid  
    return -1  
l=[]
m=int(input("how many element:"))
for i in range(m):
    l.append(int(input("enter the element:")))
print(l)  
n = int(input("enter the number you find:"))   
x = binary_search(l, n)  
if x != -1:  
    print("Element is present at index", str(x))  
else:  
    print("Element is not present in list1") 