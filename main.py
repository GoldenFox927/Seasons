import pyxel
from player import Player
from enemy import Enemy

class App:
    def __init__(self):
        pyxel.init(160, 120)  # Set the window size
        pyxel.load("resources.pyxres") # load the resources file

        self.player = Player("Brise", 1, 100, (0, 0)) # Create a player object
        self.ennemy = Enemy("Goblin", 1, 10, (0, 32), (16, 16)) # Create an enemy object
        self.ennemy.set_path("linear", [(0, 0), (160, 120)]) # Set the path for the enemy
        self.enemies = [self.ennemy] # Create a list of enemies

        pyxel.run(self.update, self.draw)  # Start the game loop

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): # Press Q to quit the game
            pyxel.quit()
        self.player.move()

    def draw(self):
        pyxel.cls(0)  # Clear the screen with color index 0
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120, 0)  # Draw the background
        
        # Draw the player
        pyxel.blt(
            self.player.pos()[0],
            self.player.pos()[1],
            0,
            self.player.get_sprite()[0],
            self.player.get_sprite()[1],
            8,
            8,
            2,
        )
        
        # Draw the enemies
        for enemy in self.enemies:
            pyxel.blt(
                enemy.pos()[0],
                enemy.pos()[1],
                0,
                enemy.get_sprite()[0],
                enemy.get_sprite()[1],
                8,
                8,
                2,
            )


if __name__ == "__main__":
    App()
