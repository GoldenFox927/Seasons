import pyxel # Import the Pyxel module
import textzone as tz

class Dialogue:
    def __init__(self):
        self.dialogue = []
        self.actual_line = ["None", (0, 0), "None"]
        self.dialogue_box = tz.TextZone("", 0, 100, 192, 3)