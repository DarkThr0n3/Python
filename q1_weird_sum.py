s = list(input().lower())

summ=0
for char in s:
  summ+= ord(char)-ord('a')+1

single_sum = 0
for no in str(summ):
  single_sum += int(no)

print(chr(single_sum+ord('a')-1))
