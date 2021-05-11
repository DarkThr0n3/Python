# Challenge command line arguments
#C1 - -help feature

#C2 - 3 flags (-i -str -null -h)

#C3 - 3 options for variables (option1 option2 option3)

#C4 - POsitional arguments - (list of files ) (open)

def help():
    print("Please refer help\npython3.6 ex4.py (-help)or(-h)")

def flag(fl):
    global var1,var2,var3

    print("inside flag")

    if fl == "-i":
        var1 = int(var1)
        var2 = int(var2)
        var3 = int(var3)

    elif fl == "-pr":
        print(f"var1 is {var1}, var2 is {var2}, and var3 is{var3}")

    elif fl == "-null":
        var1 ,var2, var3 = null

    elif fl =="-h" or "-help":
        print("somehow")

def option(op, arg):

    if op == "option1":
        var1 = arg
    elif op == "option2":
        var2 = arg
    elif op == "option3":
        var3 = arg
    else:
        print("no such option")
        help()


#T1 Taking user input (probelm in unpacking)
import sys

input = []
input = sys.argv

#print("input is")
#for i in input:
#    print(i)             Works correctly hooray
var1, var2, var3 = "1", "2" ,"3"
no = 0
#T(pre2) If any input wrong , show help
#T2 identifying flag(space with space), option, positional_argument or help
optionflag =0
#order when will end?
for intake in input:

    if optionflag == 1:
        optionflag = 0
        continue
#Starting input from first arguments
    if intake == "ex4.py":
        no = no+1
        continue #Do nothing

    if intake == "-i" or "-pr" or "-null" or "-h" or "-help":
        flag(intake)
        no = no+1

    if intake[:6] == "option":
        option(intake , input[no+1])
        optionflag = 1
        no = no + 2

    else:
        help()
