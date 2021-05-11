#Radiation

#Step 1 - Calculate radiation of each cave
#Step 2 - Sort Ciz and Hiz
#Step 3 - Check equal
#Time limit exceeded

#Changing split in one line, introducing minmax in rangee, eliminating need to calculate all int[Ci} had no impact on time execution bcc!!


#Complexity -


tcases = int(input())

for x in range(0,tcases):
    N = int(input())
    C = input().split(' ')
    H = input().split(' ')

    for no in range(0,N):
   #     C[no] = int(C[no])
        H[no] = int(H[no])            # O(N)

    r_level = [0] *N
  #  r_level = r_level*N #Initially no radiation

    #Step 2 - Count radiation (i-Ci)
    for i in range(0,N):
        rangee = range(max(i-int(C[i]),0),min(i+int(C[i])+1,N))  #Ensures rangee is in cave numbers
        for number in rangee:
            r_level[number] += 1        # O(N^2) 

    #Step 3
    #print("r_level is")
    #print(r_level)
    #print("H is")
    #print(H)
    r_level.sort() # O ( N * logN )
    H.sort()       # O ( N * logN ) - avergae and worst case, best case already sorted, linear O (N)
    if r_level == H:
        print('YES')
    else:
        print('NO')