#Ex 24---More Practice

print("Lets practice everything")
print('You\'d need to know \'bout escapes with \\ that do')

poem = """Choot men lund nahi
Hum kisi se kam nahi"""

print("-----------")
print(poem)
print("-----------")

five = 8-3

print(f"This should be {five}")

def secret_formula(started):
    jbeans = started * 500
    jars= jbeans/1000
    crates = jars /100
    return jbeans, jars, crates

start_point = 10000

beans,jars,crates = secret_formula(start_point)

#format string
print("With a starting point of: {}".format(start_point))
#Just like f"" strings with variables inside {} quotes
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point/10

print("We can also do this way")

formula = secret_formula(start_point)

print("Type of formula is ",type(formula))

#This is easy way to apply list to format string
print("We'd have {} beans,  jars, and  crates".format(formula))