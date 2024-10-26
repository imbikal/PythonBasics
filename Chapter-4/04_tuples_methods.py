# Methods ussed in tuple

a = (1,34,25,55,"AI","Udemy","Coursera",55,"Python")
print(a)

number = a.count(55)

print(number) # Here the answer is 2 because 55 is there in the list just 2 times
              # This is .count works in tuple

i = a.index(55)
print(i) 

#The index of 55 is 3 so the answer is 3. 

 # There is 55 in 7 as well but it is not included as the program already founded 55.

print(len(a)) # Prints the length of the tuple (a)

