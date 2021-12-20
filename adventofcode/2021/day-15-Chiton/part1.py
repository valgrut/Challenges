import math


def update_node(x, y, visited=None, distance=None):
    global board
    if visited is not None:
        board[x][y][1] = visited
    if distance is not None:
        board[x][y][2] = distance


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

    size_x = len(board[0])
    size_y = len(board)

    risc = 0

    # Dijkstra
    initial_node = (0, 0)
    target_node = (size_x-1, size_y-1)

    unvisited = []
    for line in board:
        for c in line:
            unvisited.append(c)
    print("unvisited len:", len(unvisited))

    #update_node(initial_node[0], initial_node[1], distance=get_difficulty(initial_node[0], initial_node[1]))
    update_node(initial_node[0], initial_node[1], distance=0)

    # Alg
    current = initial_node

    found = False
    while found is False:
        # print(current)
        x = current[0]
        y = current[1]

        if x == target_node[0] and y == target_node[1]:
            print("Optimal Path found.")
            found = True
            break

        # Neighbour on Right
        if x + 1 < size_x:
            if is_visited(x+1, y) is False:
                new_distance = 0
                tentative_distance = get_distance(x, y) + get_difficulty(x + 1, y)
                if tentative_distance < get_distance(x+1, y):
                    # print("Distance was: ", board[x + 1][y][2], "and now is: ", tentative_distance)
                    board[x+1][y][2] = tentative_distance

        # Neighbour Below
        if y+1 < size_y:
            if is_visited(x, y+1) is False:
                tentative_distance = get_distance(x, y) + get_difficulty(x, y + 1)
                if tentative_distance < get_distance(x, y + 1):
                    # print("Distance was: ", board[x][y + 1][2], "and now is: ", tentative_distance)
                    board[x][y + 1][2] = tentative_distance

        # Mark current node as Visited
        board[x][y][1] = True
        # board[x][y][0] = 'x'

        # Find new current node - with smalest tentative distance from all unvisited notes.
        current = get_node_with_smallest_tentative_distance()
        # print("new current", current)

        # If current is destination, and destination has smallest tentative distance, found.
        if current == target_node:
            print("New smallest tentative distance is same as destination")
            break

    print()
    for line in board:
        for c in line:
            print(c[2], " ", end='')
        print()
    print()

    #TODO: Find and mark path using back loop.
