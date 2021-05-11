#cut

# cut -d'' -f no filename

import argparse

def arg():
    p = argparse.ArgumentParser()

    p.add_argument('-d',help="delimiter")
    p.add_argument('-f' ,help='Columns to be selected')
    p.add_argument('filename',help="name of file for cut operation")

    return p.parse_args()

pa = arg()


if pa.d:
    deli = pa.d.strip("'")
#else:
#    deli = None

if pa.f:
    field = []
    if "-" in pa.f:
        field_start = int(pa.f[:pa.f.index('-')])
        field_end = int(pa.f[pa.f.index('-')+1 :])
        for f in range(field_start,field_end+1):
            field.append(f)
    else:
        field = [pa.f]

def extract_from_line(line,deli,field):
    cols = line.split(deli)
    str = ""
    for f in field:
        if int(f) <len(cols):
            f= int(f)
            str = str+ cols[f-1]
    print(str)


file = open(pa.filename)


flag = 0
while flag==0:
    rl = file.readline()
    if rl:
        extract_from_line(rl,deli,field)
    else:
        flag = 1
