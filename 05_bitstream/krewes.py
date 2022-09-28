import random

file_name = "krewes"
with open(file_name, "r") as f: # f = open...
    data = f.read()
    


def parse(text):
    devo_text = text.split("@@@")
    
    devo_tuples = []
    periods = []
    
    for st in devo_text:
        devo = st.split('$$$')
        if devo[0] 
        devo_tuples.append((devo[0],devo[1],devo[2]))
    
    
    


parse(data)
    






