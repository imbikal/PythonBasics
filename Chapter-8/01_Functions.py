#Functions in Python are blocks of code that are designed to perform a specific task.

#a = int(input("Enter your number: "))
#b = int(input("Enter your number: "))
#c = int(input("Enter your number: "))

#average = (a+b+c)/3
#print(average)

#a = int(input("Enter your number: "))
#b = int(input("Enter your number: "))
#c = int(input("Enter your number: "))

#average = (a+b+c)/3
#print(average)

"""
If we just continue doing this number of lines will be long, function gives name 
to this logic to make sure effective work
"""

def avg():                             #A function avg is defined/Definition function
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

    avg()                                 #This runs the defined function

    """
    If I want to repeat the steps of getting average again i can just simply
    repeat the function as many times and that's it
    Here I want to take average 5 times so i just type avg() 5 times
    avg()
    avg()
    avg()
    avg()
    avg()
    """