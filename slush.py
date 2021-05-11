import operator

tcases = int(input())

for x in range(tcases):
    NM = input()
    NM = NM.split(' ')
    N = int(NM[0])   #N customers
    M = int(NM[1])   #M flavours
    C = input()
    C = C.split(' ') #C(1) to C(M)

    ans2 = ''

    i=0
    for c in C:
        C[i] = int(c)
        i+=1

    #input details
    Ndet = []
    for y in range(N):
        det = input() # 'D F B'
        det = det.split(' ')
        D,F,B = int(det[0]) , int(det[1]), int(det[2])
        Ndet.append((D,F,B))

    #algorithm to sell
    for sell in range(N): #Selling one by one

        #Note av flavour
        fav_fla = Ndet[sell][0]

        if C[fav_fla-1] != 0: #provide him his fav cup if available
            money += Ndet[sell][1]  #take money
            C[fav_fla-1]-= 1        #Give him his cup

            ans2 = ans2 +str(fav_fla)+' '
            continue

        else:
            #Algrithm which cup to give-away to this sad guy
            #1 Select drink which is nones favourite
            #2 Select drink of least paying guy
            rem_people = Ndet[sell+1:]
            rem_people.sort(key= operator.itemgetter(1, 2))


