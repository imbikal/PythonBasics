class Employee:
    language = "English"
    salary = "Infinite"

    def __init__(self): #Dunder method which is automatically called
        print("I dont have to write Bikal. and something at last while using init")


    def getInfo(self):  # Method needs to be inside the class and include 'self'
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  #This makes sure (self) is not required
    def greet():  # Method needs to be inside the class and include 'self'
        print("Good Morning")

Bikal = Employee()
Bikal.getInfo()  # Correct method call
Bikal.greet()    # Correct method call
