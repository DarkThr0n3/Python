for t in range(int(input())):
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]

    def is_perfect_sq(no):              #O(LogN)
        if no in [0,1,4,9,16]:
            return True

        guess = 1

        while no>guess**2:
            guess = guess**2

        left = guess/2
        right = guess

        mid = int((left+right)/2)

        if(left**2 == no or right**2 == no):
            return True

        while(right>left):
            if mid**2==no:
                return True

            if mid**2>no:
                right = mid
            elif mid**2<no:
                left = mid

            mid = int((left+right)/2)

            if(right-left==1):
                if(left**2 == no or right**2 == no):
                    return True
                else:
                    return False
        return False


    count = 0
    s = 0
    for st in range(len(arr)):
        for end in range(st,len(arr)):
            print("{} {}".format(st,end))
            for i in range(st,end+1):
                s+=arr[i]
                print("sum - {}".format(s))
                if(is_perfect_sq(s)):
                    print("PERFECT SQ")
                    count+=1
                s=0

    print("Case #{}: {}".format(t+1,count))
