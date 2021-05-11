#grep

#1 skill in coding is time-manegemnt
# To find that simplest things and fundamental thing, which can get you running fast
# identifying the most required thing is the essence
import argparse

#python3.6 grepex.py "pattern" filepath -options

def arguments():
    ag = argparse.ArgumentParser()
    ag.add_argument("pattern",help='pattern',nargs=1)
    ag.add_argument("filename", help='filename',nargs=1)
    return ag.parse_args()

def scan_pattern(pattern, filepath):
    fp = open(filepath)

    flag = 1
    ln=1
    while flag:
        line = fp.readline()
        if not line:
            flag =0
            break

        if match_function(pattern,line):
            print(f"{filepath}:{ln}:{line}")

        ln+=1
    fp.close()

def match_function(pattern,line):
    lp =len(pattern)
    for x in range(0,len(line)):
        if pattern == line[x:x+lp]:
            return True
    return False

args = arguments()
scan_pattern(args.pattern[0] , args.filename[0])
