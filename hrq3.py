#Finding largest prime number

import math

def check_prime(no):
    """Returns TRUE if number is prime"""
    n = 2
    while n<no:
        if no%n == 0:
            return False
        n+=1
    if n==no:
        return True

tcases = input()
tcases = int(tcases)
n=1

while n <= tcases:
    N = input()
    N = int(N)
    #Find largest prime factor

    largest_prime = N


    no = 3
    while no <= N/2: #Consider only odd divisors
        if N%no == 0:               #Is a factor????
            if check_prime(no):    #Is a prime???
                largest_prime = no

        no += 2


    print(largest_prime)


    n=n+1
