#Program to remove given word from a list and strip at a same time

def rem(l,word):
    n = []
    for item in l:
        l.remove(word)
        return l


l = ["Soyebah","Bikal","Ryle","Atlas"]

print(rem(l,"Atlas")) 

