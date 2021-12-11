
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


# fdata = open("input.txt", 'r')
fdata = open("input1.txt", 'r')
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


# For X steps:
simulation_time = 2
for i in range(0, simulation_time):

    # One step
    # Increase all energy by 1 level
    for line in range(0, len(octopuses)):
        for idx in range(0, len(octopuses[0])):
            # new = False
            octopuses[line][idx] += 1

    # Calculate flashing neighbourhood - probably while over_nine is not empty:
    # TODO: probably while new values are above 9, loop smthg like this
    
    toprocess = []
    processed = []
    while len(toprocess):
        print("fill above nines")
        for line in range(0, len(octopuses)):
            for idx in range(0, len(octopuses[0])):
                if octopuses[line][idx] > 9:
                    if (line, idx) not in toprocess and (line, idx) not in processed:
                        toprocess.append((line, idx))
                        # surrounding = getSurrounding(octopuses, line, idx)
                        # for sur in surrounding:
                            # octopuses[sur[0]][sur[1]] += 1
                            # if sur not in procesed and sur not in toprocess:
                                # toprocess.append(sur)

        print(len(toprocess), toprocess)
        for oc in toprocess[:]:
            if octopuses[oc[0]][oc[1]] > 9:
                surrounding = getSurrounding(octopuses, oc[0], oc[1])
                for sur in surrounding:
                    octopuses[sur[0]][sur[1]] += 1
                    if sur not in procesed and sur not in toprocess:
                        toprocess.append(sur)

                processed.append(oc)
                toprocess.remove(oc)
                # some_over_nine = True
        print(len(processed), processed)

    print(len(processed), processed)
    for pd in processed:
        if octopuses[pd[0]][pd[1]] > 9:
            octopuses[pd[0]][pd[1]] = 0

        

    # initial over-nine values
    # over_nine = []
    # new_nine = True
    # while new_nine is True:
    #     some_over_nine = False
    #     for line in range(0, len(octopuses)):
    #         for idx in range(0, len(octopuses[0])):
    #             if octopuses[line][idx] > 9:
    #                 some_over_nine = True
    #                 if (line, idx) not in over_nine:
    #                     over_nine.append((line, idx))
    #                     surrounding = getSurrounding(octopuses, line, idx)
    #                     for sur in surrounding:
    #                         octopuses[sur[0]][sur[1]] += 1
    #                     new_nine = True
    #                 else:
    #                     new_nine = False
    #     # Prevent infinite loop if no new value over nine was found
    #     if some_over_nine is False:
    #         break


    # maybe endwhile
    # todo: probably mark all cels with some tag, representing that they were not flashing and flash only if they were not flashing this step.

    # Filter duplicates
    # over_nine = list(set(over_nine))


    # Now flash all over 9
    # for flash in over_nine:
        # octopuses[flash[0]][flash[1]] = 0
    
    # Print board
    for line in range(0, len(octopuses)):
        for idx in range(0, len(octopuses[0])):
            print("%-3d" % octopuses[line][idx], end='')
        print("")
    print("")



fdata.close()
