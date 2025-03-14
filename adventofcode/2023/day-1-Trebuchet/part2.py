if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input2.txt"
    final_sum = 0

    with open(input_file, 'r') as file:
        for calibration in file:
            calibration = calibration.rstrip()
            print(calibration)

            first_int = None
            last_int = None

            ivalue = None
            i = 0
            while i < len(calibration):
                value = calibration[i]
                # print(calibration, ":", value)
                if value.isdigit():
                    ivalue = value
                    i += 1
                elif calibration[i:i+3] == "one":
                    ivalue = '1'
                    i += 1 #3 (1, bo musim odchytit pripady jako "oneight")
                    # (jinak bych nezachytil tu eight, protoze bych po
                    # detekci 'one' preskocil na znak 'i')
                elif calibration[i:i+3] == "two":
                    ivalue = '2'
                    i += 1 #3
                elif calibration[i:i+5] == "three":
                    ivalue = '3'
                    i += 1 #5
                elif calibration[i:i+4] == "four":
                    ivalue = '4'
                    i += 1 #4
                elif calibration[i:i+4] == "five":
                    ivalue = '5'
                    i += 1 #4
                elif calibration[i:i+3] == "six":
                    ivalue = '6'
                    i += 1 #3
                elif calibration[i:i+5] == "seven":
                    ivalue = '7'
                    i += 1 #5
                elif calibration[i:i+5] == "eight":
                    ivalue = '8'
                    i += 1 #5
                elif calibration[i:i+4] == "nine":
                    ivalue = '9'
                    i += 1 #4
                else:
                    i += 1

                if first_int is None:
                    first_int = ivalue
                last_int = ivalue
                # if first_int is None and ivalue is not None:
                    # first_int = ivalue
                # if ivalue is not None:
                    # last_int = ivalue

            calibration_result = first_int + last_int
            print(calibration_result)
            print()

            final_sum += int(calibration_result)

    print(final_sum)
