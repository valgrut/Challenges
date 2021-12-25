from functools import reduce
import operator
import logging, sys

def bin_format(hexint, length):
    return f'{hexint:0>{length}b}'

def parse_packet(pointer_start):
    global bin_packet

    logging.info("::Called parse_packet,")

    pointer = pointer_start

    final_group = ""
    return_values = []
    pkt_id = ""
    pkt_version = ""

    next = "start"
    while next != "end":
        if next == "start":
            logging.info("")
            logging.info(">START")
            
            next = "version"

        # VERSION
        elif next == "version":
            logging.info(">VERSION")
            version = ""
            for i in range(3):
                version += bin_packet[pointer]
                pointer += 1
            
            logging.info("Version %d" % int(version, 2))
            pkt_version = int(version, 2)
            next = "type"

        # TYPE
        elif next == "type":
            logging.info(">TYPE identification")
            type = ""
            for i in range(3):
                type += bin_packet[pointer]
                pointer += 1

            int_type = int(type, 2)
            logging.debug("Type: %d" % int_type)
            
            pkt_id = int_type

            if int_type == 4:
                next = "type4"
            else:
                next = "operator"

        # Packet Type: 4
        elif next == "type4":
            logging.info(">TYPE 4")
            is_last = bin_packet[pointer]
            pointer += 1

            if is_last == '0':
                next = "lastgroup"
            else:  # is_last == '1'
                next = "notlastgroup"

        # GROUP
        elif next == "notlastgroup":
            logging.info(">GROUP")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1
            
            # Append group part into the final_group for 
            # evaluation in GROUP LAST.
            final_group += group

            next = "type4"

        # GROUP LAST
        elif next == "lastgroup":
            logging.info(">GROUP last")
            group = ""
            for i in range(4):
                group += bin_packet[pointer]
                pointer += 1
            
            final_group += group

            int_type = int(final_group, 2)
            return_values.append(int_type)
            logging.debug("Last Group %d" % int_type)

            final_group = ""

            next = "end"

        # END
        elif next == "end":
            logging.info(">END")
            break

        # Packet Type: Operator
        elif next == "operator":
            logging.info(">OPERATOR")
            mode = bin_packet[pointer]
            pointer += 1

            if mode == '0':
                next = "mode1"
            else:
                next = "mode2"

        # SUBPACKETS LENGTH
        elif next == "mode1":
            logging.info(">MODE1 (15) - bit len of subpackets")
            # Read 15 bits
            total_len_of_subpackets = ""
            for i in range(15):
                total_len_of_subpackets += bin_packet[pointer]
                pointer += 1

            total_len = int(total_len_of_subpackets, 2)
            max_sub_pointer = pointer + total_len
            
            while pointer < max_sub_pointer:
                new_pointer, result = parse_packet(pointer)
                pointer = new_pointer
                return_values.append(result)  

            next = "end"

        # SUBPACKETS NUMBER
        elif next == "mode2":
            logging.info(">MODE2 (11) - number of subpackets")
            
            # Read 11 bits
            bin_number_of_subpackets = ""
            for i in range(11):
                bin_number_of_subpackets += bin_packet[pointer]
                pointer += 1

            num_of_subpackets = int(bin_number_of_subpackets, 2)

            logging.info("number_of_subpackets %d" % num_of_subpackets)
            # print(f"number_of_subpackets: {num_of_subpackets}")

            for i in range(num_of_subpackets):
                new_pointer, result = parse_packet(pointer)
                pointer = new_pointer
                return_values.append(result)

            next = "end"


    # End of While:
    logging.info(">after WHILE %d" % pointer)
    logging.info("Groups literals list: %s" % return_values)
    logging.info("pkt type: %d" % pkt_id)

    logging.info("::returned parse_packet,")
    
    return_values = linearize(return_values)

    if pkt_id == 4:
        logging.info(">>>> just return list:" % return_values)
        # print(f"Values: {return_values} -> {return_values}")
        return (pointer, return_values)

    if pkt_id == 0:
        # Sum of literal values
        logging.info(">>>>SUM: %d" % sum(return_values))
        # print(f"+: {return_values} -> {sum(return_values)}")
        return (pointer, sum(return_values))
    
    if pkt_id == 1:
        # print(return_values)
        # logging.info(">>>>PRODUCT: %d" % product(return_values))
  
        # print(f"*: {return_values} -> {reduce(operator.mul, return_values, 1)}")
        return (pointer, reduce(operator.mul, return_values, 1))

    if pkt_id == 2:
        logging.info(">>>>MIN: %d" % min(return_values))
        # print(f"min: {return_values} -> {min(return_values)}")
        return (pointer, min(return_values))
        
    if pkt_id == 3:
        logging.info(">>>>MAX: %d" % max(return_values))
        # print(f"max: {return_values} -> {max(return_values)}")
        return (pointer, max(return_values))

    if pkt_id == 5:
        # logging.info(">>>>GREATER: %s" % return_values[0] > return_values[1])
        # print(f">: {return_values} -> {1 if return_values[0] > return_values[1] else 0}")
        return (pointer, 1) if return_values[0] > return_values[1] else (pointer, 0)

    if pkt_id == 6:
        # logging.info(">>>>SMALLER: %s" % return_values[0] < return_values[1])
        # print(f"<: {return_values} -> {1 if return_values[0] < return_values[1] else 0}")
        return (pointer, 1) if return_values[0] < return_values[1] else (pointer, 0)
    
    if pkt_id == 7:
        # logging.info(">>>>EQUAL: %s" % return_values[0] == return_values[1])
        # print(f"==: {return_values} -> {1 if return_values[0] == return_values[1] else 0}")
        return (pointer, 1) if return_values[0] == return_values[1] else (pointer, 0)



def linearize(input):
    linearized = []
    for i in input:
        if isinstance(i, list):
            linearized.extend(linearize(i))
        else:
            linearized.append(i)
    return linearized


def evaluate_packet(packet_data):
    """
    Input: string in hexadecimal format.
    i.e. "C200B40A82"
    Returns: Evaluated expression packet value

    This function transforms hexadecimal input into
    binary input ('0111001010011101...') and pass
    it into packet parser.
    """
    global bin_packet
    
    # Convert from hex to bin
    integer = int(packet_data, 16)
    bin_packet = bin_format(integer, len(packet_data) * 4)

    init_pointer = 0
    pointer, result = parse_packet(init_pointer)
    return result


def TEST(input_string, expected):
    value = evaluate_packet(input_string)
    global passed

    if len(input_string) > 15:
        input_string = input_string[0:15] + "..." + input_string[-3:]

    if value != expected:
        print(f"[FAIL]: {value} is not equal {expected} (input: {input_string})")
    else:
        passed += 1
        print(f"[PASS]: {value} is equal {expected} (input: {input_string})")


if __name__ == "__main__":
    # Levels = NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    global bin_packet
    global passed

    passed = 0

    # Run all example inputs
    TEST("C200B40A82", 3)
    TEST("04005AC33890", 54)
    TEST("880086C3E88112", 7)
    TEST("CE00C43D881120", 9)
    TEST("D8005AC2A8F0", 1)
    TEST("F600BC2D8F", 0)
    TEST("9C005AC2F8F0", 0)
    TEST("9C0141080250320F1802104A08", 1)

    print(f"PASSED {passed}/8")

    # Evaluate production input
    fdata = open("input.txt", 'r')
    packet = fdata.readline().rstrip()
    TEST(packet, 1495959086337)
    # result = evaluate_packet(packet)
    # print(f"Result: {result}")


    