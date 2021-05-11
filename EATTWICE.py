tcases = int(input())

for x in range(tcases):
    NM = input()
    NM = NM.split(' ')
    N = int(NM[0]) #  N dishes
    M = int(NM[1]) #  M days

    tasty = 0

    DV = [] #(d,v) values tupless dth day, v tastiness , yth dish
    for y in range(N):
        dv = input()
        dv = dv.split(' ')
        d = int(dv[0])
        v = int(dv[1])
        DV.append((d,v))

    #Start with most tasty dish, add it, if dishes collide select maximum ne
    DVs = sorted(DV, key = lambda i:i[1],reverse=True) #We have highest tasty dish in line

    dmax,vmax = DVs.pop(0)
    #we will eat this dish
    tasty +=vmax

    #Eat any ish other than this day (dmax)
    for x in DVs:
        if x[0] == dmax: #we cannot eat it, skip this
            continue
        elif x[0] != dmax: #Eat this second dish
            tasty+= x[1]
            break

    print(tasty)





