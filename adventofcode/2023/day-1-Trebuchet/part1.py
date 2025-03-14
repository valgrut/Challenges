if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    final_sum = 0
    with open(input_file, 'r') as file:
        for calibration in file:
            print(calibration)
            first_int = None
            last_int = None
            for value in calibration:
                if value.isdigit() and first_int is None:
                    first_int = value
                if value.isdigit():
                    last_int = value
            calibration_result = first_int + last_int
            print(calibration_result)
            final_sum += int(calibration_result)
    print(final_sum)

    # print("Versions sum", versions_sum)
