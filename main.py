import pygame
from entity.hero import Hero

# ____ initialization ____ #
pygame.init()

# Set window size
width = 800
height = 600
window = pygame.display.set_mode((width, height))

# Create hero
hero = Hero("Hero", 100, 100, (width // 2, height // 2))

# _____ Main game loop _____ #
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Move the hero
    hero.move()
        
    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the hero
    hero.draw(window)

    # Update the display
    pygame.display.flip()

# ____ Quit Pygame ____ #
pygame.quit()