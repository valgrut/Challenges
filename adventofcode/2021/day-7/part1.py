#! /usr/bin/env python3

import math

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

positions = [int(i) for i in fdata.readline().rstrip().split(',')]
print(positions)

# find best horizontal position to allign others to.
min_sum = math.inf
min_pos = math.inf
for pos in positions:
    sum = 0
    
    for ipos in positions:
        sum += abs(pos - ipos)

    if sum < min_sum:
        min_sum = sum
        min_pos = pos

print(min_sum)
print(min_pos)
