
for t in range(int(input())):
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    arr = input().split()
    count = 0

    def check(ind):
        if ind + k-1 <= len(arr)-1:
            for no in range(k,0,-1):
                if no!=int(arr[ind]):
                    return 0
                ind+=1
            return 1
        else:
            return 0


    for i,no in enumerate(arr):
        if int(no)==k and i + k-1 <= len(arr)-1:
            count+=check(i)
    print("Case #{}: {}".format(t+1,count))
