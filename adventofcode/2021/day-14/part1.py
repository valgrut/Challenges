#! /usr/sbin/env python3 


# fdata = open("input.txt", 'r')
fdata = open("input1.txt", 'r')


template = fdata.readline().rstrip()

# consume empty line
fdata.readline().rstrip()

# Counter for final result
polymers = {}
# Load polymer translation data
rules = {}
for line in fdata:
    line = line.rstrip()
    
    start, _, end = line.rstrip().replace('>', '-').split('-')
    rules[start.strip()] = end.strip()
    if end.strip() not in polymers:
        polymers[end.strip()] = 0

print(template)
print(polymers)

# Process template
iterations = 10
for it in range(iterations):
    print("Iteration", it)
    new = ""
    for idx in range((len(template) - 1)):
        current = template[idx] + template[idx + 1]
        if idx == 0:
            new += (template[idx] + rules[current] + template[idx + 1])
        else:
            new += (rules[current] + template[idx + 1])

    template = new
    print("Len of current template:", len(template))


for p in template:
    polymers[p] += 1
print("Final polymers:", polymers)

most_common = max(polymers, key=polymers.get)
least_common = min(polymers, key=polymers.get)

print(polymers[most_common] - polymers[least_common])
