import math


def print_seafloor(seafloor):
    for i in range(0, len(seafloor)):
        for j in range(0, len(seafloor[0])):
            print(seafloor[i][j], end='')
        print()
    print()


if __name__ == "__main__":

    # === Example input ===
    fdata = open("input1.txt", 'r')
    
    seafloor = []
    for row, line in enumerate(fdata):
        line = line.rstrip()
        seafloor.append([])
        for col, char in enumerate(line):
            seafloor[row].append(char)

    print("Initial state")
    print_seafloor(seafloor)
    
    steps = 1
    stopped_moving = False
    while stopped_moving is False and steps < 10:
        print(f"After {steps} steps:")
        stopped_moving = True
        # Horizontal cucumber movement
        skip_moved = False
        for row in range(0, len(seafloor)):
            for col in range(0, len(seafloor[0])):
                if skip_moved is True:
                    skip_moved = False
                    continue
                if seafloor[row][col] == '>':
                    if col + 1 < len(seafloor[0]):
                        if seafloor[row][col + 1] == '.':
                            seafloor[row][col + 1] = '>'
                            seafloor[row][col] = '.'
                            skip_moved = True
                            stopped_moving = False
                    else:
                        if seafloor[row][0] == '.':
                            seafloor[row][0] = '>'
                            seafloor[row][col] = '.'
                            stopped_moving = False


        # Vertical cucumber movement
        skip_moved = False
        for col in range(0, len(seafloor[0])):
            for row in range(0, len(seafloor)):
                if skip_moved is True:
                    skip_moved = False
                    continue
                if seafloor[row][col] == 'v':
                    if row + 1 < len(seafloor):
                        if seafloor[row + 1][col] == '.':
                            seafloor[row + 1][col] = 'v'
                            seafloor[row][col] = '.'
                            skip_moved = True
                            stopped_moving = False
                    else:
                        if seafloor[0][col] == '.':
                            seafloor[0][col] = 'v'
                            seafloor[row][col] = '.'
                            stopped_moving = False
    
        print_seafloor(seafloor)
        if stopped_moving is False:
            steps += 1
    
    print(f"Cucumbers stopped moving after {steps} steps")
    
    ### TODO: Problem
    # pokud je jedna na zacatku a jenda na konci, mela by se pohnout pouze ta na zacatku, protoze to je brane, ze konce pole jsou spojene, takze okurky tvori jeden batch, prestoze jsou na prvnim a poslednim poli pole.

