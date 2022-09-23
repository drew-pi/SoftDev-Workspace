

def sleep_in(weekday, vacation):
  return (not weekday or vacation)

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(a, b):
  if(a == b):
    return 2 * (a + b)
  return (a + b)

def diff21(n):
  if(n <= 21):
    return 21 - n
  return 2 * (n - 21)

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

def near_hundred(n):
  return (90 <= n and n <= 110) or (190 <= n and n <= 210)

def pos_neg(a, b, negative):
  if(negative):
    return (a < 0 and b < 0)
  return ( (a < 0 and b > 0) or (a > 0 and b < 0))

def not_string(str):
  if len(str) >= 3:
    if "not"not in str[:3]:
      return "not " + str
    return str
  return "not " + str

def missing_char(str, n):
  return str[:n] + str[1+n:]
    
def front_back(str):
  if(len(str) <= 1):
    return str
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

def front3(str):
  if len(str) >= 3:
    return 3*str[:3]
  return 3*str

