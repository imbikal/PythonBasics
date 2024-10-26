"""
Write a program to print the following star pattern.
  *
 ***
***** for n = 3
"""

n = int(input("Enter any number: "))
for i in range (1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("\n")


"""What does end do??

With end: 
print("Hello", end="")
print("World!")

Answer is : HelloWorld!


Without end:
print("Hello")
print("World!")

Answer is: Hello
           World!
  



"""

