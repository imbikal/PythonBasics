#A file is a data stored in a storage device. A python program can talk to the
#file by reading content from it and writing content to it.

f = open("file.txt") # Since this is readmode so ,"r" no need to include inside ()
data = f.read()
print(data)
f.close()
