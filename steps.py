for _ in range(int(input())):
    n_k = input().split()
    k = int(n_k[1])
    aans = ""
    nz = input().split()

    for n in nz:
        a = '1' if int(n)%k==0 else '0'
        ans+= a
    print(ans)
