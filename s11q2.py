def cal():
    x=int(input("enter the first number:"))
    z=int(input("enter the second number:"))
    print("1.ADDITION:\n")
    print("2.SUBTRACTION:\n")
    print("3.MULTIPLICATION:\n")
    print("4.DIVISION:\n")
    print("5.REMAINDER:\n")
    print("6.SQUARE:\n")
    y=input("enter your choice:")
    if(y=='1'):
        print("the adition is:",(x+z))
    elif(y=='2'):
        print("the subtraction is:",x-z)
    elif(y=='3'):
        print("the multiplication  is:",x*z)
    elif(y=='4'):
        print("the subtraction is:",x/z)
    elif(y=='5'):
        print("the subtraction is:",x%z)
    elif(y=='6'):
        print("the subtraction is:",x**2,z**2)
cal()
