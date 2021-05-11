from heapq import heappop, heappush, heapify


for t in range(int(input())):
    nk = input().split()
    n,k = int(nk[0]),int(nk[1])

    N = input().split()
    N = [int(x) for x in N]

    print("Starting program.....")


    heap = []
    heapify(heap)
    print("made heap")

    for i in range(n-1):
        a = N[i+1]-N[i]
        heappush(heap, -1* int(a))


    print("Heap is {}")
    for i in heap:
        print(i)
    print("########")

    print("Starting algo")
    flag = 0
    for k_i in range(k):
        if not heap:
            print("Case #{}: {}".format( t+1,1))
            flag=1
            break

        print("k_i {}".format(k_i))
        element = heappop(heap)
        print("heappop {}".format(element))
        if element== -2:
            pass
        elif element==-1 or 0:
            print("Case #{}: {}".format( t+1,1))
            flag=1
            break
        elif element%2==0:
            a = int(element/2)
            heappush(heap, int(a))
            heappush(heap, int(a))
        elif element%2!=0:
            if element==-3:
                heappush(heap, int(-2))
                continue
            else:
                a = int(element+1) /2
                heappush(heap, int(a))
                heappush(heap, int(a+1))

        print("Heap after operation")
        for i in heap:
            print(i)
        print("########")

    print("Algo finished")


    print("Heap after algo is".format(k_i))
    print("Heap after operation")
    for i in heap:
        print(i)
    print("########")

    if flag:
        continue

    ans = heappop(heap) * -1
    print("Case #{}: {}".format( t+1,ans))
