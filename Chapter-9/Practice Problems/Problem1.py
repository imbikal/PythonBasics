f = open("poem.txt")
content = f.read()
if("Twinkle" in content):
    print("Yes,Twinkle is there")
else:
    print("Twinkle is not present")    
f.close()