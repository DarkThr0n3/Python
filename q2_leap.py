input_year = input()

try:
    year = int(input_year)

    ans =False
    if year%4 ==0:
        if year%100==0:
            if year%400==0:
                ans =True
            else:
                ans = False
        else:
            ans =True
    else:
        ans = False

    l = "Leap" if ans else "Not a Leap"
    print("{} is a {} year".format(year,l))

except:
    print("Input not an integer, pleae enter an integer\n")
