from math import *
import numpy as np
import pygame

print("\nCube")

print("\nBy:  ViridianTelamon.")

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 600

pygame.display.set_caption("Cube")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

mouse_pressed = pygame.mouse.get_pressed()

mouse_x, mouse_y = pygame.mouse.get_pos()

mouse_position = (mouse_x, mouse_y)

scale = 100

position = [WIDTH / 2, HEIGHT / 2]

axis = 0

points = []

points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [
    [i, i] for i in range(len(points))
]

def connect_points(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

def rotation(x, y):
    rotation_matrix = np.dot(rotation_z, point.reshape((x, y)))

    rotation_matrix = np.dot(rotation_y, rotation_matrix)

frame = pygame.time.Clock()

while True:

    frame.tick(60)

    new_mouse_position = mouse_position

    new_mouse_x, new_mouse_y = pygame.mouse.get_pos()

    mouse_position_difference = (new_mouse_position[0] - mouse_position[0], new_mouse_position[1] - mouse_position[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
                exit()
    
    rotation_z = np.matrix([
        [cos(axis), -sin(axis), 0],
        [sin(axis), cos(axis), 0],
        [0, 0, 1]
    ])

    rotation_y = np.matrix([
        [cos(axis), 0, sin(axis)],
        [0, 1, 0],
        [sin(axis), 0, cos(axis)]
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(axis), -sin(axis)],
        [0, sin(axis), cos(axis)]
    ])


    axis += 0.01
                
    screen.fill(WHITE)

    j = 0

    for point in points:
        rotation_matrix = np.dot(rotation_z, point.reshape((3, 1)))

        rotation_matrix = np.dot(rotation_y, rotation_matrix)

        projected_matrix = np.dot(projection_matrix, rotation_matrix)

        x = int(projected_matrix[0][0] * scale) + position[0]

        y = int(projected_matrix[1][0] * scale) + position[1]

        projected_points[j] = [x, y]

        pygame.draw.circle(screen, BLACK, (x, y), 0.01)

        j += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = new_mouse_x

            mouse_y = new_mouse_y

            if mouse_x > mouse_y:
                mouse_position_difference = mouse_x - mouse_y
            elif mouse_y > mouse_x:
                mouse_position_difference = mouse_y - mouse_x
            else:
                mouse_position_difference = mouse_position_difference

            axis = mouse_position_difference

    for t in range(4):
        connect_points(t, (t + 1) % 4, projected_points)
        connect_points(t + 4, ((t + 1) % 4) + 4, projected_points)
        connect_points(t, (t + 4), projected_points)
    
    pygame.display.update()