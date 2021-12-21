import math
import copy

def get_difficulty(x, y):
    global board
    return board[x][y][0]


def is_visited(x, y):
    global board
    return board[x][y][1]


def get_distance(x, y):
    global board
    return board[x][y][2]


def get_node_with_smallest_tentative_distance():
    global board

    # unvisited = [(line, cell) for line in board for cell in line if is_visited(line, cell) is False]
    minimal = math.inf
    current_min_cell = (0, 0)
    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            if board[x][y][1] is False:
                if board[x][y][2] < minimal:
                    minimal = board[x][y][2]
                    current_min_cell = (x, y)

    return current_min_cell
    # return min(unvisited, key=lambda x:x[2])[:]


def increase_difficulty(cave, increase_level):
    new_board = cave
    for x, line in enumerate(new_board):
        for y, cell in enumerate(line):
            new_board[x][y][0] += increase_level
            if new_board[x][y][0] > 9:
                new_board[x][y][0] = new_board[x][y][0] - 9
    return new_board


if __name__ == "__main__":
    # fdata = open("input1.txt", 'r')
    fdata = open("input.txt", 'r')

    # Load data into 2d list
    board = []
    visited = False
    tentative_initial_value = math.inf
    for line in fdata:
        line = line.rstrip()
        board.append([[int(i), visited, tentative_initial_value] for i in line])

    # Multiply it 5 times with increasing risc level.
    final_board = []
    for y_cnt in range(0, 5):
        board_line_base = []
        for x_cnt in range(0, 5):
            if board_line_base == []:
                board_line_base = increase_difficulty(copy.deepcopy(board), x_cnt + y_cnt)
            else:
                new_right_board = increase_difficulty(copy.deepcopy(board), x_cnt + y_cnt)
                # append it to the right
                for l, line in enumerate(board_line_base):
                    board_line_base[l] += new_right_board[l]

        final_board += board_line_base

    # Override small board with new Big cave board
    board = final_board
    # print board
    # print()
    # for line in final_board:
    #     for c in line:
    #         print(c[0], " ", end='')
    #     print()
    # print()

    size_x = len(board)
    size_y = len(board[0])
    # print(size_x, size_y)

    # Dijkstra
    initial_node = (0, 0)
    target_node = (size_x-1, size_y-1)

    # Initial position is considered unvisited, so init as 0.
    board[initial_node[0]][initial_node[1]][2] = 0

    current = initial_node

    found = False
    while found is False:
        x = current[0]
        y = current[1]

        if x == target_node[0] and y == target_node[1]:
            print("Optimal Path found.")
            found = True
            break

        # TODO: Heuristika 1: Jdi prvne tou kratsi cestou z obou sousedu.
        # Neighbour on Right
        if x + 1 < size_x:
            if is_visited(x+1, y) is False:
                new_distance = 0
                tentative_distance = get_distance(x, y) + get_difficulty(x + 1, y)
                if tentative_distance < get_distance(x+1, y):
                    board[x+1][y][2] = tentative_distance
        # Left
        if x - 1 >= 0:
            if is_visited(x-1, y) is False:
                new_distance = 0
                tentative_distance = get_distance(x, y) + get_difficulty(x - 1, y)
                if tentative_distance < get_distance(x-1, y):
                    board[x-1][y][2] = tentative_distance

        # Neighbour Below
        if y+1 < size_y:
            if is_visited(x, y+1) is False:
                tentative_distance = get_distance(x, y) + get_difficulty(x, y + 1)
                if tentative_distance < get_distance(x, y + 1):
                    board[x][y + 1][2] = tentative_distance

        # Up
        if y - 1 >= 0:
            if is_visited(x, y - 1) is False:
                tentative_distance = get_distance(x, y) + get_difficulty(x, y - 1)
                if tentative_distance < get_distance(x, y - 1):
                    board[x][y - 1][2] = tentative_distance

        # Mark current node as Visited
        board[x][y][1] = True

        # Find new current node - with smalest tentative distance from all unvisited notes.
        current = get_node_with_smallest_tentative_distance()

        # If current is destination, and destination has smallest tentative distance, found.
        if current == target_node:
            print("New smallest tentative distance is same as destination")
            break

    # Draw board with distance values
    print()
    for line in board:
        for c in line:
            print(c[2], " ", end='')
        print()
    print()

    print("Lowest total risk of path is", board[size_x-1][size_y-1][2])

    # TODO: Find and mark path using reverse iteration.
