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
        self.selected_menu = 0
        self.actual_menu = "info"

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
        pyxel.rect(40, 20, self.player.health * 8 / self.player.max_health, 1, 11)

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
        pyxel.rect(128, 20, self.enemy.health * 8 / self.enemy.max_health, 1, 11)

        # Draw the buttons
        for button in self.buttons:
            button.draw()

        # Draw the menu
        if self.actual_menu == "info":
            self.info_menu()
        elif self.actual_menu == "attack":
            self.attack_menu()

    def run(self):
        if self.actual_menu == "info":
            self.change_button()
            self.button_click()
        elif self.actual_menu == "attack":
            self.choose_attack()

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
                self.actual_menu = "attack"

    def choose_attack(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected_menu -= 1
            if self.selected_menu < 0:
                self.selected_menu = len(self.player.capabilities["attack"]) - 1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_menu += 1
            if self.selected_menu > len(self.player.capabilities["attack"]) - 1:
                self.selected_menu = 0
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.enemy.health -= self.player.capabilities["attack"][self.selected_menu][1]
            self.actual_menu = "info"

    def info_menu(self):
        pyxel.text(
            8, 74, f"{self.enemy.name} : {self.enemy.health}/{self.enemy.max_health}", 7
        )

        pyxel.text(8, 96, "What will you do?", 7)

    def attack_menu(self):
        pyxel.blt(8, 72+8*self.selected_menu, 0, 208, 224, 8, 8, 0)
        for i in range(len(self.player.capabilities["attack"])):
            pyxel.text(16, 74 + 8 * i, self.player.capabilities["attack"][i][0], 7)
