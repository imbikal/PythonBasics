# What will be the length of the following

s = set()
s.add(30)
s.add(30.0)
s.add('30') # length of s after these operations?

print(len(s))

# The answer is 2 because 30==30.0 since values are same so datatypes doesnt matter

