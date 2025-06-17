
import pygame
import random

pygame.init()

# Setup
width, height = 600, 400
block = 20
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Snake
x = width // 2
y = height // 2
x_change = 0
y_change = 0
snake = []
length = 1

# Food
foodx = random.randint(0, width - block) // block * block
foody = random.randint(0, height - block) // block * block

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = block
                x_change = 0

    x += x_change
    y += y_change

    if x < 0 or x >= width or y < 0 or y >= height:
        running = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (foodx, foody, block, block))

    head = [x, y]
    snake.append(head)
    if len(snake) > length:
        del snake[0]

    for segment in snake:
        pygame.draw.rect(win, (255, 255, 255), (segment[0], segment[1], block, block))

    if x == foodx and y == foody:
        foodx = random.randint(0, width - block) // block * block
        foody = random.randint(0, height - block) // block * block
        length += 1

    pygame.display.update()
    clock.tick(10)

pygame.quit()
