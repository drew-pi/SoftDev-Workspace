# https://codingbat.com/prob/p145834

"""
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
yields 1 (we won't count the end substring).
"""
def last2(str):
  c = 0
  if (len(str) > 2):
    sub = str[len(str)-2:]
    str = str[:len(str)-1]
    for i in range(len(str)):
      if (str[i:i+2] == sub):
        c += 1
  return c

    

# test cases: do not edit
print(last2('hixxhi')) # 1
print(last2('xaxxaxaxx')) # 1
print(last2('axxxaaxx')) # 2

