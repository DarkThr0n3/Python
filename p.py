#Chef proxy

import math

tcases = int(input())

def proxy_condition(posi,strr):
    if (strr[posi-2] == 'P' or strr[posi-1]=='P') and (strr[posi+1] == 'P' or strr[posi+2] =='P')
        return True
    else:
        return False


while tcases != 0:
    D = int(input())
    str = input()

    #Minimum no times we have to mark him to make 75%
    present = 0
    for char in range(0, len(str)):
        if str[char] == 'P':
            present += 1
    min_no = math.ceil(.75 * D) - present

    print(min_no)





    tcases = tcases-1