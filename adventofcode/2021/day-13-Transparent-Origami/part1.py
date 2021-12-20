import re

def drawboard():
    board = [['.' for i in range(0, size_x)] for j in range(0, size_y)]

    for point in points:
        board[point[1]][point[0]] = '#'

    for y in range(0, size_y):
        for x in range(0, size_x):
            print(board[y][x], end='')
        print()
    print()



# fdata = open("input1.txt", 'r')
fdata = open("input.txt", 'r')

points = []
folds = []
coords = True
for line in fdata:
    line = line.rstrip()
    if line == "":
        coords = False
        continue

    if coords == True:
        splitted = line.split(',')
        points.append([int(splitted[0]), int(splitted[1])])
    else:
        # print(line)
        m = re.search('.*((x|y)=[0-9]+)', line)
        splitted = m.group(1).split('=')
        folds.append([splitted[0], int(splitted[1])])

# print(points)
# print(folds)

# Vertical fold (right to left): x = ?
# Horizontal fold (down to up): y = ?

# Find board size - find first X fold line and first Y fold line, and calc. size
first_y = folds[0][1] if folds[0][0] == 'y' else folds[1][1]
first_x = folds[0][1] if folds[0][0] == 'x' else folds[1][1]
size_y = (first_y * 2) + 1
size_x = (first_x * 2) + 1

drawboard()

for fold in folds:
    for point in points:
        # Horizontal fold
        if fold[0] == 'y':
            if point[1] > fold[1]:
                point[1] = abs(point[1] - size_y + 1)
        
        # Vertical fold
        if fold[0] == 'x':
            if point[0] > fold[1]:
                point[0] = abs(point[0] - size_x + 1)
 
    # Fold a board space
    if fold[0] == 'y':
        size_y = size_y // 2
    else:
        size_x = size_x // 2

    drawboard()
    # break  # Uncomment for part1: count number of '#' after just FIRST fold.

# Count visible '#'
board = [['.' for i in range(0, size_x)] for j in range(0, size_y)]

for point in points:
    board[point[1]][point[0]] = '#'

dots_counter = 0
for y in range(0, size_y):
    for x in range(0, size_x):
        if board[y][x] == '#':
            dots_counter += 1
print("Visible dots:", dots_counter)
