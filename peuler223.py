#Lattice points on a circle

import math
import numpy as np

def eq_circle(n,x,y): #Returns 0 if point on circle(shifted origin 0,0) , -1 if inside, +1 if outside
        return np.sign(x**2 + y**2 -x*n -y*n)

def no_of_integral_pts(n):
    """Returns number of integral points lying on the circle"""

    #We will find all int coods in first quadrant, then multiply it by 4
    #We start from top, then navigate like sname criss crossing every cood and counting

    #Note - my estimate in this code is wrong, if for shifted circle we miss integral points after addition, on original circle , there is no mirror in circle
    y= (n / (2**.5)) + n/2
    x= n/2

    count =0
    while x < n/(2**.5) and y > 0:
        if eq_circle(n,x,y)==0: #If point on circle, check intergral or not
            frac_x , x = math.modf(x+ (n/2))
            frac_y , y = math.modf(y+ (n/2))
            if frac_x == 0 and frac_y == 0:
                count = count + 1
            x = x+1
            continue

        elif eq_circle(n,x,y) == 1: #Outside circle
            y = y-1
            continue

        elif eq_circle(n,x,y) == -1: #Inside circle
            x = x+1
            continue

    return count


tcases = input()
tcases = int(tcases)


r=1
while r<=tcases:
    Nandm = input()
    N , m = Nandm.split(' ')
    N = int(N)
    m = int(m)

    #Now we want total no of n(n<N) which are equal to 4m
    #Choose set of n which are capable of holding 4m integral points on circle
    #Centre of circle -----> n/2 , n/2 and radius n/root2

    # Step 1 Filter n
    a

    # Step 2 , find integral coordinates in first quadrant only
    count = 0
    for n in set_n
        if no_of_integral_pts(n) == m
            count = count + 1

    print (count)








    r+=1