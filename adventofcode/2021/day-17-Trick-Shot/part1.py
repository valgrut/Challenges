
def is_hit(coords, target_area):
    return True if coords[0] in target_area[0] and coords[1] in target_area[1] else False

def shoot(initial_position, initial_velocity, target_area):
    pos_x = initial_position[0]
    pos_y = initial_position[1]
    velocity_x = initial_velocity[0]
    velocity_y = initial_velocity[1]

    highest_point = 0
    max_steps = 200
    step = 0
    hit = False
    while hit is False:
        if highest_point < pos_y:
            highest_point = pos_y

        # Calculate change of coords and velocity
        pos_x += velocity_x
        pos_y += velocity_y

        if velocity_x > 0:
            velocity_x -= 1
        if velocity_x < 0: 
            velocity_x += 1
        
        velocity_y -= 1
        
        # Check hit
        if is_hit((pos_x, pos_y), target_area):
            print(f"HIT! vel=({initial_velocity[0]}, {initial_velocity[1]}), hpoint: {highest_point}")
            hit = True

            if highest_point < pos_y:
                highest_point = pos_y

            return highest_point
        
        step += 1

        if step > max_steps:
            # print("Terminated (max_steps)")
            return -1
    
    return False


if __name__ == "__main__":
    # What can be modified:
    # - max_steps in shoot function (200 seems sufficient)
    # TODO: Could be changed that if x is below target_x and y 
    # is below target_y, break.
    # - bruteforce value (200) in loop and nested loop
    
    # Example input
    # target_area = ([i for i in range(20, 30 + 1)], [i for i in range(-10, -5 +1)])
    
    # Real input
    target_area = ([i for i in range(241, 273 + 1)], [i for i in range(-97, -63 +1)])

    # Initial position
    pos_x = 0
    pos_y = 0

    velocity_x = 6
    velocity_y = 9

    # highest_point = shoot((pos_x, pos_y), (velocity_x, velocity_y), target_area)

    # A little bruteforce cant be harmful...
    highest_point_overall = 0
    for vx in range(0, 200):
        for vy in range(-200, 200):
            highest_point = shoot((pos_x, pos_y), (vx, vy), target_area)
            if highest_point > highest_point_overall:
                highest_point_overall = highest_point
            
    print(f"Highest point overall: {highest_point_overall}")
