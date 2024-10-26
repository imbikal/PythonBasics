with open("file.txt") as f:
    content1 = f.read()

with open("donkey.txt") as f:
    content2 = f.read()    

if(content1 == content2):
    print("yes these two are identical")

else:
    print("No these files are not identical")
