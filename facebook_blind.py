

1.

s = "524262"

1 - 26

def my_fn(s):                 "111"

  if not s or len(s)==0:
    return [""]

  ans = []

  if s[0] in dict:
    ans.extend([s[0] + x for x in myfn(s[1:]))    #
                                                            [aaa,ak,ka]
    if s[:2] in dict:
      ans.extend([s[:2]+x for x in myfn(s[2:])])

  return ans
