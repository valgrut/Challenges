from functools import reduce
import operator

def bin_format(hexint, length):
    return f'{hexint:0>{length}b}'


def parse_packet(bit_length=None, number_of_subpackets=None):
    """
    Pass bit_length 
        OR 
    number of subpackets.

    Returns new pointer position.

    Function is expected to be called recursively.
    """
    global bin_packet
    global pointer

    print("::Called parse_packet,", number_of_subpackets)

    # pointer = pointer_position

    return_values = []
    pkt_id = ""
    n = 0
    returned = False

    # TODO: Poznamka: mozna cele while dat do funkce, a udelat zpracovani treba pro nejaky segment vstupniho packetu -
    # jakoze z celeho packetu treba vim, ze nasledujichich X bitu jsou subpackety, takze predam od aktualniho po X bity
    # teto funkci, a ona to rozparsuje.
    # TODO: Nebo parsovani jednotlivych sub packetu vyclenit do funkci. Nakreslit si to.

    # Determine, if we will parse N sub packets or X bits of subpackets
    sentinel = 0
    if bit_length is not None:
        sentinel = bit_length
    else:
        sentinel = len(bin_packet)-1

    next = "start"
    # while next is not "end" or pointer < len(bin_packet)-1:
    # while pointer < sentinel:
    while pointer <= sentinel+1:
        # print("ptr", pointer, '<', sentinel, " Next=", next)
        print("> Gefore IFs")

        if next == "start":
            print()
            print(">START")

            if number_of_subpackets not in [0, None] and n >= number_of_subpackets:
                break

            print(">START: Zbyva dost bitu na dalsi paket?", pointer, sentinel)
            if sentinel <= pointer + 6:
                print(return_values)
                print(">START: exit START")
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
            pkt_version = version
            # versions_sum += int(version, 2)
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
            if pkt_id == "":
                pkt_id = int_type

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

        # GROUP
        elif next == "notlastgroup":
            print(">GROUP")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1

            int_type = int(group, 2)
            return_values.append(int_type)
            print("Group", int_type)

            next = "type4"

        # GROUP LAST
        elif next == "lastgroup":
            print(">GROUP last")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1

            int_type = int(group, 2)
            return_values.append(int_type)
            print("Last Group", int_type)

            next = "end"

        # TODO: Pro kazdou rekurzi potrebuju vratit pod whilem ziskanou hodnotu literalu,
        # abych na t echto hodnotach nasledne mohl provest danou operaci. ta zase
        # podobne jako literaly bude vracena dale.

        # END
        elif next == "end":
            print(">END")
            # print("Groups literal value", int(groups_literal, 2))
            n += 1
            print("pointer:", pointer, " sentinel:", sentinel)

            print("END - pkt_ID", pkt_id)

            #if pkt_id == 4:
            #    print(">>>>LITERAL:", return_values)
            #    return return_values

            if returned is True:
                break

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

            ### Evaluovat aktualni vysledek?

            if pointer+6 < sentinel:
                #if pointer > sentinel -2:
                #    break
                print("end: next = start")
                next = "start"
            else:
                print("end: break")
                break

        # Packet Type: Operator
        elif next == "operator":
            print(">OPERATOR")
            mode = bin_packet[pointer]
            pointer += 1

            if mode == '0':
                next = "mode1"
            else:
                next = "mode2"

        # SUBPACKETS LENGTH
        elif next == "mode1":
            print(">MODE1 (15) - bit len of subpackets")
            # Read 15 bits
            total_len_of_subpackets = ""
            for i in range(15):
                total_len_of_subpackets += bin_packet[pointer]
                pointer += 1

            total_len = int(total_len_of_subpackets, 2)
            max_sub_pointer = pointer + total_len  # experimental
            
            # print("total_length_of_subpackets", total_len)
            # print(pointer, max_sub_pointer)
            
            return_values.append(parse_packet(bit_length=max_sub_pointer + 1))
            # returned = True

            next = "end" #start

        # SUBPACKETS NUMBER
        elif next == "mode2":
            print(">MODE2 (11) - number of subpackets")
            # Read 11 bits
            bin_number_of_subpackets = ""
            for i in range(11):
                bin_number_of_subpackets += bin_packet[pointer]
                pointer += 1

            num_of_subpackets = int(bin_number_of_subpackets, 2)

            print("number_of_subpackets", num_of_subpackets)

            # return_values = []
            # for i in range(num_of_subpackets):
            return_values.append(parse_packet(number_of_subpackets=num_of_subpackets))
            returned = True
            # print("returned ", i, "/", num_of_subpackets)

            #print(return_values)
            #print(return_values, sum(return_values))
            
            # after all subpackets, we get all required values. Calculate result.
            
            # break

            next = "end" #start
            

        # EVALUATION
        elif next == "evaluation":
            pass


    # End of While:
    print(">after WHILE", pointer, sentinel)
    print("Groups literals list:", return_values)
    print("pkt type:", pkt_id)
    
    return_values = linearize(return_values)

    if pkt_id == 4:
        print(">>>> just return list:", return_values)
        return return_values

    if pkt_id == 0:
        # Sum of literal values
        print(">>>>SUM:", sum(return_values))
        return sum(return_values)
    
    if pkt_id == 1:
        # print(return_values)
        print(">>>>PRODUCT:", product(return_values))
        return reduce(operator.mul, return_values, 1)

    if pkt_id == 2:
        print(">>>>MIN:", min(return_values))
        return min(return_values)
        
    if pkt_id == 3:
        print(">>>>MAX:", max(return_values))
        return max(return_values)

    if pkt_id == 5:
        print(">>>>GREATER:", return_values[0] > return_values[1])
        return 1 if return_values[0] > return_values[1] else 0

    if pkt_id == 6:
        print(">>>>SMALLER:", return_values[0] < return_values[1])
        return 1 if return_values[0] < return_values[1] else 0
    
    if pkt_id == 7:
        print(">>>>EQUAL:", return_values[0] == return_values[1])
        return 1 if return_values[0] == return_values[1] else 0


def linearize(input):
    linearized = []
    for i in input:
        if isinstance(i, list):
            linearized.extend(linearize(i))
        else:
            linearized.append(i)
    return linearized


def product(input):
    prod = 0
    for i in input:
        if isinstance(i, list):
            if prod == 0:
                prod = product(i)
            else:
                prod *= product(i)
        else:
            if prod == 0:
                prod = i
            else:
                prod *= i
    return prod


def evaluate_packet(packet_data):
    global pointer
    global bin_packet
    # Convert from hex to bin

    integer = int(packet_data, 16)
    bin_packet = bin_format(integer, len(packet_data) * 4)

    pointer = 0
    result = parse_packet(bit_length=len(bin_packet) - 1)
    return result


def TEST(input_string, expected):
    value = evaluate_packet(input_string)
    global passed
    if value != expected:
        print("[FAIL]:", value, "is not equal", expected, "(input:", input_string,")")
    else:
        passed += 1
        print("[PASS]:", value, "is equal", expected, "(input:", input_string,")")


if __name__ == "__main__":
    # fdata = open("input_short.txt", 'r')  # Literal packet
    # fdata = open("input-operator.txt", 'r')  # Operator with 2 subpackets 
    # fdata = open("input-three-sub.txt", 'r')
    # fdata = open("input_1.txt", 'r')  # should have total value of 16  # OK
    # fdata = open("input_2.txt", 'r')  # should have total value of 12
    # fdata = open("input_3.txt", 'r')  # should have total value of 23
    # fdata = open("input_4.txt", 'r')  # should have total value of 31   # OK
    # fdata = open("input.txt", 'r')
    
    # packet = fdata.readline().rstrip()
    # print(packet)

    global pointer
    global bin_packet

    global passed
    passed = 0

    TEST("C200B40A82", 3)
    TEST("04005AC33890", 54)
    TEST("880086C3E88112", 7)
    TEST("CE00C43D881120", 9)
    TEST("D8005AC2A8F0", 1)
    TEST("F600BC2D8F", 0)
    TEST("9C005AC2F8F0", 0)
    TEST("9C0141080250320F1802104A08", 1)

    print("PASSED ", passed)