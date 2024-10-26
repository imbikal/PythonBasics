#Inheritence is a way of creating new class from an existing base class

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is{self.salary} ")


    # class Programmer:
    #     company = "ITC Infotech"
    #     def show(self):
    #         print(f"The name is {self.name} and the salary is {self.salary}")

    #     def showLanguage(self):
    #         print(f"The name is {self.name} and he is good with {self.language} language")   


class Programmer(Employee): #Programmer has been inherited from base class Employee
    company = "IIT InfoTech"
    def showLanguage(self):
      print(f"The name is {self.name} and he is good with {self.language}") 

        
a = Employee()
b = Programmer()

print(a.company,b.company)
            
                 

