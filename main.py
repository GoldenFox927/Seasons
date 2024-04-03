import pyxel
from entities.player import Player
from entities.enemy import Enemy
from game.battle import Battle
from game.textzone import TextZone
import random as r


class App:
    def __init__(self):
        pyxel.init(192, 128)  # Set the window size
        pyxel.load("resources.pyxres")  # load the resources file

        self.player = Player("Player", 1, 100, (0, 0))  # Create a player object

        self.enemies = []

        self.game_state = "exploration"

        self.battle = Battle(self.player, Enemy("Bugz", 20, 10, 0.5, (24, 40)))

        for x in range(16):
            for y in range(16):
                tile = self.get_tile(x, y)
                if tile == (2, 4):
                    self.enemies.append(
                        Enemy("Slime", 20, 10, 0.5, (16, 32), (x * 8, y * 8))
                    )
                    self.enemies[-1].set_path(
                        "linear", [(x * 8, y * 8), (x * 8 + 16, y * 8 + 16)]
                    )
                    pyxel.tilemap(0).pset(x, y, (2, 0))

        pyxel.run(self.update, self.draw)  # Start the game loop

    def get_tile(self, tile_x, tile_y):
        return pyxel.tilemap(0).pget(tile_x, tile_y)

    def collision(self, enemy):
        if (
            self.player.hitbox()[0] < enemy.hitbox()[2]
            and self.player.hitbox()[2] > enemy.hitbox()[0]
            and self.player.hitbox()[1] < enemy.hitbox()[3]
            and self.player.hitbox()[3] > enemy.hitbox()[1]
        ):
            self.battle = Battle(self.player, enemy)
            self.game_state = "battle"
            self.enemies.remove(enemy)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):  # Press Q to quit the game
            pyxel.quit()

        if self.game_state == "exploration":
            self.player.move()

            for enemy in self.enemies:
                enemy.move()
                self.collision(enemy)

        if self.game_state == "battle":
            self.game_state = self.battle.run()

    def exploration_draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 192, 128, 0)  # Draw the background

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

    def draw(self):
        pyxel.cls(0)  # Clear the screen with color index 0

        if self.game_state == "exploration":
            self.exploration_draw()

        if self.game_state == "battle":
            self.battle.draw()


if __name__ == "__main__":
    App()
