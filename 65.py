#write a program to find greatest of four numbers entered by the user
num1 = int(input("enter the first number : \n"))
num2 = int(input("enter the second number : \n"))
num3 = int(input("enter the third number : \n"))
num4 = int(input("enter the fourth number : \n"))

if(num1>num2):
    f1=num1
else:
    f1=num2
    
if(num3>num4):
    f2=num3
else:
    f2=num4
    
if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")    