# write a program to find out whether a student is pass or a fail if it requires a total 40% and at least 33% in each subject to pass.assume 3 subjects and take a marks as an input from the user.
sub1 = int(input("enter the marks in sub1 :"))
sub2 = int(input("enter the marks in sub2 :"))
sub3 = int(input("enter the marks in sub3 :"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
    
elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to less percentage below 40")    
else:
    print("congratulations! you pass the exam")