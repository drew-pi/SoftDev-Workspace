# https://codingbat.com/prob/p113152

"""
Given a string, return a new string made of every other char starting with the
first, so "Hello" yields "Hlo".
"""
def string_bits(str):
  s = ""
  for i in range(len(str)):
    if i % 2 == 0:
      s += str[i]
  return s

    

# test cases: do not edit
print(string_bits('Hello')) # 'Hlo'
print(string_bits('Hi')) # 'H'
print(string_bits('Heeololeo')) # 'Hello'

