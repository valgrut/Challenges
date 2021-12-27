class Node():
    def __init__(self) -> None:
        self.parent = None
        self.left = None
        self.right = None

# if left.isinstanceof(node) ...

def traverse_tree(root) -> None:
    """
    Write tree using left first
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


def find_right_leftmost_node(tree_root) -> Node:
    pass

def find_left_rightmost_node(tree_root) -> Node:
    pass

def string_to_tree(data_str) -> Node:
    root_node = Node()

    current_node = root_node
    side_stack = ["left"]
    for ch in data_str:
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
                current_node.left = int(ch)
            else:
                current_node.right = int(ch)
        
        if ch == "]":
            current_node = current_node.parent
            side_stack.pop()

    return root_node

def tree_to_str(tree_root, result_string):
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
    

def reduction(tree):
    """
    Reduce given tree until no operaton can be used.
    """
    pass

def list_to_string(lst):
    return ''.join(map(str, lst))

if __name__ == "__main__":
    
    fdata = open("input.txt", 'r')
    # for line in fdata:
    #     line = line.rstrip()
    #     root = string_to_tree(line)
    #     traverse_tree(root)

    data = "[[[[8,2],[6,5]],[4,[9,2]]],[[0,[2,6]],[6,6]]]"
    data = "[1,[[8,[9,5]],2]]"
    print("input", data)
    root = string_to_tree(data)
    traverse_tree(root)
    
    data_again = []
    tree_to_str(root, data_again)
    print("output", list_to_string(data_again))