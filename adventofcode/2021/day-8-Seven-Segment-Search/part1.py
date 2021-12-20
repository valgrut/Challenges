#! /usr/bin/env python3

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

appear = 0
for line in fdata:
    split = line.rstrip().split('|')
    code_left = [i for i in split[0].split()]
    code_right = [i for i in split[1].split()]
    print(code_left)
    print(code_right)
    
    for code in code_right:
        if len(code) == 2:
            print(code, "is", 1)
            appear += 1
        if len(code) == 3:
            print(code, "is", 7)
            appear += 1
        if len(code) == 4:
            print(code, "is", 4)
            appear += 1
        if len(code) == 7:
            print(code, "is", 8)
            appear += 1
    
print(appear)


