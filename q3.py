#Test Case 1 - K==1
#Why wont it let me pass bc....? :-/

for t in range(int(input())):
    nk = input().split()
    nk = [int(x) for x in nk]

    ns = input().split()
    diff = []

    print("ns is {}".format(ns))

    for i in range(nk[0]-1):
        d = int(ns[i+1]) - int(ns[i])
        print("appending {}".format(d))
        diff.append(d)



    diff.sort(reverse = True) #Descending

    print("diff is {}".format(diff))
    #K==1


    a = int(diff[0]/2)
    if len(diff)==1:
        ans = a
    elif diff[0]==diff[1]:
        ans = int(diff[0])
    else:
        ans = a if a>diff[1] else int(diff[1])
    print("Case #{}: {}".format(t+1, ans))
