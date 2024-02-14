import game.button as button
import pyxel


class Battle:
    def __init__(self, party: list, enemy):
        self.player = party
        self.enemy = enemy
        self.buttons = [
            button.Button(0, 112, 6, "Attack", (208, 232)),
            button.Button(48, 112, 6, "Spells", (200, 232)),
            button.Button(96, 112, 6, "Object", (216, 232)),
            button.Button(144, 112, 6, "Action", (224, 232)),
        ]
        self.buttons[0].change_state()
        self.selected_button = 0

    def draw(self):
        pyxel.bltm(0, 0, 0, 1856, 1920, 192, 128, 0)  # Draw the background

        # Draw the player
        pyxel.blt(
            40,
            26,
            0,
            0,
            8,
            8,
            8,
            2,
        )
        # draw player life bar
        pyxel.rect(39, 19, 10, 3, 7)
        pyxel.rect(40, 20, 8, 1, 8)
        pyxel.rect(40, 20, self.player.health * 8 / 100, 1, 11)

        # Draw the enemy
        pyxel.blt(
            128,
            26,
            0,
            self.enemy.get_sprite()[0],
            self.enemy.get_sprite()[1],
            8,
            8,
            2,
        )

        # draw enemy life bar
        pyxel.rect(127, 19, 10, 3, 7)
        pyxel.rect(128, 20, 8, 1, 8)
        pyxel.rect(
            128, 20, self.enemy.health * 8 / self.enemy.max_health, 1, 11
        )

        # Draw the buttons
        for button in self.buttons:
            button.draw()

    def run(self):
        self.change_button()
        self.button_click()
        return "battle" if self.enemy.health > 0 else "exploration"

    def change_button(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.buttons[self.selected_button].change_state()
            self.selected_button -= 1
            if self.selected_button < 0:
                self.selected_button = 3
            self.buttons[self.selected_button].change_state()
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.buttons[self.selected_button].change_state()
            self.selected_button += 1
            if self.selected_button > 3:
                self.selected_button = 0
            self.buttons[self.selected_button].change_state()

    def button_click(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.selected_button == 0:
                self.enemy.take_damage(self.player.attack_damage)
