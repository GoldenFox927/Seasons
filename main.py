import pyxel
from player import Player


class App:
    def __init__(self):
        pyxel.init(160, 120)  # Set the window size
        pyxel.load("resources.pyxres") # load the resources file

        self.player = Player("Brise", 1, 100, (0, 0)) # Create a player object

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


if __name__ == "__main__":
    App()
