#using re
import imp
import re as relib

imp.find_module("re")



pattern_in = input("Input pattern")
text_to_search = input("paragraph????")

#Using r' ' raw string for pattern_in
#even in r' ' , we have to escape symbols
pattern = relib.compile(pattern_in)




matches = pattern.finditer(text_to_search)

