import pyxel
from player import Player
from enemy import Enemy

class App:
    def __init__(self):
        pyxel.init(160, 120)  # Set the window size
        pyxel.load("resources.pyxres") # load the resources file

        self.player = Player("Brise", 1, 100, (0, 0)) # Create a player object
        
        self.enemies = []
        
        for x in range(16):
            for y in range(16):
                tile = self.get_tile(x, y)
                print(tile)
                if tile == (0, 4):
                    self.enemies.append(Enemy("Slime", 1, 10, 0.5, (0, 32), (x*8, y*8)))
                    print(f"Adding enemy at {x*8}, {y*8}")
                    self.enemies[-1].set_path("linear", [(x*8, y*8), (x*8+16, y*8+16)])
                    pyxel.tilemap(0).pset(x, y, (1, 0))

        pyxel.run(self.update, self.draw)  # Start the game loop

    def get_tile(self, tile_x, tile_y):
        return pyxel.tilemap(0).pget(tile_x, tile_y)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): # Press Q to quit the game
            pyxel.quit()
        self.player.move()
        
        for enemy in self.enemies:
            enemy.move()

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
