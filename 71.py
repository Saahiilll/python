# write a program to calculate the grade of a student from his marks from the following scheme
# 100-90 A
# 90-80 B
# 80-70 C
# 70-60 D
# 60-50 E
# >5O F


marks = int(input("enter your marks\n"))

if marks>=90:
    grade = "A"
elif marks>=80:
    grade = "B"
elif marks>=70:
    grade = "C"
elif marks>=60:
    grade = "D"
elif marks>=50:
    grade = "E"
else:
   
   
    print("your grade is" + grade)
   
    