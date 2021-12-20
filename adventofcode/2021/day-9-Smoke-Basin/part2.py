#! /usr/bin/env python3


def checkBoundaries(board, x, y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]):
        # print("something is out of bound", x, y, len(board), len(board[x]))
        return True
    return False


def getSurrounding(board, x, y):
    """
    return list of surrounding values of value on x,y
    """

    surrounding = []

    if checkBoundaries(board, x-1, y) is False:
        surrounding.append(int(board[x-1][y]))

    if checkBoundaries(board, x, y-1) is False:
        surrounding.append(int(board[x][y-1]))

    if checkBoundaries(board, x, y+1) is False:
        surrounding.append(int(board[x][y+1]))

    if checkBoundaries(board, x+1, y) is False:
        surrounding.append(int(board[x+1][y]))

    return surrounding


def getSurroundingCells(board, x, y):
    """
    return list of surrounding values of value on x,y
    """

    surrounding = []
    if checkBoundaries(board, x-1, y) is False:
        surrounding.append((x-1, y, int(board[x-1][y])))

    if checkBoundaries(board, x, y-1) is False:
        surrounding.append((x, y-1, int(board[x][y-1])))

    if checkBoundaries(board, x, y+1) is False:
        surrounding.append((x, y+1, int(board[x][y+1])))

    if checkBoundaries(board, x+1, y) is False:
        surrounding.append((x+1, y, int(board[x+1][y])))

    return surrounding


fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

# Init board
board = []
for line in fdata:
    board.append(line.rstrip())

# Find lowlands
lowlands = []
for line in range(0, len(board)):
    for col in range(0, len(board[line])):
        if int(board[line][col]) < min(getSurrounding(board, line, col)):
            lowlands.append((line, col, int(board[line][col])))

# print("lowlands:", lowlands)


# BFS
lowland_sizes = []
open = []
closed = []
for lowland in lowlands:
    open.append(lowland)
    lowland_size = 0
    while len(open) > 0:
        current = open.pop(0)
        closed.append(current)

        # get surrounding of current cell
        cur_sur = getSurroundingCells(board, current[0], current[1])
        for sur in cur_sur:
            if sur not in closed and sur not in open and sur[2] != 9:
                open.append(sur)

        lowland_size += 1 

    lowland_sizes.append(lowland_size)


# print("lowland sizes:", lowland_sizes)
lowland_sizes.sort(reverse=True)
# print(lowland_sizes)

print("sum of 3 biggest:", lowland_sizes[0] * lowland_sizes[1] * lowland_sizes[2])

