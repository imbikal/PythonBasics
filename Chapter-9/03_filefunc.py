f = open("file.txt")

#lines = f.readlines()       This reads all lines of file.txt
#print(lines,type(lines))  

line1 = f.readline()       # This reads line 1 of file.txt
print(line1,type(line1))

line2 = f.readline()       # This reads line 2 of file.txt
print(line2,type(line2))  

f.close()