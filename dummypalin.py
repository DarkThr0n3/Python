#Dummy palindrome
tcases = int(input())

t=1
while t<=tcases:
    string = input()
    list_of_string = sorted(string)

    if len(list_of_string)%2==0:   #even ---exactly two chars are left without pair
        pair = 0
        while list_of_string:
            a_pop = list_of_string.pop(-1)
            pair = pair+1
            if list_of_string:
                b_pop = list_of_string.pop(-1)
            else:
                break
            if a_pop==b_pop:
                pair = pair-1
            else:
                list_of_string.append(b_pop)

        if pair == 2:
            flag = True
        else:
            flag = False

    else:                           #odd ---either 1 or 3 chars without pair
        pair = 0
        while list_of_string:
            a_pop = list_of_string.pop(-1)
            pair = pair+1
            if list_of_string:
                b_pop = list_of_string.pop(-1)
            else:
                break
            if a_pop==b_pop:
                pair = pair-1
            else:
                list_of_string.append(b_pop)

        if pair==1 or pair==3:
            flag = True
        else:
            flag = False

    if flag == True:
        print('DPS')
    elif flag == False:
        print('!DPS')



    t=t+1