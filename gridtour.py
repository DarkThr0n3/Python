#Grid Tour

#Sub_task 1
tcases = int(input())

t=1
while t<= tcases:
    nmk = input()
    N, M, K = nmk.split(' ')
    N = int(N)
    M = int(M)
    K = int(K)

    #K=1 and 2, subtask 1
    if K=1:
        ans = M*N
    elif K=2:
        if M%2==0 or N%2==0: #Both are even, tour not possible
            ans= -1
        else: #One is odd, therefore, find shortest








    t=t+1