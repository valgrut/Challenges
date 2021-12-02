#! /usr/bin/env python3

fdata = open("data.txt", 'r')

horizontal = 0
depth = 0

for line in fdata:
    line = line.rstrip()
    command, value = line.split()

    if command == "forward":
        horizontal += int(value)
    elif command == "up":
        depth -= int(value)
    elif command == "down":
        depth += int(value)

print("Result multiplication: ", horizontal*depth)
