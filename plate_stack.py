for t in range(int(input())):
    nkp = input().split()
    n,k,p = int(nkp[0]),int(nkp[1]),int(nkp[2])

    plate_stack = [[] for _ in range(n)]

    for i in range(n):
        st = input().split()
        st = [int(x) for x in st]

        beauty = 0
        plate_stack[i].append(beauty)
        for ii in range(k):
            beauty+=st[ii]
            plate_stack[i].append(beauty)

    print("OK so plate stack is\n{}".format(plate_stack))
    #Solving for test case 1 1<=N<=3

    if n==1:
        print("Case #{}: {}".format(t+1, plate_stack[0][p-1]))
    elif n==2:
        if k>=p:
            rp = 0
        else:
            rp = p-k
        max2= 0
        j=rp
        for i in range(k,-1,-1):
            print("i {} j {}\n{} {}\nSum {}\n\n".format(i,j,plate_stack[0][i],plate_stack[1][j],plate_stack[0][i]+plate_stack[1][j]))
            max2= max(max2,plate_stack[0][i]+plate_stack[1][j])
            j+=1
            if j==k+1:
                break
        print("Case #{}: {}".format(t+1, max2))
    else:
        max3=0
        for i in range(0,k+1):
            for ii in range(0,k+1):
                for iii in range(0,k+1):
                    if i+ii+iii==p:
                        max3 = max(max3, plate_stack[0][i]+plate_stack[1][ii]+ plate_stack[2][iii])
        print("Case #{}: {}".format(t+1, max3))
