#! /usr/sbin/env python3

if __name__ == "__main__":
    # fdata = open("input1.txt", 'r')
    fdata = open("input.txt", 'r')

    # Initiate graph nodes and connect them in both directions
    graph = {}
    for line in fdata:
        conn = line.rstrip().split('-')
        if conn[0] not in graph:
            graph[conn[0]] = []
        if conn[1] not in graph:
            graph[conn[1]] = []
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])

    global_counter = 0
    outer_closed = []
    rstack = []
    recursive(1, "start", outer_closed.copy())
    print("Number of paths:", global_counter)







