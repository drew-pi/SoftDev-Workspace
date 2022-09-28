import random as rd
'''
Andrew Piatetsky
SoftDev
K04 -- krewes / Random Picking
2022-09-23
time spent: 0.5 hours
'''

'''
DISCO:
there is a random module in python, there are many functions/methods that come with
that library 

dictionaries are iterable, but they are not sequences because you can't refer to the
keys as indeces, they are hashes

QCC:
How does random work? we think it refernces the time or mouse movement perhaps?

Do we have to change the devos into actual names later?
RESOLVED


OPS SUMMARY:

Our code first picks a random key from a list of the available keys and then we pick a random person
from the list value associated with the key, then it returns that random person and the period 

'''





krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "KAREN"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "WANYING"]
         }


def pick_rand(peeps: dict):
    
    # get random period
    rand_period = rd.choice(list(peeps))

    # get random person from the chosen period
    rand_devo = rd.choice(peeps[rand_period])
     
    return f"{rand_period} : {rand_devo}"
    
    

print (pick_rand(krewes))



