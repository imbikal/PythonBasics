f = open("file.txt")
print(f.read())
f.close()

#The same can be written using the statement like this:

with open("file.txt") as f:
    print(f.read())