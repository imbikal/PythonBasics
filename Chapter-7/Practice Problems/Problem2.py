""" Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry","Soham","Sahil","Soyebah"]
"""

l = ["Harry","Soham","Sahil","Soyebah"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
