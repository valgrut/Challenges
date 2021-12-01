#! /usr/bin/env python3


fdata = open('data.txt', 'r')
win_size = 3  # size of sliding window
data = [0 for i in range(0, win_size)]
inc_cnt = 0

first = 0
second = 0

i = 0
for line in fdata:

    line = int(line.rstrip())
    data[i%win_size] = line

    if i < 2:
        i += 1
        continue
    
    sliding_sum = sum(data)
    
    # Shift sum values
    first = second
    second = sliding_sum
    
    # shift first value for comparison
    if first == 0 or second == 0:
        print(f"{sliding_sum}: - N/A no previous sum")
        i += 1
        continue

    if first < second:
        inc_cnt += 1
        print(f"{sliding_sum}: increasing")
    elif first == second:
        print(f"{sliding_sum}: same")
    else:
        print(f"{sliding_sum}: decreasing")


    i += 1

print(f"Increment count: {inc_cnt}")
fdata.close()
