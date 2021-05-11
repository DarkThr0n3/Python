#ex 13 Prompting people
#Ex 13 Input by Argument

from sys import argv
#read the WYSS section for how to run this

script , first, second, third = argv

print(f"you typed {script} , with 1st arg {first} ,2nd {second} and 3rd{third}")

#Interesting - Command line arguments are strings, just like in C 
#Just like input
#We use int() to convert numbers
