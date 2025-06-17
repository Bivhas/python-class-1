import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Mario")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player variables
player_width = 40
player_height = 60
player_x = 50
player_y = HEIGHT - player_height - 50  # Start on ground
player_vel_x = 0
player_vel_y = 0
gravity = 0.8
jump_strength = -15
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),          # ground
    pygame.Rect(200, HEIGHT - 150, 120, 20),         # floating platform 1
    pygame.Rect(450, HEIGHT - 220, 150, 20),         # floating platform 2
]

player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key pressed
    keys = pygame.key.get_pressed()
    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -5
    if keys[pygame.K_RIGHT]:
        player_vel_x = 5
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_strength
        on_ground = False

    # Apply gravity
    player_vel_y += gravity
    player_rect.x += player_vel_x
    player_rect.y += player_vel_y

    # Collision detection
    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            # Check if falling on top of platform
            if player_vel_y > 0 and player_rect.bottom <= platform.top + player_vel_y:
                player_rect.bottom = platform.top
                player_vel_y = 0
                on_ground = True
            # Prevent going through sides of platforms
            elif player_vel_x > 0:
                player_rect.right = platform.left
            elif player_vel_x < 0:
                player_rect.left = platform.right

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
