#Apples

tcases = int(input())

for x in range(0,tcases):
    N_K = input()
    N_K = N_K.split(' ')
    N = int(N_K[0])     # K*Q = N apples
    K = int(N_K[1])     # K labelled boxes, in order

    #output 'YES' diffrerent distribution, 'NO' same distribution
    # Candidates 1 - Q, apples in each box
    Q = N/K

    #Candidate 2 - Fills each box with K apples (minimum) - (Total chances - Q chances)

    remainder = N%(K*K)

    if remainder == 0:
        times_filled = Q/K
        #(Candidate 1) Check Q = K*times filled (Candidate 2)

        different = False
    else: #Reh gye kuch
        different = True

    if K==1:
        different = False

    if different:
        print('YES')
    else:
        print('NO')