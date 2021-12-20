#! /usr/bin/env python3

fdata = open("report.txt", 'r')

# Removing items while iterating: 
#   https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating


def count_zeros_ones(data):
    """
    input: 
        data: list of strings
    output:
        zeros: list of '0' counts on all positions
        ones: list of '1' counts on all positions
    """

    zeros = []
    ones = []
    init = False

    for line in data:
        if init is False:
            zeros = [0 for i in range(0, len(line))]
            ones = [0 for i in range(0, len(line))]
            init = True

        for i in range(0, len(line)):
            if line[i] == "0":
                zeros[i] += 1 
            else:
                ones[i] += 1 

    return zeros, ones


# Init list with data
report_data = []
for data in fdata:
    data = data.rstrip()
    report_data.append(data)

data_len = len(report_data[0])

# Oxygen generator raging
oxygen_data = report_data.copy()
while len(oxygen_data) > 1:
    # Tetermine most common value for current i
    # For each bit of data
    for i in range(0, data_len):
        zeros_count, ones_count = count_zeros_ones(oxygen_data)
        most_common_for_i = '1' if ones_count[i] >= zeros_count[i] else '0'
        if len(oxygen_data) == 1:
            break
        # for each remaining data in list
        for line in oxygen_data[:]:
            # remove all lines not satisfying bit-criteria
            if line[i] != most_common_for_i:
                oxygen_data.remove(line)

print(oxygen_data)


# CO2 Scrubber rating
co2_data = report_data.copy()
while len(co2_data) > 1:
    # Tetermine most common value for current i
    # For each bit of data
    for i in range(0, data_len):
        zeros_count, ones_count = count_zeros_ones(co2_data)
        least_common_for_i = '1' if ones_count[i] < zeros_count[i] else '0'
        if len(co2_data) == 1:
            break
        # for each remaining data in list
        for line in co2_data[:]:
            # remove all lines not satisfying bit-criteria
            if line[i] != least_common_for_i:
                co2_data.remove(line)

print(co2_data)

print(int(oxygen_data[0], 2), int(co2_data[0], 2))
print("Life support rating: ", int(co2_data[0], 2) * int(oxygen_data[0], 2))

fdata.close()


