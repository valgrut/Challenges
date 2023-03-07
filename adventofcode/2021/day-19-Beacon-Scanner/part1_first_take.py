import re
import matplotlib.pyplot as plt
import numpy as np

def swap(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]

def plot_points(scanner_reports):
    fig = plt.figure()
    graph = fig.add_subplot(projection='3d')
    for key in scanner_reports.keys():
        graph.scatter(*zip(*scanner_reports[key]))
    plt.show()

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

# Initialization
scanner_regex = re.compile(r'--- scanner [0-9]{1,3} ---')
scanner_reports = {}
scanner_count = -1

numpy_reports = {}
# Loading of input data
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

# Data procession
# plot_points(scanner_reports)

print(scanner_reports[0])
arr0 = np.array(scanner_reports[0]) # + 0.1
arr1 = np.array(scanner_reports[1])

#######################################################################
#-- PROLINAJI SE!!!
# print(arr1)
# arr1[:,0] *= -1  # Vertikalni zrcadleni bodu na X (otoceni 90 doleva)
# print(arr1)
# swap(arr1, 1, 2)  # zrcadleni podle z a x(nebo y?)
# print(arr1)
# arr1[:,1] *= -1  # Vertikalni zrcadleni bodu na Y (otoceni 90 doprava)
# print(arr1)
# arr1[:,2] *= -1  # zrcadlove preved body (Z souradnice) (Horizontalni reflexe) (90 nahoru)

#TODO: Analyzovat tyto 4 kroky od prvniho az po ten ctvrty, a zapsat, co konkretne kazdy krok udela s body a zapsat do komentare.
# Note: Takze je to mozne pomoci techto operaci to udelat!!!!!
# Note: Zalezi na poradi operaci!!!
# Vypsat si jednotlive transformovane body, abych vedel, co se s nimi stalo, a pripadne to nasazet do transformacni matice.
#######################################################################

def reflection_x(input_array):
    input_array[:,0] *= -1  # Vertikalni zrcadleni bodu na X (otoceni 90 doleva)

def reflection_y(input_array):
    input_array[:,1] *= -1  # Vertikalni zrcadleni bodu na Y (otoceni 90 doprava)

def reflection_z(input_array):
    input_array[:,2] *= -1  # Horizontalni zrcadleni bodu na Z (otoceni 90 nahoru)

def swap_xy(input_array):
    swap(input_array, 0, 1)

def swap_xz(input_array):
    swap(input_array, 0, 2)

def swap_yz(input_array):
    swap(input_array, 1, 2)

# transformations={"ref_x": reflection_x, "ref_y": reflection_y, "ref_z": reflection_z, "swap_xy": swap_xy, "swap_xz": swap_xz, "swap_yz": swap_yz}
transformations={0: reflection_x, 1: reflection_y, 2: reflection_z, 3: swap_xy, 4: swap_xz, 5: swap_yz}
# Calling the ops:
#   transformations["ref_x"](arr1)

def detect_common_points(array1, array2):
    # TODO: Predelat na detekci alespon 12 spolecnych bodu
    return True if (array1 == array2).all() else False

# it = 0
# explored_configurations = []
# transform_stack = []
# transform_stack = list(transformations.keys())  # Push first transformation
# print(transform_stack)
# while len(transform_stack) > 0:
#     print(f"iteration {it}")

#     top_op = transform_stack.pop()
#     transformations[top_op](arr1)
    # if any(arr1 in explored_configurations):
        # print(explored_configurations)
        # continue
    # else:
        # print("Adding explored conf")

#     if detect_common_points(arr0, arr1):
#         print("Arrays have at least 12 common points")
#         break

    # it += 1


def is_explored(explored, list1):
    for ex in explored:
        if (list1 == ex).all():
            # print("lists are same")
            # print(list1, ex)
            return True
    return False

def have_12_common(list1, list2):
    aset = set([tuple(x) for x in list1])
    bset = set([tuple(x) for x in list2])
    common_list = np.array([x for x in aset & bset])
    # print(len(common_list), common_list)
    if len(common_list) >= 12:
        return True
    return False



def backtracking(arr, transform, depth):
    # if depth > 6:
        # return False

    print("depth: ", depth, "transf:", transform)

    transformations[transform](arr1)

    if is_explored(explored, arr1):
        return False
    else:
        explored.append(arr1.copy())

    # if (arr1 == arr0).all():
    if have_12_common(arr0, arr1):
        print("FOUND")
        # print(arr0)
        # print(arr1)
        return True

    for tr in transformations.keys():
        value = backtracking(arr1, tr, depth + 1)
        if value is True:
            return True

    return False


# ----- MAIN -----
explored = []
backtracking(arr1, 0, 0)
plot_points({0: arr0, 1: arr1})


