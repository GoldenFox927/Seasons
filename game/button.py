import pyxel

class Button:
    def __init__(self, x, y, w, text, icon):
        assert w > 2, "Button width must be greater than 2 tiles"
        self.x = x
        self.y = y
        self.w = w
        self.icon = icon
        self.text = text
        self.action = action
        self.is_selected = False
        
    def change_state(self):
        self.is_selected = not self.is_selected
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 208, 240, 8, 16, 0)
        for i in range(1, self.w-1):
            pyxel.blt(self.x+i*8, self.y, 0, 216, 240, 8, 16, 0)
        pyxel.blt(self.x+(self.w-1)*8, self.y, 0, 224, 240, 8, 16, 0)
        
        if self.is_selected:
            color = 12
            icon = (self.icon[0], self.icon[1]-8)
        else:
            color = 7
            icon = self.icon
            
        pyxel.text(self.x+20, self.y+5, self.text, color)
        pyxel.blt(self.x+4, self.y+4, 0, icon[0], icon[1], 8, 8, 0)