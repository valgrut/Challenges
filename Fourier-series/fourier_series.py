import pygame
import math
import random
import os

pygame.init()
os.environ['SDL_VIDEODRIVER'] = 'dummy'


# Coding Challenge: Fourier Series
#
# Author: Jiri Peska
# Description:
#   - Sum of specific frequency series will generate square signal.
#   - With Fourier series any function can be generated.
#
# Resources:
#   - https://bilimneguzellan.net/en/purrier-series-meow-and-making-images-speak/
#   - [The Coding Train - Coding Challenge #125: Fourier Series](https://www.youtube.com/watch?v=Mm2eYfj0SgA)
#   - [Guide to Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
#   - [Wikipedia - Fourier Transform](https://en.wikipedia.org/wiki/Fourier_series)


class RotatingCircle(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, radius=None, velocity=None, parent_node=None):
        pygame.sprite.Sprite.__init__(self)
        self.parent_node = None
        self.child_node = None
        self.current_x = pos_x
        self.current_y = pos_y
        self.radius = radius
        self.velocity = velocity

        if parent_node is not None:
            self.parent_node = parent_node
            parent_node.child_node = self

        self.update(0)

    def sync_pos_with_parent(self):
        if self.parent_node is not None:
            self.current_x = self.parent_node.end_point_pos[0]
            self.current_y = self.parent_node.end_point_pos[1]

    def update(self, delta_time):
        self.sync_pos_with_parent()

        self.end_point_pos = (
            self.current_x + self.radius * math.cos(self.velocity * delta_time),
            self.current_y + self.radius * math.sin(self.velocity * delta_time))

    def get_new_end_point_pos(self):
        """
        Get exact position of outermost circle node using parent's references.
        """
        if self.child_node is None:
            return self.end_point_pos
        else:
            return self.child_node.get_new_end_point_pos()

    def draw(self):
        # This circle
        pygame.draw.circle(screen, (255, 255, 255), (self.current_x, self.current_y), self.radius, 1)
        # Line from center to moving point
        pygame.draw.line(screen, (255, 255, 255), (self.current_x, self.current_y), self.end_point_pos)
        # Moving point
        pygame.draw.circle(screen, (255, 255, 255), self.end_point_pos, 5)



screen_width = 1400
screen_height = 1000

clock = pygame.time.Clock()
fps = 60

# screen definition
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(f"Fourier Series")

# Background initialization
background = pygame.Surface(screen.get_size())  # create surface for background
background.fill((15, 15, 15))  # fill the background (red,green,blue)
background = background.convert()  # convert surface for faster blitting

# Base circle values
size_scale_const = 100
base_circle_radius = size_scale_const * (4 / (1 * math.pi))
base_circle_position_x = screen_width // 4
base_circle_position_y = screen_height // 2

# Generate Fourier series - square signal.
# if n == 1, n += 2: Square signal
# if n == 2, n += 2: triangular signal
n = 1
num_of_sinusoids = 20  # Accuracy

circles = []
prev_circle = None
for i_children in range(1, num_of_sinusoids + 1):
    current_circle = None
    radius = (100 * (4 / (n * math.pi)))
    if prev_circle is None:
        current_circle = RotatingCircle(pos_x=base_circle_position_x, pos_y=base_circle_position_y, radius=radius, velocity=n, parent_node=None)
    else:
        current_circle = RotatingCircle(radius=radius, velocity=n, parent_node=prev_circle)
    circles.append(current_circle)
    prev_circle = current_circle
    # This n
    n += 2

# Graph plotting settings
graph_points = []
num_of_points_to_draw = 1000 * num_of_sinusoids
shift_speed = 1 / (num_of_sinusoids + 1)
playtime = 0
run = True

while run:
    clock.tick(fps)
    milliseconds = clock.tick(fps)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0  # seconds passed since last frame (float)
    playtime += seconds + 0.01  # increase an animation speed a bit by 0.005

    # Redraw Background
    screen.blit(background, (0, 0))

    for circle in circles:
        circle.update(playtime)
        circle.draw()

        end_point_pos = circle.get_new_end_point_pos()
        # we want only y coord
        end_point_pos_array = [0, end_point_pos[1]]
        if len(graph_points) < num_of_points_to_draw:
            graph_points.insert(0, end_point_pos_array)
        else:
            graph_points.pop()  # remove last item
            graph_points.insert(0, end_point_pos_array)

        for point in graph_points:
            point[0] += shift_speed  # shift all points right

    # Draw horizontal line between first point of graph and moving outermost circle node
    pygame.draw.line(screen, (255, 255, 255), end_point_pos, (base_circle_position_x + base_circle_radius * 2, graph_points[0][1]))

    # draw points of running graph
    for point in graph_points:
        pygame.draw.circle(screen, (255, 255, 255), (base_circle_position_x + base_circle_radius * 2 + point[0], point[1]), 2)

    # draw point lines of running graph
    for point in range(1, len(graph_points)-1):
        pygame.draw.line(screen, (255, 255, 255), (base_circle_position_x + base_circle_radius * 2 + graph_points[point][0], graph_points[point][1]), (base_circle_position_x + base_circle_radius * 2 + graph_points[point+1][0], graph_points[point+1][1]), 1)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

