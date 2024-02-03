import numpy as np
import pygame
import sys

# Initialize pygame
pygame.init()

# Grid dimensions
width, height = 400, 400
# Size of each cell
cell_size = 2

# Colors
bg_color = (50, 50, 50)
sand_color = (204, 192, 79)

# Create the grid
grid_width, grid_height = width // cell_size, height // cell_size
grid = np.zeros((grid_height, grid_width), dtype=np.uint8)

# Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Falling Sand Simulator')

def draw_grid():
    for y in range(grid_height):
        for x in range(grid_width):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
            if grid[y, x] == 1:
                pygame.draw.rect(screen, sand_color, rect)
            else:
                pygame.draw.rect(screen, bg_color, rect)

def update_grid():
    for y in range(grid_height-2, -1, -1):  # Start from the second last row
        for x in range(grid_width):
            if grid[y, x] == 1 and grid[y+1, x] == 0:
                grid[y, x] = 0
                grid[y+1, x] = 1

def place_sand(pos):
    x, y = pos
    grid[y // cell_size, x // cell_size] = 1

# Main loop
running = True
mouse_down = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

    if mouse_down:
        place_sand(pygame.mouse.get_pos())

    update_grid()
    screen.fill(bg_color)
    draw_grid()
    pygame.display.flip()
    pygame.time.wait(10)  # Slow down the simulation

pygame.quit()
sys.exit()
