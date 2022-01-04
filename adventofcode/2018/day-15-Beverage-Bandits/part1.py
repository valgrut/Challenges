from dataclasses import dataclass        
import math
import copy
import random

@dataclass
class Entity:
    x: int = 0
    y: int = 0
    c: str = '.'
    attack: int = 3
    hp: int = 200
    
    def coords(self):
        return (self.x, self.y)

def drawmap(map):
    for line in map:
        for c in line:
            print(c, end='')
        print()
    print()


def mark_path(renderedmap, path):
    # for node in path:

    # Mark everything from starting and target location
    for node in path[1:-1]:
        renderedmap[node[0]][node[1]] = 'x'
    # drawmap(renderedmap)


def distance(adj_node, destination):
    # return abs(adj_node[0] - destination.x) + abs(adj_node[1] - destination.y)
    return math.sqrt((adj_node[0] - destination.x)**2 + (adj_node[1] - destination.y)**2)


def BFS(renderedmap, source, destination) -> list:
    """
    returns path between start and destination

    if path is [], no path leads from src to dst.
    """

    open = []
    closed = []
    open.append([source.coords()])
    while len(open) > 0:
        current_path = open.pop(0)
        exploding_node = current_path[-1]
        closed.append(exploding_node)
        
        adjacent_nodes = [(exploding_node[0]-1, exploding_node[1]), (exploding_node[0]+1, exploding_node[1]), (exploding_node[0], exploding_node[1]-1), (exploding_node[0], exploding_node[1]+1)]

        # For each adjacent node
        for adjacent_node in adjacent_nodes:

            # If adjacent_node is Visited
            if adjacent_node in closed:
                continue
            
            # Do not wait until this node is exploded, mark is as added to open now.
            closed.append(adjacent_node)

            new_path = copy.deepcopy(current_path)

            # Check, if some adjacent tile is destination tile.
            if adjacent_node[0] == destination.x and adjacent_node[1] == destination.y:
                new_path.append(adjacent_node)
                return new_path

            # Check that new node is not already in current path (looping)
            if adjacent_node in current_path:
                continue
            
            # Check that adjacent node is not Unit or Wall
            if renderedmap[adjacent_node[0]][adjacent_node[1]] in ['#', 'E', 'G']:
                continue

            # This adjacent_node is not already in path, so we can append it to end.
            new_path.append(adjacent_node)

            # Adjacent node (adjacent_node) is OK
            open.append(new_path)

    return []


if __name__ == "__main__":
    fdata = open("input.txt", 'r')
    # fdata = open("input1.txt", 'r')

    entities = []
    map = []
    # Init map and entities
    for i, line in enumerate(fdata):
        line = line.rstrip()
        map_row = []
        for j, c in enumerate(line):
            if c != '#' and c != '.':
                map_row.append('.')
                newentity = Entity()
                newentity.c = c
                newentity.x = i
                newentity.y = j
                newentity.hp = 200
                newentity.attack = 3
                entities.append(newentity)
            else:
                map_row.append(c)
        map.append(map_row)
    
    # draw entities to map (copy empty map and draw entities to that map according to if they are alive or not)
    # analyze map - neighbours of current entity
    # find shortest path to enemies, and find, which one is closest
    # And if some are same distance, pick one according to directions (top, bottom, left, right)

    # Game loop
    allkilled = False
    turn = 0
    while allkilled is False:
        # Make a copy of map, to which we will render entities
        rendermap = copy.deepcopy(map)
        
        # Draw entities to the copy of original map
        for entity in entities:
            if entity.hp > 0:
                rendermap[entity.x][entity.y] = entity.c
        
        # imove = random.randrange(0, len(entities))
        # entities[imove].x += 1
        
        drawmap(rendermap)
        if input() == "e": 
            break
        turn += 1
    
    # BFS test
    path = BFS(rendermap, entities[5], entities[16])
    drawmap(rendermap)
    mark_path(rendermap, path)
    drawmap(rendermap)
    
