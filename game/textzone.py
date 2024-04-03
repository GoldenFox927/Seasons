import pyxel # Import the Pyxel module

class TextZone:
    def __init__(self, text, x, y, width, lines=-1, color=7):
        self.text = text.split(" ")
        count = 0
        while len(self.text) > count+1:
            if len(self.text[count])*4 + len(self.text[count+1])*4 + 4 <= width:
                self.text[count] = self.text[count] + " " + self.text.pop(count+1)
            else:
                count += 1
        
        self.x = x
        self.y = y
        self.width = width
        self.lines = lines
        self.color = color
        
    def draw(self):
        for count, line in enumerate(self.text):
            pyxel.text(self.x, self.y+6*count, line, self.color)
            
TextZone("Ceci est un long text qui va etre coupe en plusieurs lignes", 0, 0, 100)