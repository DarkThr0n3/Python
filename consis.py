#consistent or not

def start_minus():
    """y=0 is -1"""
    y=0
    while A[y] == -1:
        y++
    no = A[y]

    myno = no
    while y!=0:
        if S[y-1] == '=':
            myno = no
        if S[y-1] == '<':
            myno = no-1
        if S[y-1] == '>'
            myno = no +1

        if myno < 0:
            return False
        no = myno
        y-=1
    return True




t = int(input())

for x in range(0,t):
    N = int(input())
    A = input()
    A = A.split(' ')

    lenA= len(A)
    y=0
    for y in range(0,lenA):
        A[y] = int(A[y])

    S = input()

    flag = 0
    for y in range(0,lenA):
        if A[y] == -1 and y==0:
            start_res = start_minus():
            if start_res:






