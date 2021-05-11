import argparse
from sys import argv

pobject = argparse.ArgumentParser()

#ORDER MATTERS !!!!!!!!!!!

pobject.add_argument('--square' ,help='echoes the string u use here') #Order matters, but not between optional/flagged and (int types)
pobject.add_argument('--no',help="Enter no to be squared",type=int) #if type not specified, theya re stringss
pobject.add_argument('v',help="To check version number",type=int) #default=0(even not for int type),choices=[1,2,3]
pobject.add_argument('--no2',type=int,help='This is no2')
# dd_argument('--arg')  double- indicates optional and onemore
#1. Takes one more argument,2. indicates optional argument (Otherwise takes None)

pobject.add_argument('-f','--flag',help='Flag', action='store_true')
#It cannot accept valu. If specified, p.flag is True else False.
#Short version pobject.add_argument('-f','--flag',action='store_true') #action='count' can also be


p = pobject.parse_args()
if p.square:
    print(p.square*2)

if p.no:
    print((p.no)**2)

if p.v:
    print("Version"+str(p.v))

if p.no2:
    print(f"no 2 is {p.no2}")
if p.flag:
    print("flag is on")
