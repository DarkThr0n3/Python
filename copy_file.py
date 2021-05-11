#Code to coopy file

from sys import argv

script , fromm , to = argv

fin = open(fromm)
content = fin.read()
fin.close()

fwr = open(to,'w')
fwr.write(content)
fwr.close()


