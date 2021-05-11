#Chef proxy

import math

tcases = int(input())

def proxy_condition(posi,strr):
    if (strr[posi-2] == 'P' or strr[posi-1]=='P') and (strr[posi+1] == 'P' or strr[posi+2] =='P'):
        return True
    else:
        return False


while tcases != 0:
    D = int(input())
    str = input() #"abcd"

    #Minimum no times we have to mark him to make 75%
    present = 0
    for char in range(0, len(str)):
        if str[char] == 'P':
            present += 1
    min_no = math.ceil(.75 * D) - present
    #print("Min att req is",min_no)

    m = min_no
    start=2
    #Now we have to mark him proxy
    #print("Entering while loop")
    while 1:

        if str[start]=='A': #If absent, check can we mark his proxy, else move next
            if proxy_condition(start,str):
                m=m-1 #Proxy lga di
                print("Proxy successful at position",start)
        start +=1
        if start == D-2 or m==0: #If we reach end of string, or did the minimum no of proxies
            #print("Breaking out of while loop")
            break
    #print("Value of index(OUT loop) is",start)
    #print("Value of m is",m)

    if m==0:           #All min_required_proxies used
        print(min_no)
    else:
        print(-1)  #Couldn mark his min proxy





    tcases = tcases-1