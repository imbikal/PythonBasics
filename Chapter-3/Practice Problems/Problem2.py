letter = ''' Dear <|Name|>,\n You are selected!\n <|Date|> '''

print(letter.replace("<|Name|>","Bikal").replace("<|Date|>","22 Feb"))

# .replace function can be chained as above / chaining function