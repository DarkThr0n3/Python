t = int(input())


def ret(c):
    if c==1:
        return(2)
    elif c == 2 or c==3 or c==5 :
        return(5)
    elif c==4:
        return(4)
    elif c==6 or c==9 or c==0:
        return(6)
    elif c==7:
        return(3)
    elif c==8:
        return(7)



for x in range(0,t):
    ab = input().split(' ')
    a = int(ab[0])
    b = int(ab[1])

    res = a+b
    r=0
    while res !=0:
        no = res%10
        r = r+ ret(no)
        res = int(res/10)

    print(r)




