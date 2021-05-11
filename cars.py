e = 1000000007
for t in range(int(input())):
    n = int(input())
    cars_price = input().split()
    cars_price = [int(x) for x in cars_price]
    cars_price.sort()

    #We shoudl avoid making 0
    #There is no margin, if we sell one car over other and both remian non zero

    ans = 0
    i=0
    for p in cars_price:
        if p>=i+1:
            ans+=p-i
            i+=1
        if ans>e:
            ans%=e
    print(ans)
