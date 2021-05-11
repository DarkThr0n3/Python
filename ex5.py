#Practicing print(f"") 

#Exercise 5

my_name = 'Sankalp'
my_age = 23

my_state = f"Hiiii my name is {my_name} and age is {my_age}"

print(my_state)

funny = (3 > 4.000)
joke = "Isnt this so easy? {}"

print(joke.format(funny))
print(int(funny))

#Using .format type for more than 2

str1 = "Ek bol pe {} chowke aur ek life men {} mauke nahi milte loll".format('2','3')

print(str1)

#Using double vs triple quotes

#print("Ek
#do
#teen") EOL syntax error while scanning string literal


print("""ek
do
teen""")

#Using input()

age = input("Kitni Umar bhai sab?")
print(age)


