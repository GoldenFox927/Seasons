import pygame


class Hero:
    def __init__(self, name, health, mana, position=(0, 0)):
        self.name = name
        self.health = health
        self.mana = mana
        self.position = position
        self.speed = 0.1
        self.movement = [0, 0]
        self.orientation = "right"
        self.position = pygame.Vector2(position[0], position[1])  # Initial position

        # Load the sprite
        sprite_sheet = pygame.image.load(
            "assets\playerSprites_ [version 1.0]\mPlayer_ [elf].png"
        )

        # Define the rectangle for the area of the sprite sheet you want
        sprite_rect = pygame.Rect(
            32, 32, 32, 32
        )  # Change these values to the area you want

        # Get the sprite from the sprite sheet
        self.sprite = sprite_sheet.subsurface(sprite_rect)

        # Scale the sprite
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed
            if self.orientation == "right":
                self.orientation = "left"
                self.sprite = pygame.transform.flip(self.sprite, True, False)
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed
            if self.orientation == "left":
                self.orientation = "right"
                self.sprite = pygame.transform.flip(self.sprite, True, False)
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed

    def draw(self, window):
        window.blit(self.sprite, self.position)
