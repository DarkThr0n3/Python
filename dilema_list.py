#Dilema2
#import psyco
#psyco.full()

#Time limit exceeded error
#i think i have to check working of string[:] rane function, len function

def flip(n):
    global cards
    global N

    #removing card by marking it as zero and then stripping
    cards= cards[n+1:] #remove card ERRRORRRRRRRRRRRR

    N = len(cards)
    if N==0:            #This case 0001 this last one
        return True
    else:
    #cards are remaining
    #Turn next 1 into 0  (N number of total cards left)
        noz=0
        while True:
            if cards[noz] == '1':
                cards = '0'+cards[noz+1:]
                N = len(cards) #new length of cards
                return False
            else:
                noz = noz+1
            if noz==N: #All trailing were zeros, awesome
                return True #


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