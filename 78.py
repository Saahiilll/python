# write a program to find the percentage using the functiom
def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[45,56,67,78]
percentage1 = percent(marks1)
marks2=[54,65,76,87]
percentage2 = percent(marks2)

print(percentage1,percentage2)