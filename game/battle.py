import game.button as button
import pyxel

class Battle:
    def __init__(self, party:list, enemy):
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
            

    #def start(self):
        