#! /usr/sbin/env python3 

import copy


fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

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

print(template)
print("Initial polymers", polymers)

# init counters and duplicate polymers
polymer_counter = {}
for idx in range((len(template) - 1)):
    current = template[idx] + template[idx + 1]
    if current not in polymer_counter:
        polymer_counter[current] = 1
    else:
        polymer_counter[current] += 1

    # Additional duplicate is needed to account while initial
    # template is parsed, since it is parsed by 2 polymers,
    # so there is duplication while initiating polymer counter.
    # i.e. NNBC -> NN, NB, BC, where N and B are duplicated.
    if idx < len(template) - 2:
        polymer_duplicates[template[idx + 1]] += 1

print("Initial polymer counters", polymer_counter, len(polymer_counter))
print("Initial polymer duplications", polymer_duplicates)

iterations = 40
for it in range(iterations):
    tmp_counter = {}

    # We don't want to update list under our hands.
    deep_copy = copy.deepcopy(polymer_counter)

    for pair in deep_copy:
        tmp = deep_copy[pair]

        new_pair_1 = pair[0] + rules[pair]
        new_pair_2 = rules[pair] + pair[1]

        # Add as many duplicates as number of same pair
        # i.e. (number of 'CD' = 8, rule: CD->H => add 8 duplicates of H)
        polymer_duplicates[rules[pair]] += tmp
        
        if new_pair_1 not in polymer_counter:
            polymer_counter[new_pair_1] = 0
        if new_pair_2 not in polymer_counter:
            polymer_counter[new_pair_2] = 0
    
        polymer_counter[new_pair_1] += tmp
        polymer_counter[new_pair_2] += tmp
        polymer_counter[pair] -= tmp


# Count polymers
for pair in polymer_counter:
    polymers[pair[0]] += polymer_counter[pair]
    polymers[pair[1]] += polymer_counter[pair]

# Sub duplicate polymers
for p in polymer_duplicates:
    polymers[p] -= polymer_duplicates[p]

# Find least and most common values
most_common = max(polymers, key=polymers.get)
least_common = min(polymers, key=polymers.get)
print(polymers[most_common] - polymers[least_common])

fdata.close()
