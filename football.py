#Football

tcases = int(input())

for x in range(0,tcases):

    N = int(input())
    Anz = input()
    Bnz = input()

    A_list = Anz.split(' ')
    B_list = Bnz.split(' ')

    for no in range(0,N):
        A_list[no] = int(A_list[no])
        B_list[no] = int(B_list[no])

    #Output one line, max no of points
    point_list = []

    for no in range(0,N):
        points = (A_list[no] * 20) - (B_list[no] *10)
        if points < 0:
            points =0
        point_list.append(points)

    point_list.sort(reverse=True)
    print(point_list.pop(0))