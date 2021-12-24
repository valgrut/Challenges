
def bin_format(hexint, length):
    return f'{hexint:0>{length}b}'

def parse_packet(pointer_position, bit_length=None, number_of_subpackets=None):
    """
    Pass bit_length 
        OR 
    number of subpackets.

    Returns new pointer position.

    Function is expected to be called recursively.
    """
    global bin_packet
    global versions_sum

    pointer = pointer_position

    groups_value = ""


    # Determine, if we will parse N sub packets or X bits of subpackets
    sentinel = 0
    if bit_length is not None:
        sentinel = bit_length
    else:
        sentinel = len(bin_packet)-1

    next = "start"
    while pointer < sentinel:
        # print("ptr", pointer, '<', sentinel, " Next=", next)
        if next == "start":
            print()
            print(">START")
            #print("Mam jeste pokracoval????", pointer, sentinel)
            if sentinel <= pointer + 6:
                break
            next = "version"

        # VERSION
        elif next == "version":
            print(">VERSION")
            version = ""
            for i in range(3):
                version += bin_packet[pointer]
                pointer += 1
            
            print("Version", int(version, 2))
            versions_sum += int(version, 2)
            next = "type"

        # TYPE
        elif next == "type":
            print(">TYPE identification")
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

        # Packet Type: 4
        elif next == "type4":
            print(">TYPE 4")
            is_last = bin_packet[pointer]
            pointer += 1

            if is_last == '0':
                next = "lastgroup"
            else:  # is_last == '1'
                next = "notlastgroup"

        # Packet Type: Operator
        elif next == "operator":
            print(">OPERATOR")
            mode = bin_packet[pointer]
            pointer += 1

            if mode == '0':
                next = "mode1"
            else:
                next = "mode2"

        # GROUP
        elif next == "notlastgroup":
            print(">GROUP")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1

            groups_value += group

            int_type = int(group, 2)
            print("Group", int_type)
            next = "type4"

        # GROUP LAST
        elif next == "lastgroup":
            print(">GROUP last")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1
            # print(group)
            groups_value += group

            int_type = int(group, 2)
            print("Last Group", int_type)

            next = "end"

        # END
        elif next == "end":
            print(">END")
            print("Groups literal value", int(groups_value, 2))
            groups_value = ""
            

            # experimental - for subpackets
            # print('len(bin_packet)', len(bin_packet), 'pointer:', pointer, 'sentinel:', sentinel)
            # if subs > 0 or max_sub_pointer > pointer:
            #     print("to start again")
            #     next = "start"
            # else:
            #     break

            # print("Mam jeste pokracoval????", pointer, sentinel)
            # if sentinel <= pointer + 6:
            #     break

            if pointer < sentinel:
                if pointer > sentinel -2:
                    break
                next = "start"
            else:
                break

        elif next == "mode1":
            print(">MODE1 (15)")
            # Read 15 bits
            total_len_of_subpackets = ""
            for i in range(15):
                total_len_of_subpackets += bin_packet[pointer]
                pointer += 1

            total_len = int(total_len_of_subpackets, 2)
            max_sub_pointer = pointer + total_len  # experimental
            
            # print("total_length_of_subpackets", total_len)
            # print(pointer, max_sub_pointer)
            
            pointer = parse_packet(pointer, bit_length=max_sub_pointer + 1)

            next = "start"

        elif next == "mode2":
            print(">MODE2 (11)")
            # Read 11 bits
            number_of_subpackets = ""
            for i in range(11):
                number_of_subpackets += bin_packet[pointer]
                pointer += 1

            num_of_subs = int(number_of_subpackets, 2)
            subs = num_of_subs

            # print("number_of_subpackets", num_of_subs)

            for i in range(subs):
                pointer = parse_packet(pointer)
            
            next = "start"

    

    # Return final pointer position
    return pointer



if __name__ == "__main__":
    # fdata = open("input_short.txt", 'r')  # Literal packet
    # fdata = open("input-operator.txt", 'r')  # Operator with 2 subpackets 
    # fdata = open("input-three-sub.txt", 'r')
    # fdata = open("input_1.txt", 'r')  # should have total value of 16  # OK
    # fdata = open("input_2.txt", 'r')  # should have total value of 12
    # fdata = open("input_3.txt", 'r')  # should have total value of 23
    # fdata = open("input_4.txt", 'r')  # should have total value of 31   # OK
    fdata = open("input.txt", 'r')
    packet = fdata.readline().rstrip()
    # print(packet)

    # packet = "C200B40A82"
    # packet = "04005AC33890"
    # packet = "880086C3E88112"
    # packet = "CE00C43D881120"
    # packet = "D8005AC2A8F0"

    # 1. convert to bin
    integer = int(packet, 16)
    bin_packet = bin_format(integer, len(packet) * 4)

    pointer = 0

    # jen docasna promenna pro testovani groups - nebude fungovat pro zanorene
    groups_value = ""
    subs = 0
    max_sub_pointer = 0
    versions_sum = 0

    parse_packet(0, bit_length=len(bin_packet) - 1)

    print("Versions sum", versions_sum)