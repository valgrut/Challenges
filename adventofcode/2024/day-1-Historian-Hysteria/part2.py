

if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    
    col1 = []
    col2 = []
    
    with open(input_file, 'r') as file:
        for line in file:
            splitted = line.strip("\n").split("   ")
            col1.append(int(splitted[0]))
            col2.append(int(splitted[1]))
    
    # magic of the part 2 here:
    col1_total = [0, ]
    for row1_i in range(0, len(col1)):
        col1_total.append(0)
        for row2 in col2:
            if col1[row1_i] == row2:
                col1_total[row1_i] += 1
    
    # Check numbers
    # print(col1)
    # print(col1_total)
    
    final_sum = 0
    
    for row in range(0, len(col1)):
        final_sum += (col1[row] * col1_total[row])
    print(final_sum)

    # print("Versions sum", versions_sum)
