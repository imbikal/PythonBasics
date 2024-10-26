#Recursive function for sum of 1st n natural numbers

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n    

print(sum(4)) 