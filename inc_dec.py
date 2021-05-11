from collections import defaultdict

for t in range(int(input())):
    n = int(input())
    a = input().split()

    if len(a)==1:
        print("YES")
        print(a)
        continue
    if len(a)==2:
        print("NO")
        continue

    dic = defaultdict(int)
    l1 = []
    l2 = []
    flag = False

    for no in a:
        no = int(no)
        dic[no]+=1
        if dic[no]==1:
            l1.append(no)
        elif dic[no]==2:
            l2.append(no)
        elif dic[no]==3:
            flag = True
            break
    if flag:
        print("NO")
        continue

    l1.sort()
    if l2:
        l2.sort(reverse = True)

    if l2:
        if l1[-1]==l2[0]:
            flag = True

    if flag:
        print("NO")
        continue
    else:
        print("YES")

    ans = ""
    for no in l1+l2:
        ans+=" " + str(no)
    print(ans)
