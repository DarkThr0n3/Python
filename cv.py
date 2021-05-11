#S string len N
#i consonant and i+1  voewel

tcases = int(input())

t=1
while t<=tcases:
    N = int(input())
    S = input()

    count =0
    no = 0

    if N==1:
        count=0
    elif N>1:
          while no != N-1:
                if S[no] != 'a' and S[no]!='e' and S[no]!='i' and S[no]!='o' and S[no] !='u':
                    if S[no+1] == 'a' or S[no+1] == 'e' or S[no+1]=='i' or S[no+1]=='o' or S[no+1] =='u':
                        count = count + 1
                no = no+1

    print(count)
    t+=1