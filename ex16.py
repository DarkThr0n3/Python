#Reading and Writing FIles

from sys import argv

script , filename = argv
print(f"Now we\"are going to erase {filename}")
print("If you dont want that, hit CTRL-C (^C)")
print("If you want to go ahead, hit ENter/Return")

input('?')

print("Openingn the file...........")
target = open(filename, 'w') #If you omit 'w' , you will see error on truncate() and write() commands, FIle not open for writing

print("Truncating the file (Erase), GoodBye! \n with target.truncate() command\n.........")
target.truncate()

print("Now I am gonna ask you three lines")
line_1 = input("First line")
line_2 = input("Second line")
line_3 = input("3rd line")

print("Now we gonna write these 3 lines to the file")

target.write(f"{line_1} \n{line_2} \n{line_3}\n")


print("And finally we gonna close it (Like save-AS")
#target.seek(0) #This will overwrite, first line instead of appending it

target.write("1\2\3\4") 
target.close() #When I openethe file, cursor was in end, so I decided to use seek :-/ Didnt solved it

