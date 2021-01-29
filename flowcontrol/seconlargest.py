num1=int(input("enter the first number"))
num2=int(input("enter the second nmber"))
num3=int(input("enter the third number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"is second largesr")
    else:
        print(num3,"second")
    print("num1 is greater")
elif(num2>num1)&(num2>num3):
    if(num1>num2):
        print(num1,"second largest")
    else:
        print(num3,"nu3 is greater")
elif(num3>num1)&(num3>num2):
    if(num1>num3):
        print(num1,"is scond large")
    else:
        print("num2 is second")
else:
    print("invalid")