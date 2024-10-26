def GoodDay(name,ending="Thank You"):
    print(f"Good Day!!,{name}")
    print(ending)

GoodDay("Hari","Thanks") 
GoodDay("Ram")

"""
When writing GoodDay("Hari","Thanks") the answer is
Good Day!!,Hari
Thanks
because name,ending is mentioned at last / specifically "Thanks" is mentioned

"""

"""
When writing GoodDay("Ram") the answer is 
Good Day!!,Ram
Thank You
because since just name is mentioned now ending="Thank You" is used in case if 
specifically it is not used / its by default if ending is not mentioned
"""