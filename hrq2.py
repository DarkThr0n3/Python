#SUm of even fibonacci numbers

fibo_ser = [1,2]


def fibo_series(N):
    """Generates fibonacci series with last number less than N"""
    while fibo_ser[-1] <= N:
        fibo_ser.append(fibo_ser[-1] + fibo_ser[-2])

    if fibo_ser[-1] > N:
        fibo_ser.pop(-1)


def sum_even(list):

    sum = 0
    while list:
        no = list.pop(0)
        if no%2==0:
            sum = sum + no
    return (sum)





Test_cases = input()
Test_cases = int(Test_cases)

if Test_cases >= 1 and Test_cases <= 100000:
    n = 1
    while n <= Test_cases:
        N = input()
        N = int(N)
        if N>= 10 and N<=(4* (10**16)):
            fibo_series(N)
            sum = sum_even(fibo_ser)
            print(sum)
            n=n+1
            fibo_ser = [1,2]
        else:
            break
