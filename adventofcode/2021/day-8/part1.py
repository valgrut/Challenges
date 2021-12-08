#! /usr/bin/env python3

# fdata = open("input.txt", 'r')
fdata = open("input1.txt", 'r')

split = fdata.readline().rstrip().split('|')
code_left = [i for i in split[0].split()]
code_right = [i for i in split[1].split()]
print(code_left)
print(code_right)




