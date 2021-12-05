#! /usr/bin/env python3


def draw_line(array, p_start, p_end):
    if p_start[0] == p_end[0]:
        for x in range(min(p_start[1], p_end[1]), max(p_start[1], p_end[1])+1):
            array[x][p_start[0]] += 1

    if p_start[1] == p_end[1]:
        for y in range(min(p_start[0], p_end[0]), max(p_start[0], p_end[0])+1):
            array[p_start[1]][y] += 1

def count_intersections(array):
    intersections = 0
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] > 1:
                intersections += 1
    return intersections


###################################################################
fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

size = 1000
board = [[0 for i in range(0, size)] for i in range(0, size)]

# Read data, parse them and draw vents into board
for line in fdata:
    start, _, end = line.rstrip().replace('>', '-').split('-')
    start_p = [int(start.split(',')[0]), int(start.split(',')[1])]
    end_p = [int(end.split(',')[0]), int(end.split(',')[1])]

    # Draw vents into array
    # print(start_p, end_p)
    draw_line(board, start_p, end_p)

# Draw board with vents
for line in board:
    print(line)

print("intersections: ", count_intersections(board))

fdata.close()
