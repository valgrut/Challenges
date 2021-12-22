
def bin_format(hexint, length):
    return f'{hexint:0>{length}b}'


if __name__ == "__main__":
    # fdata = open("input_short.txt", 'r')
    # fdata = open("input-operator.txt", 'r')
    # fdata = open("input-three-sub.txt", 'r')
    # fdata = open("input_1.txt", 'r')  # should have total value of 16  # OK
    fdata = open("input_2.txt", 'r')  # should have total value of 12
    # fdata = open("input_3.txt", 'r')  # should have total value of 23
    # fdata = open("input_4.txt", 'r')  # should have total value of 31   # OK
    # fdata = open("input.txt", 'r')


    packet = fdata.readline().rstrip()
    print(packet)

    # 1. convert to bin
    integer = int(packet, 16)
    bin_packet = bin_format(integer, len(packet) * 4)

    pointer = 0

    # jen docasna promenna pro testovani groups - nebude fungovat pro zanorene
    groups_value = ""
    subs = 0
    max_sub_pointer = 0
    versions_sum = 0

    # TODO: Poznamka: mozna cele while dat do funkce, a udelat zpracovani treba pro nejaky segment vstupniho packetu -
    # jakoze z celeho packetu treba vim, ze nasledujichich X bitu jsou subpackety, takze predam od aktualniho po X bity
    # teto funkci, a ona to rozparsuje.

    next = "start"
    # while next is not "end" or pointer < len(bin_packet)-1:
    while pointer < len(bin_packet) - 1:
        # print("ptr", pointer)
        if next == "start":
            # for subpackets
            if subs > 0:
                subs -= 1
            next = "version"

        elif next == "version":
            version = ""
            for i in range(3):
                version += bin_packet[pointer]
                pointer += 1
            print("Version", int(version, 2))
            versions_sum += int(version, 2)
            next = "type"

        elif next == "type":
            type = ""
            for i in range(3):
                type += bin_packet[pointer]
                pointer += 1

            int_type = int(type, 2)
            print("Type", int_type)

            if int_type == 4:
                next = "type4"
            else:
                next = "operator"

        elif next == "type4":
            is_last = bin_packet[pointer]
            pointer += 1

            if is_last == '0':
                next = "lastgroup"
            else:  # is_last == '1'
                next = "notlastgroup"

        elif next == "operator":
            mode = bin_packet[pointer]
            pointer += 1

            if mode == '0':
                next = "mode1"
            else:
                next = "mode2"

        # GROUP
        elif next == "notlastgroup":
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1

            groups_value += group

            int_type = int(group, 2)
            print("Group", int_type)
            next = "type4"

        # GROUP
        elif next == "lastgroup":
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1

            groups_value += group

            int_type = int(group, 2)
            print("Last Group", int_type)

            next = "end"

        # END
        elif next == "end":
            print("Groups literal value", int(groups_value, 2))
            groups_value = ""
            print("end")

            # experimental - for subpackets
            print(len(bin_packet), max_sub_pointer, pointer)
            if subs > 0 or max_sub_pointer > pointer:
                print("to start again")
                next = "start"
            else:
                break

        elif next == "mode1":
            # Read 15 bits
            total_len_of_subpackets = ""
            for i in range(15):
                total_len_of_subpackets += bin_packet[pointer]
                pointer += 1

            total_len = int(total_len_of_subpackets, 2)
            max_sub_pointer = pointer + total_len  # experimental
            print("total_length_of_subpackets", total_len)
            next = "start"

        elif next == "mode2":
            # Read 11 bits
            number_of_subpackets = ""
            for i in range(11):
                number_of_subpackets += bin_packet[pointer]
                pointer += 1

            num_of_subs = int(number_of_subpackets, 2)
            subs = num_of_subs
            print("number_of_subpackets", num_of_subs)
            next = "start"

    print("Versions sum", versions_sum)