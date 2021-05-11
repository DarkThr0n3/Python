
tcases = int(input())

for x in range(tcases):
    #x starts fro 0 till tcases-1
    N = int(input())
    S = input() #len N --- SOlutions
    U = input() #len N 'N' if not answered the q, otherwise ans

    score = 0
    i=0
    while i<= N-1:
        if U[i] == 'N': #not answered see next one
            i+=1
            continue
        elif U[i] == S[i]: #correct answer
            score +=1
            i+=1
            continue
        elif U[i] != S[i]: #incorrect, skip next question
            i+=2

    print(score)


