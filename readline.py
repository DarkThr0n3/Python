#Using readline

from sys import argv

script , filename = argv 

open_file = open(filename) 

line1 = open_file.readline()
line2 = open_file.readline()
line3 = open_file.readline()
line4 = open_file.readline()
line5 = open_file.readline()

print("Lines are ready")
print("Line 1 --->",line1)
print("Line 2 --->",line2)
print("Line 3 --->",line3)
print("Line 4 --->",line4)
print("Line 5 --->",line5)
