for t in range(int(input())):
    no_spots = int(input())
    q = input().split()
    p = None
    for posi,spot in enumerate(q):
        if spot=="1":
            if p!=None and posi-p<6:
                p = -1
                break
            p = posi
    if p==-1:
        print("NO")
    else:
        print("YES")
