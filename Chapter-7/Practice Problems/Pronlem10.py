#Write a program to print multiplication table of n using for loops in reversed order


n = int(input("Enter any number: "))

for i in range(1,11):   # Range works as (n,n-1)
    print(f"{n} X {11-i} = {n*(11-i)}")
