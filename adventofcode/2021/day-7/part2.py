#! /usr/bin/env python3

import math

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

positions = [int(i) for i in fdata.readline().rstrip().split(',')]
print(positions)
max_position = max(positions)

# find best horizontal position to allign others to.
min_sum = math.inf
min_pos = math.inf
for tarpos in range(0, max_position):
    sum = 0
    
    for pos in positions:
        N = abs(pos - tarpos)
        delta = (1 + N) / 2
        sum += N * delta
    
    print(tarpos, sum)

    if sum < min_sum:
        min_sum = sum
        min_pos = tarpos

print(min_sum)
print(min_pos)
