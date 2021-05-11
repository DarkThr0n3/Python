#Implement cat

#Feature 1 - Printing file
#Feature 2 - multiple files concatenated
#Feature 3  >
#Feature 4 - flags


import argparse

pobject = argparse.ArgumentParser()

pobject.add_argument('filename',nargs='*',help='file name', type=str)
pobject.add_argument('-out','--output',help = 'output file')

argz = pobject.parse_args()


out=""

for i in argz.filename:
    fopen = open(i)
    outfile = fopen.read()
    out = out + outfile
    fopen.close()

if argz.output:
    target = open('{}'.format(argz.output), 'w')
    target.write(out)
    target.close()
else:
    print(out)
