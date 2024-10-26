#Python Problem using function to covert Celcius to Fahrenheit

#c/5 = (f-32)/9 or # 5*(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temprature in F: "))
c = f_to_c(f)
print (f"{round(c,2)} Degree C")  #round round off decimal to 2 places here