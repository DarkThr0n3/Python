#Reading writing files python

from sys import argv

script , filee = argv #Unpacking arguments

print("Type of filee( i guess string) is",type(filee))
open_file = open(filee)

print("Reading contents!!!!!!")
content = open_file.read()
print("Contents read!")

print("Displaying contents")

print(content)

print("Finished displaying")


