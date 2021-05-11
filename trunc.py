from sys import argv

script , filename = argv

print("Trunating the whole file")

fopenn = open(filename,'w')

fopenn.truncate()

print("Displaying file now after truncate")

#content = fopenn.read()  ---> gives error not readable, which means file is now empty
#print(content)

#Okay so lets write something to our chootfile
print("Writing to file")
fopenn.write(str(3>4))
fopenn.write('\nConquer the habits, conquer yourself')

print("Finished writing!")
fopenn.close()
newopen= open(filename)
contents = newopen.read()

print("Printing Contents-->", contents)
