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
    distances_points = {}
    for cidx1 in range(len(list1)):
        for cidx2 in range(len(list2)):
            distance = str(round_down(math.dist(list1[cidx1], list2[cidx2]), 3))
            if distance in distances.keys():
                distances[distance] += 1
                # print(list1[cidx1])
                # print(distances_points[distance])
                # if any(list1[cidx1] == point for point in distances_points[distance]):
                # print(list1[cidx1].tolist())
                # print(list1[cidx1])
                # print()
                # print(distances_points[distance])
                if list1[cidx1].tolist() not in distances_points[distance]:
                    distances_points[distance].append(list1[cidx1].tolist())
            else:
                distances[distance] = 1
                distances_points[distance] = []
                distances_points[distance].append(list1[cidx1].tolist())

    for dist, dist_num in distances.items():
        if dist_num >= 12:
            # print(dist, dist_num)
            # print(distances_points[dist])
            # return True
            return distances_points[dist]

    return []

def find_corelation(ref_list, checked_list):
    """
    Transform input list of points to all 24 possible positions and
    return True, if some of the rotations have common points with second list of points.
    """
    common_beacons = []
    operations = []
    for flip in range(1, 5):
        operations.append("flip90up")
        flip90up(checked_list)
        for rot in range(1, 5):
            operations.append("rot90left")
            rot90left(checked_list)
            common_points = have_12_common(ref_list, checked_list)
            if common_points:
                print(operations)
                # return True
                return common_points

    for flip in range(1, 5):
        operations.append("flip90left")
        flip90left(checked_list)
        for rot in range(1, 5):
            operations.append("rot90left")
            rot90left(checked_list)
            common_points = have_12_common(ref_list, checked_list)
            if common_points:
                print(operations)
                # return True
                return common_points

    return []
    # return False

# ===============================================================================================

# data_file = "input_t1.txt"  # Test data - 2D
data_file = "input_t2.txt"  # Test data - 3D - arrangement of beacons as seen from a scanner in the same position but in different orientations
data_file = "input_t2_sub.txt"  # Test data - 3D - subset of above
data_file = "input_t2_sub2.txt"  # Test data - 3D - subset of above
# data_file = "input_t4_crafted.txt"  # Test data - 3D - subset of above
data_file = "input_t3.txt"  # Test data - 3D - larger test input
# data_file = "input_t3_sub1.txt"  # Test data - 3D - subset
# data_file = "i1.txt"  # Test data - 3D - subset
data_file = "input1.txt"  # Part 1 input data
# data_file = "input2.txt"  # Part 2 input data

fdata = open(data_file, 'r')

# ==== Initialization
scanner_regex = re.compile(r'--- scanner [0-9]{1,3} ---')
scanner_reports = {}
scanner_count = -1

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

beacons = []
# print(scanner_reports[1])
for scanner_x, report_x in enumerate(list(scanner_reports.values())):
    # print(scanner_reports[scanner_x])
    for scanner_y, report_y in enumerate(list(scanner_reports.values())[:scanner_x]):
        print("Porovnavam:", scanner_x, scanner_y)
        arr0 = np.array(report_x)
        arr1 = np.array(report_y)
        common_beacons = find_corelation(arr0, arr1)
        if not common_beacons:
            print("Could not find corelation")
        else:
            # if common_beacons not in beacons:
            beacons += common_beacons

# lst = beacons
# # 1. Convert into list of tuples
# tpls = [tuple(x) for x in lst]
# # 2. Create dictionary with empty values and
# # 3. convert back to a list (dups removed)
# dct = list(dict.fromkeys(tpls))
# # 4. Convert list of tuples to list of lists
# dup_free = [list(x) for x in dct]
# # Print everything
# print("deduplikovane beacons", len(dup_free))
# print(dup_free)

# print("Pocet nalezenych beacons", len(list( dict.fromkeys(beacons) )))
print("Pocet nalezenych beacons: ", len(beacons))
# print(list( dict.fromkeys(beacons) ))
print(beacons)
# plot_points({0: arr0, 1: arr1})


