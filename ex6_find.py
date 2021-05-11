# find, the very easy command to

# BAsic structure
#find (directory to look in, ex . .. /blah/blh) (-type f or d) (additional args)
#-maxdepth -mindepth no (1 indicates specified directory, and so on)

#additional args
#-name (case sens),
#-iname (case insens),
#-mmin -x +y(mod -less than xmin ago, more than y min ago)
#-mtime (days)
#-size +10M +more than, -less than M mbs (note directory nahi dikhata, only files)
#-print (optional, does same thing, prints)

#Excuting command with those results of find
#-exec command {find result are within {} }  [+ or \;]

#library note from Zed
#When you implement this, try to find libraries that can do the work for you. You’ll definitely want to look at
#the subprocess module and also the glob module. You will definitely want to look at os more carefully
#as well.

#find -name "blah" -type d (-print or -exec)

import argparse

pobject = argparse.ArgumentParser()

pobject.add_argument('-type','--typ', help = '-type f for file, d for dir' )

parsed = pobject.parse_args()

print(parsed)

if parsed.typ:
    if parsed.typ == 'f':
        print('filetype')
    elif parsed.typ =='d':
        print('directory type')
