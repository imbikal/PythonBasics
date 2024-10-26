class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Bikal",1200000,245001)
print(p.name,p.salary,p.pin,p.company)    

h = Programmer("Hero",1200000,245001)
print(h.name,h.salary,h.pin,h.company) 
      