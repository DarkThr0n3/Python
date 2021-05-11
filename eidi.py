#eidi gifts

#3 age , 3 Ci - fair if greater

tcases = int(input())

for i in range(0,tcases):
    A_C = input().split(' ')

    for l in range(0, len(A_C)):
        A_C[l] = int(A_C[l])

    coll = []
    coll.append([A_C[0],A_C[3]])
    coll.append([A_C[1], A_C[4]])
    coll.append([A_C[2], A_C[5]])

    coll.sort(key=lambda x: x[0]) #sorted by age ascending , increasing

    #print(coll)

    flag = 0
    if coll[0][0] == coll[1][0]: #Same age, should be equal only
        if coll[0][1] != coll[1][1]:
            flag=1
            #print("one")
            #print(flag)


    else: #different age , should be less only
        if coll[0][1] >= coll[1][1]:
            flag=1
            #print("two")
            #print(flag)

    if coll[1][0] == coll[2][0]:
        if coll[1][1] != coll[2][1]:
            flag = 1
            #print("three")
            #print(flag)
    else:
        if coll[1][1] >= coll[2][1]:
            flag=1
            #print("four")
            #print(flag)

    if flag == 1:
        print("NOT FAIR")
    else:
        print("FAIR")

