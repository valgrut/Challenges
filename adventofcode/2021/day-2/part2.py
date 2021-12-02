#! /usr/bin/env python3

fdata = open("data.txt", 'r')

horizontal = 0
depth = 0
aim = 0

for line in fdata:
    line = line.rstrip()
    command, value = line.split()
    value = int(value)
    
    if command == "forward":
        horizontal += value
        depth += aim * value
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value

print("Result multiplication: ", horizontal*depth)
