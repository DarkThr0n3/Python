#CERSOL

#test cases t
#n soldiers m links k clasees
# u ---> v

#Atleats one sparrow in each class
#Minimum sparrow????

#Things i learnt
# 1. Careful while deleting list repeatedly, i had to use recursive function to get it done, after deletion, take care of index
# 2. use diff name for ariable and function in a class, obviously
# 3. anything without self in object is not accesible
# 4. Using key of object to sort ----> list.sort(key=lambda soldier: soldier.count )


def calc_solcount_on_list():

    for x in list_of_links:
        lu = x[0]
        lv = x[1]
        # Increse count of lu and lv numbered soldier
        ranklu = sol_class_list[lu - 1]
        ranklv = sol_class_list[lv - 1]

        #print(lu,"---->",lv)
        #print("rank u and v",ranklu,ranklv) #Rank lu and lv are prnting correctly!!
        iii = 0
        while list_of_ranks[ranklu][iii].no != lu:
            #print("iii no = ",iii)
            iii += 1

        #print("Changing",ranklu,iii,"on rank list")
        list_of_ranks[ranklu][iii].countt()

        iii = 0
        while list_of_ranks[ranklv][iii].no != lv:
            #print("iii no = ", iii)
            iii += 1

        #print("Changing", ranklv, iii, "on rank list")
        list_of_ranks[ranklv][iii].countt()



def sort_sol():

    for x,list in list_of_ranks.items():
        list.sort(key=lambda soldier: soldier.count )

def refresh_count():

    for x,list in list_of_ranks.items():
        for sol in list:
            sol.count=0

def rem_sol_n(no):
    i=0
    for x in list_of_links:
        if x[0]==no or x[1] == no:
            del list_of_links[i]
            rem_sol_n(no)
            continue
        i+=1

class soldier():


    def __init__(self,no):
        self.no = no
        self.count = 0

    def countt(self):
        self.count = self.count + 1

    def refresh_count(self):
        self.count = 0

    def give_count(self):
        return self.count


test_cases = int(input())


n=1

while n <= test_cases:

    nmk = input()
    nmklist = nmk.split(' ')
    n = int(nmklist[0]) # Soldiers
    m = int(nmklist[1]) # Links
    k = int(nmklist[2]) # Classes

    #Next input tells. soldier class relation

    sol_class = input()
    sol_class_list =  sol_class.split(' ')

    nn=0
    while nn<n:
        sol_class_list[nn]=int(sol_class_list[nn])
        nn+=1

    #I create a list of classes, where each value is itself list of soldiers, sorted in their count
    list_of_ranks = {}
    ff=1                  #k ranks, therefore k list of ranks----ex 1st item is list of rank 1, 2nd is list of rank 2 soldiers, 3rd is list of rank 3 soldiers
    while ff<=k:
        list_of_ranks[ff]=[]
        ff=ff+1

    nn=0
    while nn<n:
        rank = sol_class_list[nn]
        list_of_ranks[rank].append(soldier(nn+1))   #Assigning soldiers to their rank list
        nn+=1

    #Soldiers now distributed to their respected rank groups (because we need atleast one sparrow in every rank)


    list_of_links = []

    l=1
    while l<=m:
        link = input( )
        lu,lv = link.split(' ')
        luv = (int(lu),int(lv))
        list_of_links.append(luv)
        l=l+1


    list_of_links.sort(key=lambda x:x[0])

        #Atleast one sparrow with each class
    flag = []
    for i in range(0,k):
        flag.append(0)

    #Till this point
    #We have list of soldiers in a dictionary key(rank) -->List of soldiers
    #We have list of links
    #Flags all should be one or else not possible(Couldnt assign atleast one sparrow with each class)

    sparrow=0


    while 1:
        #Functions ------V
        #calc_sol_count_on_list() ----> assigns count to each soldier
        #sort_sol()               ----> sorts every list in listofrank acc to soldier count
        #refresh_count()          ----> sets count to 0 for each soldier
        #rem_sol_n()              ----> remove soldier no n from links


        for rank,list_of_sol in list_of_ranks.items():
            calc_solcount_on_list()
            sort_sol()


            if list_of_sol:         #is there any soldier in rank = rank ????

                soldier = list_of_sol.pop() #HIghest count soldier


                if soldier.count:       #If non zero count
                    sparrow += 1
                    rem_sol_n(soldier.no)
                    flag[rank-1] = 1

                elif soldier.count ==0: #Soldier not in link anyways, this soldier is already popper btw line 139
                        pass

            elif not list_of_sol:
                if flag[rank-1] == 0:
                    sparrow = -1
                    break
                continue

            refresh_count()

        if sparrow==-1:
            break

        if not list_of_links:
            break

    if sparrow >= 1:
        for x in flag:
            if x==0:
                sparrow+=1
    print(sparrow)




    n+=1


