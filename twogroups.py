t = int(input())

for x in range(0,t):
    abc = input().split(' ')

    for y in range(0,len(abc)):
        abc[y] = int(abc[y])

    no1 = abc[0]%2
    no2 = abc[1]%2
    no3 = abc[2]%2 #Either 1 or 2

    flag = 0

    if no1==0 and no2 == 0 and no3==0:
        flag =1
    if no1==1 and no2 == 1 and no3 ==1:
        flag = 1

    




    if flag==1:
        print("YES")
    else:
        print("NO")