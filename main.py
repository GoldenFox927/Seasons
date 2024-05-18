import pygame
import pyscroll
from pytmx.util_pygame import load_pygame
from entity.hero import Hero


class Game:
    def __init__(self) -> None:
        # ____ initialization ____ #
        pygame.init()

        # Set window size
        width = 1200
        height = 900
        self.window = pygame.display.set_mode((width, height))

        tmx_data = load_pygame("test.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (width, height))
        
        map_layer.zoom = 3
        
        # Create map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)

        # Create hero
        self.hero = Hero("Hero", 100, 100, [100, 100])
        self.group.add(self.hero)

    def run(self):
        # _____ Main game loop _____ #
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update all
            self.group.update()

            # Draw the map
            self.group.draw(self.window)

            # Update the display
            pygame.display.flip()

        # ____ Quit Pygame ____ #
        pygame.quit()

Game().run()