import random as rd


'''
Andrew Piatetsky
SoftDev
K05 -- bitstream / Random Picking and creating dictionary with tuples
2022-09-23
time spent: 0.5 hours


DISCO:

Its very easy to read files in python and then manipulate them.
string parsing is super nice and fluid too 


QCC:
Can you store objects in files, like can I save my dictionary to an external file or a tuple for example.
Strings are easy enough to work with but how can we save a list that we were working with 

'''

file_name = "krewes"
with open(file_name, "r") as f: # f = open...
    data = f.read()
    


def parse(text):
    krews_dic = {} # {2:[],7:[],8:[]}
    devo_text = text.split("@@@") #list of strings
    
    for strings in devo_text:
        strings = strings.split('$$$')
        if int(strings[0]) not in krews_dic:
            krews_dic[int(strings[0])] = []
        krews_dic[int(strings[0])].append((strings[1],strings[2]))
    
    return krews_dic


def pick_rand(peeps: dict):
    
    # get random period
    rand_period = rd.choice(list(peeps))

    # get random person from the chosen period
    rand_devo = rd.choice(peeps[rand_period])
     
    return f"{rand_period} : {rand_devo[0]} + {rand_devo[1]}"
    
    

  
krewes = parse(data)
# print(krewes)

print(pick_rand(krewes))


    






