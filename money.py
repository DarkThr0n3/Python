for t in range(int(input())):
    sn = input().split()
    s = int(sn[0])
    n = int(sn[1])

    mini_coins = 0

    if s>=n:
        mini_coins+=int(s/n)
        s = s%n

    if s==0:
        pass
    elif s==1 or s%2==0:
        mini_coins+=1
    else:
        mini_coins+=2
    print(mini_coins)
