
#Break in loop 

for i in range(100):
    if (i==34):
        break       #Exit the loop after getting 34
    print (i)      # This print 0 to 33, rather than 0 to 99

    
#Continue in loop

for j in range(100):
    if (j==34):
        continue      #Skip just the number 34 and print remaining 
    print (j)    


#Pass in Python
for i in range(300):
    pass             #"Pass" is basically do nothing / I'll do it later 


i = 0
while(i<45):
    print(i)
    i = i + 1
