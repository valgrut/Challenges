

if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    
    final_sum = 0
    
    col1 = []
    col2 = []
    
    with open(input_file, 'r') as file:
        for line in file:
            splitted = line.strip("\n").split("   ")
            col1.append(int(splitted[0]))
            col2.append(int(splitted[1]))
    
    # print(col1)
    # print(col2)
    
    col1.sort()
    col2.sort()

    # print(col1)
    # print(col2)

    for row in range(0, len(col1)):
        final_sum += abs(col2[row] - col1[row])

    print(final_sum)

    # print("Versions sum", versions_sum)
