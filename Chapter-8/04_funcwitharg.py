#Function wit Argument

def GoodDay(name):   
    print("Good Day!!"  + name)

GoodDay("Hero")

#Here name is an argument, similary we can add up arguments

def GoodDay(name,ending):   
    print("Good Day!!"  + name, end=" ")
    print(ending)

GoodDay("Hero", "Prasad")