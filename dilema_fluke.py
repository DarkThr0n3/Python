tcases = int(input())

for x in range(0,tcases):
    S = input()
    S = S.strip('0')
    no = S.count('1')

    if no%2 != 0:
        print('WON')
    else:
        print('LOSE')

#Wrong answer lol