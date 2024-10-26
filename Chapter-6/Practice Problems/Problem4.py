#Write a program to find whether a given username contains less than 10 characters or not

username = input("Enter a username: ")

if(len(username)<10):
    print("Username is too short")

else:
    print("Username exceeds 10 character limit")