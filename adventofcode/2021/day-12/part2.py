#! /usr/sbin/env python3

max_allowed_count_on_stack = 2

def aggregate_small(list):
    """
    Aggregate all lowercase nodes on stack
    """
    pairs = {}
    for i in list:
        if i not in pairs:
            if i.islower():
                pairs[i] = 0
        if i.islower():
            pairs[i] = pairs[i] + 1

    return pairs


def is_something_twice(list):
    """
    Aggregate list and return True if some value is greater
    or equal to max_allowed_count_on_stack.
    """
    aggregated = aggregate_small(list)
    for c in aggregated:
        if aggregated[c] >= max_allowed_count_on_stack:
            return True

    return False


def is_node_twice(list, node):
    """
    Aggregate list and return True if some value is greater
    or equal to max_allowed_count_on_stack.
    """
    aggregated = aggregate_small(list)
    for c in aggregated:
        if aggregated[c] >= max_allowed_count_on_stack and c == node:
            return True

    return False


def recursive(level, node, current_closed):
    closed = current_closed.copy()

    if node.isupper():
        rstack.append(node)

    # Node is on stack, but only once, so now it will be twice, co
    # all other small nodes on stack will be added to closed.
    elif is_something_twice(rstack) is False and node in rstack:
        # add this node second time to stack
        rstack.append(node)
        for n in aggregate_small(rstack):
            if n not in closed:
                closed.append(n)

    # Nothing is twice yet and current node is not yet on stack
    elif is_something_twice(rstack) is False and node not in rstack:
        rstack.append(node)

    elif is_something_twice(rstack) is True and node not in rstack:
        rstack.append(node)
        closed.append(node)

    if node == "end":
        print(level, ">> Found path", rstack)
        global global_counter
        global_counter += 1
        rstack.pop()
        return

    for next in graph[node]:
        if next not in closed:
            recursive(level+1, next, closed)

    # Remove this node from stack, if following paths are blind
    rstack.pop()


if __name__ == "__main__":
    # fdata = open("input1.txt", 'r')
    # fdata = open("input_19.txt", 'r')
    # fdata = open("input_226.txt", 'r')
    fdata = open("input.txt", 'r')

    # Init graph nodes and connect them in both directions
    graph = {}
    for line in fdata:
        conn = line.rstrip().split('-')
        if conn[0] not in graph:
            graph[conn[0]] = []
        if conn[1] not in graph:
            graph[conn[1]] = []
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])

    print(graph)

    global_counter = 0
    outer_closed = ["start"]
    rstack = []
    recursive(1, "start", outer_closed.copy())

    print("Number of paths:", global_counter)







