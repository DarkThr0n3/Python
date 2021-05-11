#Intervie q for bloomberg, which i fucked up dramatically

#Unfold given string 4[ab]3[c]2[2[a]]abc3[e]22[a]


def print_str(stringg):
    #1 Scan number
    n=0
    while stringg[n]!='['
        number[n]=stringg[n]

    num = int(number)

    #2 Scan string part
    str = stringg[n+1:-1]
    str = eval_str(str)

    print(num*str)

while 1:
    string = input()



