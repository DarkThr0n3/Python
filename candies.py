for t in range(int(input())):
    nmxy = input().split()
    r,c,x,y = int(nmxy[0]),int(nmxy[1]),int(nmxy[2]),int(nmxy[3])

    if y==0 or x==0 or r==0 or c==0:
        print("0")
        continue
    if y>=2*x:
        ans = x*r*c
        print(ans)
        continue
    if x>y:
        x = y

    big = max(x,y-x)
    small = min(x,y-x)

    ans = 0
    if c%2==0:
        ans =int((big+small)*(c//2)*r)
    else:
        r1 = int((big+small)*(c//2) + big)
        r2 = int((big+small)*(c//2) + small)
        #print("r1 is {}".format(r1))
        #print("r2 is {}".format(r2))
        ans= 0
        ans+=int((r//2)*r1)
        ans+=int((r//2)*r2)
        a = r1 if r%2==1 else 0
        ans+=a
    print(ans)
