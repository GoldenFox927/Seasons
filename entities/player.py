import pyxel


class Player:
    def __init__(self, name, level, health, coordinates):
        self.name = name
        self.level = level
        self.attack_damage = 10
        self.health = health
        self.max_health = health
        self.coordinates = coordinates
        self.sprite = (8, 8)
        self.capabilities = {
            "attack": [("slash", 10, None), ("stab", 5, None)],
            "spell": [("sunray", 20, "burn")],
        }

    def is_traversable(self, x: int, y: int) -> bool:
        """Check if the player can move to the given coordinates

        Args:
            x (int): the x coordinate
            y (int): the y coordinate

        Returns:
            bool : True if the player can move to the given coordinates, False otherwise
        """

        # get the tile for all corner of the player
        tile_ul = pyxel.tilemap(0).pget(x // 8, y // 8)
        tile_bl = pyxel.tilemap(0).pget(x // 8, (y + 7) // 8)
        tile_br = pyxel.tilemap(0).pget((x + 7) // 8, (y + 7) // 8)
        tile_ur = pyxel.tilemap(0).pget((x + 7) // 8, y // 8)

        up_left = (
            tile_ul[0] >= 2 and tile_ul[0] <= 3 and tile_ul[1] >= 0 and tile_ul[1] <= 1
        )  # Check if the tile is a traversable tile
        up_right = (
            tile_ur[0] >= 2 and tile_ur[0] <= 3 and tile_ur[1] >= 0 and tile_ur[1] <= 1
        )  # Check if the tile is a traversable tile
        bottom_left = (
            tile_bl[0] >= 2 and tile_bl[0] <= 3 and tile_bl[1] >= 0 and tile_bl[1] <= 1
        )  # Check if the tile is a traversable tile
        bottom_right = (
            tile_br[0] >= 2 and tile_br[0] <= 3 and tile_br[1] >= 0 and tile_br[1] <= 1
        )  # Check if the tile is a traversable tile

        # return True if all the corner are traversable
        return up_left and up_right and bottom_left and bottom_right

    def move(self):
        """Move the player based on the input from the keyboard"""
        # get the current coordinates
        nx = self.coordinates[0]
        ny = self.coordinates[1]

        # check the input from the keyboard and update the coordinates
        if pyxel.btn(pyxel.KEY_UP):
            ny -= 1
            self.set_sprite("up")
        if pyxel.btn(pyxel.KEY_DOWN):
            ny += 1
            self.set_sprite("down")
        if pyxel.btn(pyxel.KEY_LEFT):
            nx -= 1
            self.set_sprite("left")
        if pyxel.btn(pyxel.KEY_RIGHT):
            nx += 1
            self.set_sprite("right")

        # update the coordinates if the player can move to the new coordinates
        if self.is_traversable(nx, ny):
            self.coordinates = (nx, ny)

    def pos(self) -> tuple:
        """Get the current coordinates of the player

        Returns:
            tuple : the coordinates of the player
        """
        return self.coordinates

    def hitbox(self) -> tuple:
        """Get the hitbox of the player

        Returns:
            tuple : the hitbox of the player
        """
        return (
            self.coordinates[0],
            self.coordinates[1],
            self.coordinates[0] + 8,
            self.coordinates[1] + 8,
        )

    def set_sprite(self, side: str):
        """Set the sprite of the player based on the direction of the movement

        Args:
            side (str): the direction of the movement
        """
        if side == "right":
            self.sprite = (0, 8)
        elif side == "left":
            self.sprite = (8, 0)
        elif side == "up":
            self.sprite = (8, 8)
        else:
            self.sprite = (0, 0)

    def get_sprite(self) -> tuple:
        """Get the sprite of the player

        Returns:
            tuple: the sprite of the player by coordinates in the resource file
        """
        return self.sprite

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
