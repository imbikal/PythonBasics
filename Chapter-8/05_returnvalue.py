
def GoodDay(name,ending):   
    print("Good Day!!"  + name, end=" ")
    print(ending)
    return "ok"

a = GoodDay("Hero", "Prasad")
print(a)

#When a function reaches a return statement,it ends the function and gives the value
#specified after return to whatever called the function.