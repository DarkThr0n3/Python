class Solution:
    def longestLine(self, M: List[List[int]]) -> int:

        if not M:
            return 0

        maxx = float('-inf')

        #Horizontal & Vertical
        for handv in [M,zip(*M)]:
            for line in handv:
                count=0
                flag = 0
                for no in line:
                    if no==1:
                        if flag == 0:
                            flag = 1
                            count = 1
                        elif flag == 1:
                            count+=1
                    elif flag == 1:
                        flag = 0
                        maxx = max(count,maxx)
                        count = 0
                maxx = max(count,maxx)
                HaHa
Ha HaHaHaHa
Ha HaHa

321-1234-213217
213-23-12-213
123.12323.213.

        M2 = [list(reversed(x)) for x in M]
        d=1
        for diag in [M,M2]:
            vivisited = set()
            print("Diag {}".format(d))
            d+=1
            for i in range(len(diag)):
                for j in range(len(diag[0])):
                    print("Checking i j {} {}".format(i,j))
                    if diag[i][j]==1 and (i,j) not in visited:
                        print("i {} j {}".format(i,j))
                        visited.add((i,j))
                        count = 1
                        while i+1<len(diag) and j+1<len(diag[0]) and diag[i+1][j+1]==1:
                            i+=1
                            j+=1
                            visited.add((i,j))
                            count+=1
                        print("{}\n".format(count))
                        maxx = max(count,maxx)


        return maxx
