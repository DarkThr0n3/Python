#sequence

tcases = int(input())

for i in tcases:
    N, K = input().split(' ')
    N = int(N)
    K = int(K)      #Length K sub-sequence

    seqA = input().split(' ')

    no_freq_list = [[0,0] , [1,0] ,[2,0] ,[3,0] , [4,0], [5,0] , [6,0],  [7,0] , [8,0] , [9,0] ]

    for l in range(0,len(seqA)):
        seqA[l] = int(seqA[l])
        no = seqA[l]
        #Update frq list
        ind = no_freq_list[0].index(no)
        a[int][1] +=1


    #choose a real number m in such a way that for each contiguous subsequence of B with length K, the arithmetic average of the elements of this subsequence is m

    #IDea 1 - K lists - and fill one by one - from sorted sequence

    # K subset will repeat, as it is, [   K lenght  ] [   same pattern   ] [   remaining but same pattern]
    # Choose K

    #NO list

