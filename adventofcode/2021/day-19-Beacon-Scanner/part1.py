import re
import matplotlib.pyplot as plt
import numpy as np
import math
from collections import Counter

import decimal

def round_down(value, decimals):
    with decimal.localcontext() as ctx:
        d = decimal.Decimal(value)
        ctx.rounding = decimal.ROUND_DOWN
        return round(d, decimals)

def swap(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]

def plot_points(scanner_reports):
    fig = plt.figure()
    graph = fig.add_subplot(projection='3d')
    for key in scanner_reports.keys():
        graph.scatter(*zip(*scanner_reports[key]))
    plt.show()

def rot90right(input_array):
    swap(input_array, 0, 1)
    input_array[0:, 1] *= -1

def rot90left(input_array):
    swap(input_array, 0, 1)
    input_array[0:, 0] *= -1

def flip90up(input_array):
    swap(input_array, 1, 2)
    input_array[0:, 2] *= -1

def flip90down(input_array):
    swap(input_array, 1, 2)
    input_array[0:, 1] *= -1

def flip90right(input_array):
    swap(input_array, 0, 2)
    input_array[0:, 2] *= -1

def flip90left(input_array):
    swap(input_array, 0, 2)
    input_array[0:, 0] *= -1


def have_12_common(list1, list2):
    """
    Check, whether two provided lists of coordinates overlap in at least 12 points
    """
    # Find the 12 same distances between points of two arrays
    distances = {}
    final = []
    for cidx1 in range(len(list1)):
        for cidx2 in range(len(list2)):

            distance = str(round_down(math.dist(list1[cidx1], list2[cidx2]), 3))
            if distance in distances.keys():
                distances[distance] += 1
                final.append(list1[cidx1])
            else:
                distances[distance] = 1

    # min_common_points = 12  # Default: 12
    # if any(dist_num >= min_common_points for dist_num in distances.values()):
        # print(distances)
    for dist, dist_num in distances.items():
        if dist_num >= 12:
            print(dist, dist_num)
            # print(distances)
            print(final)
            return True

    return False


def find_corelation(ref_list, checked_list):
    """
    Transform input list of points to all 24 possible positions and
    return True, if some of the rotations have common points with second list of points.
    """
    operations = []
    for flip in range(1, 5):
        operations.append("flip90up")
        flip90up(checked_list)
        for rot in range(1, 5):
            operations.append("rot90left")
            rot90left(checked_list)
            if have_12_common(ref_list, checked_list):
                print(operations)
                return True

    for flip in range(1, 5):
        operations.append("flip90left")
        flip90left(checked_list)
        for rot in range(1, 5):
            operations.append("rot90left")
            rot90left(checked_list)
            if have_12_common(ref_list, checked_list):
                print(operations)
                return True

    return False

# ===============================================================================================

# data_file = "input_t1.txt"  # Test data - 2D
data_file = "input_t2.txt"  # Test data - 3D - arrangement of beacons as seen from a scanner in the same position but in different orientations
data_file = "input_t2_sub.txt"  # Test data - 3D - subset of above
data_file = "input_t2_sub2.txt"  # Test data - 3D - subset of above
# data_file = "input_t4_crafted.txt"  # Test data - 3D - subset of above
# data_file = "input_t3.txt"  # Test data - 3D - larger test input
data_file = "input_t3_sub1.txt"  # Test data - 3D - subset
# data_file = "input1.txt"  # Part 1 input data
# data_file = "input2.txt"  # Part 2 input data

fdata = open(data_file, 'r')

# ==== Initialization
scanner_regex = re.compile(r'--- scanner [0-9]{1,3} ---')
scanner_reports = {}
scanner_count = -1

numpy_reports = {}

# ==== Loading of input data
for line in fdata:
    line = line.rstrip()

    if line == "":
        continue

    # Match the "--- scanner x ---"
    if scanner_regex.search(line):
        scanner_count += 1
        scanner_reports[scanner_count] = []
        continue

    scanner_reports[scanner_count].append([int(x) for x in line.split(',')])


# ==== Data procession
# plot_points(scanner_reports)

print(scanner_reports[0])
arr0 = np.array(scanner_reports[0]) # + 0.1
arr1 = np.array(scanner_reports[1])

if not find_corelation(arr0, arr1):
    print("Could not find corelation")

plot_points({0: arr0, 1: arr1})


