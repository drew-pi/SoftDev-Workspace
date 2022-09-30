import random as rd

with open('occupations.csv') as f:
    data = f.read()
    
# print(data)
data = data.split('\n')[1:-2]
occupations = {}

for item in data:
    tmp_list = item.split(',')
    occupations[float(tmp_list[-1])] = (' ').join(tmp_list[0:-1])


def rolling_sum(dic):
    fin_sum = rd.random() * 99.8
    roll_sum = 0
    
    for chance in dic:    
        roll_sum += chance
        
        if fin_sum < roll_sum:
            return dic[chance]
        

test = {}
for i in range(1000):
    cur_occ = rolling_sum(occupations)
    if cur_occ in test:
        test[cur_occ] += 1
    else:
        test[cur_occ] = 1
    
    
print(test)
total = 0
for key in test:
    total += test[key]
    
print(total)