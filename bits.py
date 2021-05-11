from collections import defaultdict

for t in range(int(input())):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    nos = input().split()

    if k==0:
        print(0)
        continue

    bit_count = defaultdict(int)
    maxi = 0

    for no in nos:
        binary_string = bin(int(no))
        if len(binary_string)-2>maxi:
            maxi=len(binary_string)-2
        for i in range(len(binary_string)-2):
            if binary_string[-1-i]=="1":
                bit_count[i]+=1

    ansl = []
    for i in range(maxi):
        ansl.append(bit_count[i]*(2**i))

    # print("Bit count --> ")
    # print(bit_count)
    # print("List --> ")
    # print(ansl)

    x = 0
    while k!=0:
        k-=1
        max_ans = ansl[0]
        ind = 0
        for i in range(len(ansl)):
            if ansl[i]>max_ans:
                max_ans = ansl[i]
                ind = i
        x+= 2**ind
        ansl[ind]=0
    print(x)
