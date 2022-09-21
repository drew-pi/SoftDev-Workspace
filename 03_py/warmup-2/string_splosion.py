# https://codingbat.com/prob/p118366

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
  s = ""
  for i in range(len(str) + 1):
    s += str[:i]
  return s

    

# test cases: do not edit
print(string_splosion('Code')) # 'CCoCodCode'
print(string_splosion('abc')) # 'aababc'
print(string_splosion('ab')) # 'aab'

