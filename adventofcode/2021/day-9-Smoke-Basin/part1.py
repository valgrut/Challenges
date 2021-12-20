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
    # if checkBoundaries(board, x-1, y-1) is False:
        # surrounding.append(int(board[x-1][y-1]))

    if checkBoundaries(board, x-1, y) is False:
        surrounding.append(int(board[x-1][y]))

    # if checkBoundaries(board, x-1, y+1) is False:
        # surrounding.append(int(board[x-1][y+1]))

    if checkBoundaries(board, x, y-1) is False:
        surrounding.append(int(board[x][y-1]))

    if checkBoundaries(board, x, y+1) is False:
        surrounding.append(int(board[x][y+1]))

    # if checkBoundaries(board, x+1, y-1) is False:
        # surrounding.append(int(board[x+1][y-1]))

    if checkBoundaries(board, x+1, y) is False:
        surrounding.append(int(board[x+1][y]))

    # if checkBoundaries(board, x+1, y+1) is False:
        # surrounding.append(int(board[x+1][y+1]))
    
    # print("Surroundings for ", x, y, surrounding)
    return surrounding

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

board = []
for line in fdata:
    board.append(line.rstrip())
print(board)

lowlands = []
for line in range(0, len(board)):
    for col in range(0, len(board[line])):
        # print(line, col)
        if int(board[line][col]) < min(getSurrounding(board, line, col)):
            lowlands.append(int(board[line][col]))

print("lowlands: ", lowlands)

print(sum(lowlands))
result = sum([i+1 for i in lowlands])
print(result)


