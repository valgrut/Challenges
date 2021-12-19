#! /usr/sbin/env python3 

import copy


# fdata = open("input.txt", 'r')
fdata = open("input1.txt", 'r')

template = fdata.readline().rstrip()

# consume empty line
fdata.readline().rstrip()

# Counter for final result
polymers = {}
polymer_duplicates = {}

# Load polymer translation data
rules = {}
for line in fdata:
    line = line.rstrip()
    
    start, _, end = line.rstrip().replace('>', '-').split('-')
    rules[start.strip()] = end.strip()
    if end.strip() not in polymers:
        polymers[end.strip()] = 0
        polymer_duplicates[end.strip()] = 0

# print(template)
# print(polymers)

# init counters and duplicate polymers
polymer_counter = {}
for idx in range((len(template) - 1)):
    current = template[idx] + template[idx + 1]
    polymer_counter[current] = 1

# print(polymer_counter)

iterations = 1
for it in range(iterations):
    tmp_counter = {}
    # print()
    print("Iteration", it)
    deep_copy = copy.deepcopy(polymer_counter)
    # print("Deep copy len: ", len(deep_copy))
    for pair in deep_copy:
        tmp = deep_copy[pair]
        
        # print("polymer_counter[pair] is ", pair, polymer_counter[pair])
        new_pair_1 = pair[0] + rules[pair]
        new_pair_2 = rules[pair] + pair[1]
        
        # print("new pairs: ", new_pair_1, new_pair_2)
        
        polymer_duplicates[rules[pair]] += tmp
        
        if new_pair_1 not in polymer_counter:
            polymer_counter[new_pair_1] = 0
        if new_pair_2 not in polymer_counter:
            polymer_counter[new_pair_2] = 0
    
        print("before addition and subb: ", polymer_counter)
        polymer_counter[new_pair_1] += tmp
        polymer_counter[new_pair_2] += tmp
        #print(polymer_counter)
        polymer_counter[pair] -= tmp
        print("after addition and subb: ", polymer_counter)
    
    # print(polymer_counter)
    # print(polymer_duplicates)

# Count polymers
for pair in polymer_counter:
    polymers[pair[0]] += polymer_counter[pair]
    polymers[pair[1]] += polymer_counter[pair]

# Sub duplicate polymers
for p in polymer_duplicates:
    polymers[p] -= polymer_duplicates[p]

print("polymer numbers:", polymers)

most_common = max(polymers, key=polymers.get)
least_common = min(polymers, key=polymers.get)
print(most_common, least_common, polymers[most_common], polymers[least_common])
print(polymers[most_common] - polymers[least_common])


fdata.close()
