"""
Create an empty dictionary. Allow 4 friends to enter their favourite language as value
and use keys as their names. Assume that the names are unique

"""

d = {}

name = input("Enter friends name: ")
lang = input ("Enter language name: ")

d.update ({name : lang})
name = input("Enter friends name: ")
lang = input ("Enter language name: ")

d.update ({name : lang})
name = input("Enter friends name: ")
lang = input ("Enter language name: ")

d.update ({name : lang})
name = input("Enter friends name: ")
lang = input ("Enter language name: ")




print(d)