

if __name__ == "__main__":
    fdata = open("input1.txt", 'r')
    # fdata = open("input.txt", 'r')

    # Load data into 2d list
    board = []
    for line in fdata:
        line = line.rstrip()
        board.append([int(i) for i in line])

    print(board)
    size_x = len(board[0])
    size_y = len(board)

    risc = 0

    # Dijkstra
    initial_node = (0, 0)
    target_node = (size_x-1, size_y-1)

    

    # BFS
    opened = []
    closed = []
    opened.append((0, 0))
    while opened:
        top = opened.pop()
        closed.append(top)

        print("current cell:", top[0], top[1], " value: ", board[top[0]][top[1]])

        # Add adjacent fields into opened
        x = top[0]
        y = top[1]
        if y + 1 >= size_y or x + 1 >= size_x:
            break

        if board[x+1][y] > board[x][y+1]:
            if (x, y + 1) not in closed:
                opened.append((x, y + 1))  # Y, X + 1 (right)
            if (x + 1, y) not in closed:
                opened.append((x + 1, y))  # Y + 1, X (down)
        else:
            if (x + 1, y) not in closed:
                opened.append((x + 1, y))  # Y + 1, X (down)
            if (x, y + 1) not in closed:
                opened.append((x, y + 1))  # Y, X + 1 (right)

        if x == size_x - 1 and y == size_y - 1:
            print("Konec nalezen.")
            break


