#write a program to print a multiplication table using for loop

num = int(input("enter the number"))

for i in range (1,11):
    print(str(num) +"x" + str(i) + "=" + str(i*num))