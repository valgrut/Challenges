if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    with open(input_file, 'r') as file:
        for calibration in file:
            print(calibration.rstrip())
    print(final_sum)

    # print("Versions sum", versions_sum)
