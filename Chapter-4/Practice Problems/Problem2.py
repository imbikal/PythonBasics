# Program to accept marks of 6 students and sort them in ascending order

marks = []

mark1 = int(input("Enter mark here: "))
marks.append(mark1)

mark2 = int(input("Enter mark here: "))
marks.append(mark2)

mark3 = int(input("Enter mark here: "))
marks.append(mark3)

mark4 = int(input("Enter mark here: "))
marks.append(mark4)

mark5 = int(input("Enter mark here: "))
marks.append(mark5)

mark6 = int(input("Enter mark here: "))
marks.append(mark6)

marks.sort()
print(marks)