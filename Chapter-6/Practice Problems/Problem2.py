# Program to find whether a student has passed or fail
# Considering total 40% and at least 33% each subject to pass
# Assume 3 subjects and take marks as input from user

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

#Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300 

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed",total_percentage)

else:
    print("You are failed,appear for re-exam",total_percentage)

