# Dilemma of cards

#import psyco
#psyco.full()


def flip(n):
    global cards
    global N
    #removing card by marking it as zero and then stripping
    cards= cards[:n] +'0' + cards[n+1:] #remove card ERRRORRRRRRRRRRRR
    #print("stripping inside function")
    cards = cards.lstrip('0') # -1-000-1- => -0-100-1- => 0001-1- => 0000-0- or -1-000 thi case we win , so lstrip will return ''
    N = len(cards)
    #print(f"N is now {N}")
    if N==0: #We are sure that if this is the case, that all left sorted, we won(i.e. we will be able to remove all cards)
        return True #We won
    else: #Flip
        #if cards[0]=='0':
        #    cards='1' + cards[1:]
        return False

flag = False
tcases = int(input())

for x in range(0,tcases):
    cards = input()
    cards = cards.lstrip('0') #Strip from left - according to our algo
    #cards = cards.split(' ')
    N = len(cards)
    #for no in range(0,N):
    #    cards[no] = int(cards[no])
    #Algo
    # 1. WE can left - if 0 skip, if 1 flip
    no = 0
    while True:

        if N==0:
            break

        if cards[no]=='0':
           no = no+1

        elif cards[no]=='1': #flip it
            flag = flip(no)
            if flag:
                break
            #cards are stripped, so start counting from 0 again for this loop
            no = 0
        #print(cards)
        #print("inside while")
        #print(f"N length is {N} , no is {no}")

        if no==N:
            #print("Reached end of string ----- breaking out of while")
            break

    if flag==True:
        print("WIN")
    elif flag == False:
        print("LOSE")
