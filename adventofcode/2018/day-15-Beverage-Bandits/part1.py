from dataclasses import dataclass        
import math
import copy
import random
import numpy

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
    return math.sqrt((adj_node[0] - destination[0])**2 + (adj_node[1] - destination[1])**2)


def BFS_u(renderedmap, source, destination) -> list:
    path = BFS(renderedmap, source.coords(), destination.coords())
    return path


def BFS(renderedmap, source_coords, destination_coords) -> list:
    """
    coords bfs
    returns path between start and destination

    if path is [], no path leads from src to dst.
    """

    open = []
    closed = []
    open.append([source_coords])
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
            if adjacent_node[0] == destination_coords[0] and adjacent_node[1] == destination_coords[1]:
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


def enemyof(unit):
    if unit.c == "E":
        return "G"
    return "E"


def identify_targets(map, units, active_unit):
    possible_targets = []
    for unit in units:
        if unit.hp <= 0:
            continue
        if unit.c == enemyof(active_unit) and unit != active_unit:
            if len(BFS_u(map, active_unit, unit)):
                possible_targets.append(unit)
    
    return possible_targets


def identify_open_squares(map, targets, active_unit):
    opened_squares = []
    for target in targets:
        if map[target.x-1][target.y] not in ['E', 'G', '#'] or (target.x-1, target.y) == active_unit.coords(): 
            opened_squares.append((target.x-1,target.y))
        if map[target.x+1][target.y] not in ['E', 'G', '#'] or (target.x+1, target.y) == active_unit.coords():
            opened_squares.append((target.x+1,target.y))
        if map[target.x][target.y-1] not in ['E', 'G', '#'] or (target.x, target.y-1) == active_unit.coords(): 
            opened_squares.append((target.x,target.y-1))
        if map[target.x][target.y+1] not in ['E', 'G', '#'] or (target.x, target.y+1) == active_unit.coords():
            opened_squares.append((target.x,target.y+1))
    return opened_squares


def identify_reachable_squares(rendermap, squares_in_range, active_unit):
    reachable_squares = []
    for square in squares_in_range:
        if len(BFS(rendermap, active_unit.coords(), square)):
            if square not in reachable_squares:
                reachable_squares.append(square)

    return reachable_squares


def identify_closest_square(rendermap, reachable_squares, active_unit):
    if not reachable_squares:
        return []

    reachable_squares_paths = []
    for square in reachable_squares:
        path = BFS(rendermap, active_unit.coords(), square)
        reachable_squares_paths.append(path)

    reachable_squares_paths.sort(key=lambda path: len(path))

    return reachable_squares_paths[0]



def battle(map_file):
    fdata = open(map_file, 'r')

    units = []
    map = []
    # Init map and units
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
                units.append(newentity)
            else:
                map_row.append(c)
        map.append(map_row)
    
    # draw units to map (copy empty map and draw units to that map according to if they are alive or not)
    # analyze map - neighbours of current entity
    # find shortest path to enemies, and find, which one is closest
    # And if some are same distance, pick one according to directions (top, bottom, left, right)

    # Game loop
    allkilled = False
    turn = 0
    while allkilled is False:
        # print("Turn:",turn)
        # Sort objects to reflect their positions from top to bottom and from left to right
        units.sort(key=lambda unit: (unit.x, unit.y))
        
        # Each Unit will take a turn
        for active_unit in units:
            if active_unit.hp <= 0:
                continue
            # print("active_unit:",active_unit.c, active_unit.coords(), "HP:",active_unit.hp)
            # Make a copy of map, to which we will render units
            rendermap = copy.deepcopy(map)
            
            # Draw units to the copy of original map
            for entity in units:
                if entity.hp > 0:
                    rendermap[entity.x][entity.y] = entity.c
            
            # Identify all enemy targets
            targets = identify_targets(rendermap, units, active_unit)
            # print("possible targets:",targets)
            if not targets:
                continue
            
            # Identify reachable open squares around each target
            in_range = identify_open_squares(rendermap, targets, active_unit)
            # print("open squares:",in_range)
            if not in_range:
                continue
            
            path = []
            reachable_squares = []
            # print("coords, range", active_unit.coords(), in_range)
            # active unit is not in target's open square yet
            if active_unit.coords() not in in_range:
                # Identify, which of opened squares are reachable by active_unit
                reachable_squares = identify_reachable_squares(rendermap, in_range, active_unit)
                if not reachable_squares:
                    continue
            
                # Get path to closest square of enemy
                path = identify_closest_square(rendermap, reachable_squares, active_unit)
                
            # print(len(path), path)
            if len(path) > 0:
                active_unit.x = path[1][0]
                active_unit.y = path[1][1]
                rendermap[path[-1][0]][path[-1][1]] = 'x'
            
            # Attack all adjacent enemies
            if len(path) == 0:
                # print("unit already in range of enemy, dont move, ATTACK!")
                adjacent_enemies = []
                for enemy in units:
                    if enemy.hp > 0:
                        if (enemy.x+1 == active_unit.x and enemy.y == active_unit.y) or\
                        (enemy.x-1 == active_unit.x and enemy.y == active_unit.y) or\
                        (enemy.x == active_unit.x and enemy.y+1 == active_unit.y) or\
                        (enemy.x == active_unit.x and enemy.y-1 == active_unit.y):
                            if enemy.c == enemyof(active_unit):
                                adjacent_enemies.append(enemy)
                adjacent_enemies.sort(key=lambda enemy: (enemy.hp, enemy.x, enemy.y))
                if len(adjacent_enemies):
                    adjacent_enemies[0].hp -= active_unit.attack
                
                # Chech if some side won
                elfs_alive = sum(1 for i in units if i.hp > 0 and i.c == 'E')
                goblins_alive = sum(1 for i in units if i.hp > 0 and i.c == 'G')
                if elfs_alive == 0:
                    # print("Turn", turn, "Goblins won!")
                    goblins_hp = [i.hp for i in units if i.hp > 0 and i.c == 'G']
                    # print("Goblin HPs", goblins_hp, ", prod:", sum(goblins_hp))
                    return (goblins_hp, sum(goblins_hp), turn, turn*sum(goblins_hp))
                    # exit(0)
                elif goblins_alive == 0:
                    # print("Turn", turn, "Elves won!")
                    elves_hp = [i.hp for i in units if i.hp > 0 and i.c == 'E']
                    # print("Elves HPs", elves_hp, ", prod:", sum(elves_hp))
                    return (elves_hp, sum(elves_hp), turn, turn*sum(elves_hp))
                    # exit(0)
            
        # drawmap(rendermap)
        
        # if input() == "e": 
            # break
        
        turn += 1

if __name__ == "__main__":
    # fdata = open("input.txt", 'r')
    # fdata = open("input1.txt", 'r')
    fdata = open("input2.txt", 'r')
    # fdata = open("input3.txt", 'r')
    initial_map = open("input2.txt", 'r')

    result = battle("input1.txt")
    result = battle("input2.txt") # [], 590, 47, 27730
    print(result)
    result = battle("input3.txt") # [], 982, 37, 36334
    print(result)
    result = battle("input4.txt") # [], 859, 46, 39514
    print(result)
    result = battle("input5.txt") # [], 793, 35, 27755
    print(result)
    result = battle("input6.txt") # [], 536, 54, 28944
    print(result)
    result = battle("input7.txt") # [], 937, 20, 18740
    print(result)

    # TODO: jediny problem, ze nekde je o 1-2 utoky vice, tim i obcas o kolo vice.

    result = battle("input.txt") #
    print(result)


