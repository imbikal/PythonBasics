class Employee:                   #Creating a class, this is like default ones
    language = "English"
    salary = "Infinite"


Bikal = Employee()               #Creating an object with custom values
Bikal.name = "Bikal"
print(Bikal.name,Bikal.salary)    

Soyebah = Employee()
Soyebah.name = "Soyebah Majeed"
print(Soyebah.name,Soyebah.salary)


# Here name is object/instance attributes and salary and language arre calss attributes as they directly belong to the class

#Instance attributes are priotized over class attributes