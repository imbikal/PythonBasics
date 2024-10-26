# len is used to showcase length of the string

name = "Bikal"
print(len(name)) # length of string
print(name.endswith("kal")) # check if that ends with "kal" or not
print(name.startswith("Bi")) # check if that starts with "Bi" or not
print(name.capitalize()) # to capitalize the first letter

# this function replaces old word with new word
example = "Hello World"
replaced_string = example.replace("Hello","Ohayo")
print(replaced_string)