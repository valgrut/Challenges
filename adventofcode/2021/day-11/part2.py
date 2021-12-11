
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
    if checkBoundaries(board, x-1, y-1) is False:
        surrounding.append((x-1, y-1))

    if checkBoundaries(board, x-1, y) is False:
        surrounding.append((x-1, y))

    if checkBoundaries(board, x-1, y+1) is False:
        surrounding.append((x-1, y+1))

    if checkBoundaries(board, x, y-1) is False:
        surrounding.append((x, y-1))

    if checkBoundaries(board, x, y+1) is False:
        surrounding.append((x, y+1))

    if checkBoundaries(board, x+1, y-1) is False:
        surrounding.append((x+1, y-1))

    if checkBoundaries(board, x+1, y) is False:
        surrounding.append((x+1, y))

    if checkBoundaries(board, x+1, y+1) is False:
        surrounding.append((x+1, y+1))
    
    # print("Surroundings for ", x, y, surrounding)
    return surrounding


fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')
# fdata = open("simple.txt", 'r')

# Load data
octopuses = []
for line in fdata:
    line = line.rstrip()
    newline = []
    for i in range(0, len(line)):
        newline.append(int(line[i]))
    octopuses.append(newline)
    # print(line.rstrip())


# Print board
for line in range(0, len(octopuses)):
    for idx in range(0, len(octopuses[0])):
        print("%-3d" % octopuses[line][idx], end='')
    print("")
print("")

sum_of_flashes = 0
# For X steps:
flashed_simultaneously = False
simulation_time = 1
# for time in range(1, simulation_time+1):
while flashed_simultaneously is False:
    # One step
    # Increase all energy by 1 level
    for line in range(0, len(octopuses)):
        for idx in range(0, len(octopuses[0])):
            # new = False
            octopuses[line][idx] += 1
    
    # While there are still new enpowered (over 9) octopuses
    new_over_nine = []
    processed = []  # processed cells with value greater than 9
    new_found = True
    while new_found is True:
        new_found = False
        # Fill all new over 9
        # print("fill above nines")
        for line in range(0, len(octopuses)):
            for idx in range(0, len(octopuses[0])):
                if octopuses[line][idx] > 9:
                    if (line, idx) not in processed:
                        new_over_nine.append((line, idx))
                        new_found = True
                        
        # print(len(new_over_nine), new_over_nine)
        
        # increase neighbours energy level
        for newover in new_over_nine[:]:
            surrounding = getSurrounding(octopuses, newover[0], newover[1])
            for sur in surrounding:
                octopuses[sur[0]][sur[1]] += 1

            # Remove currently processed cell
            processed.append(newover)
            new_over_nine.remove(newover)
        # print(len(processed), processed)

    
    # print(len(processed), processed)
    for pd in processed:
        if octopuses[pd[0]][pd[1]] > 9:
            octopuses[pd[0]][pd[1]] = 0

    # Discharge all over 9
    sum_of_flashes += len(processed)
    for octopus in processed:
        octopuses[octopus[0]][octopus[1]] = 0

    # Print board
    print("Simulation step:", simulation_time)
    for line in range(0, len(octopuses)):
        for idx in range(0, len(octopuses[0])):
            print("%-3d" % octopuses[line][idx], end='')
        print("")
    print("")

    if len(processed) == len(octopuses) * len(octopuses[0]):
        flashed_simultaneously = True
        break

    simulation_time += 1

print("sum of flashes", sum_of_flashes)
print("sync time step",simulation_time)

