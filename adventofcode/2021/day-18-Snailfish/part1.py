import math

def list_to_string(lst) -> str:
    """
    Transform list of characters to string.
    """
    return ''.join(map(str, lst))


class Node():
    def __init__(self) -> None:
        self.parent = None
        self.left = None
        self.right = None


def traverse_tree(root) -> None:
    """
    Print tree using left first traversion.
    """
    current = root

    if isinstance(current.left, Node):
        traverse_tree(current.left)
    else:
        # left is not instance of Node, so print value.
        print(current.left)

    if isinstance(current.right, Node):
        traverse_tree(current.right)
    else:
        # left is not instance of Node, so print value.
        if current.right is not None:
            print(current.right)


def string_to_tree(data_str) -> Node:
    """
    Transform input string data into Tree representation.
    """
    root_node = Node()

    current_node = root_node
    side_stack = ["left"]
    for ch in data_str:
        # print("ch:", ch)
        if ch == "[":
            new_node = Node()
            if side_stack[-1] == "left":
                current_node.left = new_node
            else:
                current_node.right = new_node
            new_node.parent = current_node
            current_node = new_node

            # Push new nesting node marker
            side_stack.append("left")
        
        if ch == ',':
            side_stack[-1] = "right"

        if ch.isnumeric():
            if side_stack[-1] == "left":
                if current_node.left is None:
                    current_node.left = int(ch)
                else:
                    current_node.left = int(str(current_node.left) + ch)
            else:
                if current_node.right is None:
                    current_node.right = int(ch)
                else:
                    current_node.right = int(str(current_node.right) + ch)
        
        if ch == "]":
            current_node = current_node.parent
            side_stack.pop()

    return root_node


def tree_to_str(tree_root, result_string):
    """
    Transform input tree into string representation.
    """
    current = tree_root
    
    if isinstance(current.left, Node):
        result_string.append("[")
        tree_to_str(current.left, result_string)
        result_string.append("]")
    else:
        result_string.append(str(current.left))

    # Don't put ',' after last closing ']'.
    if current.right is not None:
        result_string.append(",")
    
    if isinstance(current.right, Node):
        result_string.append("[")
        tree_to_str(current.right, result_string)
        result_string.append("]")
    else:
        if current.right is not None:
            result_string.append(str(current.right))


def TEST_reset():
    global passed
    global failed
    passed = 0
    failed = 0


def TEST(input_string, expected):
    global passed
    global failed
    tree_root = string_to_tree(input_string)
    
    reconstructed_string = []
    tree_to_str(tree_root, reconstructed_string)

    return_value = list_to_string(reconstructed_string)

    if return_value != expected:
        failed += 1
        print(f"[FAIL]: {return_value} is not equal {expected}") # (input: {input_string})")
    else:
        passed += 1
        print(f"[PASS]: {return_value} is equal {expected}") # (input: {input_string})")


def find_closest_left_value(previous, current, expl_left_value):
    """
    Find and return first node to add right number of exploded node to the left
    number of the found node.
    """
    # Going UP to the root
    if current.left == previous:
        #print("minuly node je nalevo, jdu do parenta UP.")
        
        if current.parent is not None:
            find_closest_left_value(current, current.parent, expl_left_value)
        else:
            #print("Po leve strane stromu nebylo nalezeno vhodne misto.")
            return

    # Going up to the root
    # Jdeme z prave vetve do leve. Mozna prelezem pres root, pak ale jdeme nahoru, viz 3.
    elif current.right == previous:
        #print("Minuly node byl NAPRAVO, takze mohu jit doleva")
        if isinstance(current.left, Node):
            find_closest_left_value(current, current.left, expl_left_value)
            # UP to the right viz 3. 
        else:
            #print("found")
            current.left += expl_left_value
        return

    # ad 3. Jdeme od root dolu co nejvic doleva
    elif previous.left == current:
        if isinstance(current.right, Node):
            find_closest_left_value(current, current.right, expl_left_value)
            # UP to the right viz 2. 
        else:
            #print("found")
            current.right += expl_left_value
        return

    # ad 2. Jdeme od root dolu co nejvic doprava (sli jsme do rootu z prave vetve do leve)
    elif previous.right == current:
        if isinstance(current.right, Node):
            find_closest_left_value(current, current.right, expl_left_value)
            # UP to the right viz 2. 
        else:
            #print("found")
            current.right += expl_left_value
        return


def find_closest_right_value(previous, current, expl_right_value):
    """
    Find and return first node to add left number of exploded node to the right
    number of the found node.
    """
    # Going UP to the root
    if current.right == previous:
        # print("minuly node je vpravo, jdu do parenta UP.")
        
        if current.parent is not None:
            find_closest_right_value(current, current.parent, expl_right_value)
        else:
            # print("Po prave strane stromu nebylo nalezeno vhodne misto.")
            return

    # Going up to the root
    # Jdeme z prave vetve do leve. Mozna prelezem pres root, pak ale jdeme nahoru, viz 3.
    elif current.left == previous:
        #print("Minuly node byl NAPRAVO, takze mohu jit doleva")

        # fix pro pravou stranu
        if current.parent is None:
            # print("Po prave strane stromu nebylo nalezeno vhodne misto.")
            return

        if isinstance(current.right, Node):
            find_closest_right_value(current, current.right, expl_right_value)
            # UP to the right viz 3. 
        else:
            current.right += expl_right_value
        return

    # ad 3. Jdeme od root dolu co nejvic doleva
    elif previous.right == current:
        if isinstance(current.left, Node):
            find_closest_right_value(current, current.left, expl_right_value)
            # UP to the right viz 2. 
        else:
            #print("found")
            current.left += expl_right_value
        return

    # ad 2. Jdeme od root dolu co nejvic doprava (sli jsme do rootu z prave vetve do leve)
    elif previous.left == current:
        if isinstance(current.left, Node):
            find_closest_right_value(current, current.left, expl_right_value)
            # UP to the right viz 2. 
        else:
            #print("found")
            current.left += expl_right_value
        return


def find_leftmost_value(root):
    """
    Find leftmost value for magnitude calculation
    """
    ret = -1
    if isinstance(root.left, Node):
        ret = find_leftmost_value(root.left)
    else:
        ret = root.left

    return ret


def find_rightmost_value(root):
    """
    Find rightmost value for magnitude calculation
    """
    ret = -1
    if isinstance(root.right, Node):
        ret = find_rightmost_value(root.right)
    else:
        ret = root.right

    return ret


def find_split_value(root_tree) -> Node:
    """
    Find and return first value greater than 9, that will be split up and new
    node will be created from this splitted value.
    """
    current = root_tree
    found = None

    if isinstance(current.left, Node):
        found = find_split_value(current.left)
        if found is not None:
            return found
    else:
        # left is not instance of Node, so print value.  
        if current.left is not None:
            # print(current.left)
            if current.left > 9:
                # print(f"Found, {current.left}")
                return current

    if isinstance(current.right, Node):
        found = find_split_value(current.right)
        if found is not None:
            return found
    else:
        # left is not instance of Node, so print value.
        if current.right is not None:
            # print(current.right)
            if current.right > 9:
                # print(f"Found, {current.right}")
                return current
    
    return found


def find_exploding_pair(root_tree, depth) -> Node:
    """
    Find and return first node in depth greater than 4.
    """
    current = root_tree
    found = None
    # This is leaf pair AND is nested in 4 or more depth
    if  not isinstance(current.left, Node) and not isinstance(current.left, Node) and depth > 4:
        return current

    if isinstance(current.left, Node):
        found = find_exploding_pair(current.left, depth + 1)
        if found is not None:
            return found
    else:
        # left is not instance of Node, so print value.
        # print(current.left)
        pass

    if isinstance(current.right, Node):
        found = find_exploding_pair(current.right, depth + 1)
        if found is not None:
            return found
    else:
        # left is not instance of Node, so print value.
        if current.right is not None:
            #print(current.right)
            pass
    
    return found


def split_node_value(node):
    if node is not None:
        if not isinstance(node.left, Node):
            if node.left > 9:
                new_node = Node()
                new_node.parent = node
                new_node.left = math.floor(node.left / 2)
                new_node.right = math.ceil(node.left / 2)
                node.left = new_node
                return

        if not isinstance(node.right, Node):
            if node.right > 9:
                new_node = Node()
                new_node.parent = node
                new_node.left = math.floor(node.right / 2)
                new_node.right = math.ceil(node.right / 2)
                node.right = new_node
                return

def reduce_tree(root_tree):
    """
    Reduce given tree until no operaton can be used.
    """

    # Until no reduction rule can be applied
    reduced = False
    while not reduced:
        # [Explode]
        can_explode = find_exploding_pair(root_tree, 0)
        while can_explode is not None:
            # print(f"Exploding {can_explode.left}, {can_explode.right}")
            explode_parent = can_explode.parent
            # - find first left value from exploding node and add left number
            find_closest_left_value(can_explode, explode_parent, can_explode.left)
            
            # - find first right value from exploding node and add right number
            find_closest_right_value(can_explode, explode_parent, can_explode.right)

            # - remove child from left or right position in parent node
            if explode_parent.left == can_explode:
                explode_parent.left = 0
            if explode_parent.right == can_explode:
                explode_parent.right = 0

            # Find another exploding pair
            can_explode = find_exploding_pair(root_tree, 0)

        # [Split]
        # If some number can be split (is > 9)
        can_split = find_split_value(root_tree)
        if can_split is not None:
            # print("Splitting")
            split_node_value(can_split)

        if can_explode is None and can_split is None:
            reduced = True
            return root_tree


def add_numbers(number1, number2):
    """
    numbers in string format (i.e. "[[2,[2,2]],[8,[8,1]]]")

    Add 2 numbers together.
    
    Creates a string with [number1,number2] and convert this to tree.
    Then starts with explode,split routine, until none of them can be applied.

    Returns summed and reducted number.
    """

    summed_string = '[' + number1 + ',' + number2 + ']'
    tree_root = string_to_tree(summed_string)

    # Reductions
    reduce_tree(tree_root)
    # TODO: maybe check, if both input numbers are reducted.

    reconstructed_string = []
    tree_to_str(tree_root, reconstructed_string)
    return_value = list_to_string(reconstructed_string)

    return return_value


# TODO: 4. Implementovat find leftmost a find rightmost pro vypocet magnitude.
# TODO: 5. vypocet magnitude


if __name__ == "__main__":
    global passed
    global failed
    passed = 0
    failed = 0

    print("Testing part 1")
    fdata = open("input1.txt", 'r')

    sum = fdata.readline().rstrip()
    for line in fdata:
        line = line.rstrip()
        # TEST(line, line)

        print("adding:")
        print("sum ", sum)
        print("line", line)
        sum = add_numbers(sum, line)

    # Calculate magnitude
    # TODO

    # Expected result for "input1.txt"
    TEST(sum, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

    print("")
    print(f"PASSED: {passed}/{passed+failed}")
    print(f"FAILED: {failed}/{passed+failed}")
    print("")
     
    # Testing
    print("")
    print("Testing part 2")
    TEST(add_numbers("[[6,[2,[4,2]]],[8,7]]", "[6,3]"), "[[[6,[6,0]],[[5,5],7]],[6,3]]")
    TEST(add_numbers("[[6,[[4,2],2]],[8,7]]", "[6,3]"), "[[[[5,5],[0,4]],[8,7]],[6,3]]")    
    TEST(add_numbers("[[[2,[4,2]],6],[8,7]]", "[6,3]"), "[[[[6,0],8],[8,7]],[6,3]]")
    TEST(add_numbers("[[[[4,2],2],6],[8,7]]", "[6,3]"), "[[[[0,4],6],[8,7]],[6,3]]")
    TEST(add_numbers("[[[[4,2],9],6],[8,7]]", "[6,3]"), "[[[[5,0],[6,6]],[8,7]],[6,3]]")

    # Testing of Examples
    print("")
    print("Testing part 3 - testing of examples")
    TEST(add_numbers("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"), "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

    sum = add_numbers("[1,1]", "[2,2]")
    sum = add_numbers(sum, "[3,3]")
    sum = add_numbers(sum, "[4,4]")
    TEST(sum, "[[[[1,1],[2,2]],[3,3]],[4,4]]")

    sum = add_numbers("[1,1]", "[2,2]")
    sum = add_numbers(sum, "[3,3]")
    sum = add_numbers(sum, "[4,4]")
    sum = add_numbers(sum, "[5,5]")
    TEST(sum, "[[[[3,0],[5,3]],[4,4]],[5,5]]")

    sum = add_numbers("[1,1]", "[2,2]")
    sum = add_numbers(sum, "[3,3]")
    sum = add_numbers(sum, "[4,4]")
    sum = add_numbers(sum, "[5,5]")
    sum = add_numbers(sum, "[6,6]")
    TEST(sum, "[[[[5,0],[7,4]],[5,5]],[6,6]]")

    print()
    TEST(add_numbers("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"), "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
    TEST(add_numbers("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]", "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]"), "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")
    TEST(add_numbers("[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]", "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"), "[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]")
    TEST(add_numbers("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]", "[7,[5,[[3,8],[1,4]]]]"), "[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
    TEST(add_numbers("[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]", "[[2,[2,2]],[8,[8,1]]]"), "[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]")
    TEST(add_numbers("[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]", "[2,9]"), "[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]")
    TEST(add_numbers("[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]", "[1,[[[9,3],9],[[9,0],[0,7]]]]"), "[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]")

