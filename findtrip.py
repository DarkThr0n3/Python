tcases = int(input())

for i in range(0,tcases):
    NK = input().split(' ')
    days , places = int(NK[0]), int(NK[1])

    seq = input().split(' ')

    for l in range(0,days):
        seq[l] = int(seq[l])

    #Subtask 1, k=2, and N < 1000
    def swap(no):
        if no==1:
            return 2
        if no==2:
            return 1:


    def searchr(no): #right men kitne vacant
        l = no
        count = 0
        while seq(l) == -1:
            l+=1
            count +=1

        return count-1


    for l,no in seq, range(0,N):
        if l==-1:
            #Starting case
            if no==0:
                #Both -1





