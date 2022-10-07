import random as rd

with open('occupations.csv') as f:
    data = f.read()
    
# print(data)
data = data.split('\n')[1:-2]
occupations = {}

for item in data:
    tmp_list = item.split(',')
    # occupations[float(tmp_list[-1])] = (' ').join(tmp_list[0:-1])
    occupations[(' ').join(tmp_list[0:-1])] = float(tmp_list[-1])

def rolling_sum(dic):
    fin_sum = rd.random() * 99.8
    roll_sum = 0
    
    for key in dic:    
        roll_sum += dic[key]
        if fin_sum < roll_sum:
            return key

test = {}
range_num = 1000
for i in range(range_num):
    cur_occ = rolling_sum(occupations)
    if cur_occ in test:
        test[cur_occ] += 100 * 1/range_num
    else:
        test[cur_occ] = 100 * 1/range_num
    
    
print(test)
total = 0
for key in test:
    total += test[key]
    
print(total)

print(rolling_sum(occupations))