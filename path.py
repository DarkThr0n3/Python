from pathlib import Path
import argparse


class sanky_class(object):

    def __init__(self, no):
        self.no = no

ag = argparse.ArgumentParser()

ag.add_argument('path',type=str,nargs=1)
ag.add_argument('--type',type=str,nargs = 2)
ag.add_argument('--name',type=str)

final_args = ag.parse_args()

print(final_args)
print(type(final_args))

print("final_args.path[0] is",final_args.path[0])
print("final_args.path is",final_args.path)
print("fina.type is",final_args.type)
print("final_args.type[0] is", final_args.type[0])

mypath = Path(final_args.path[0])
print("my path is",mypath)
print("type of mypath", type(mypath))

for x in mypath.rglob(*name*):
    if x.is_file():
        print("file",x)
    elif x.is_dir():
        print("dir",x)
