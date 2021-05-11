#Ex 16 
#Reading Files

#Importing from argc
from sys import argv

#Unpacking argv 
script , filename = argv

#Open, similar to fopen in C, to open file with file_path_name relative to CWD
txt = open(filename)

print(f"Here's your file {filename} :")

# Using dot.read() to see contents of file
print(txt.read())

#Closing it appropriately
txt.close()

#Using input() to read file
print("Type the filename again:")
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
