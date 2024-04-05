import pygame

# Pygame initialization
pygame.init()

# Set window size
width = 800
height = 600
window = pygame.display.set_mode((width, height))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
