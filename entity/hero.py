import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, health, mana, position=[0, 0]):
        super().__init__()
        self.name = name
        self.health = health
        self.mana = mana
        self.position = position
        self.speed = 0.1
        self.movement = [0, 0]
        self.orientation = "right"
        self.position = pygame.Vector2(position[0], position[1])  # Initial position

        # Load the spritesheet
        self.sprite_sheet = pygame.image.load(
            "assets/graphism/playerSprites_\mPlayer_ [elf].png"
        )

        # Get the sprite from the sprite sheet
        self.image = self.get_image(0, 5)
        self.rect = self.image.get_rect()

    def get_image(self, x, y, reverse=False):
        image = pygame.Surface((12, 21))
        image.blit(self.sprite_sheet, (0, 0), (x*32+10, y*32+7, 12, 22))
        image = pygame.transform.flip(image, reverse, False)
        image.set_colorkey((0, 0, 0))
        return image

    def update(self):
        self.move()
        self.rect.topleft = self.position

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed
            self.image = self.get_image(0, 5, True)
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed
            self.image = self.get_image(0, 5)
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed
