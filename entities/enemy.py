import pyxel
class Enemy:
    def __init__(self, name, health, attack_damage, speed, sprite, pos=(0, 0)):
        print(attack_damage)
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_damage = attack_damage
        self.speed = speed
        self.path = []
        self.sprite_type = sprite
        self.sprite = sprite
        self.coordinate = pos

    def __str__(self) -> str:
        return f"{self.name} : {self.health}/{self.max_health}"

    def get_sprite(self):
        return self.sprite
    
    def get_sprite_type(self):
        return self.sprite_type

    def set_path(self, type, path):
        self.path = [type, 0, path]
        
    def move(self):
        if self.coordinate[0] == self.path[2][self.path[1]][0] and self.coordinate[1] == self.path[2][self.path[1]][1]:
            if self.path[1] < len(self.path[2]) - 1:
                self.path[1] += 1
            else:
                self.path[1] = 0
        if self.coordinate[0] != self.path[2][self.path[1]][0]:
            if self.coordinate[0] < self.path[2][self.path[1]][0]:
                self.coordinate = (self.coordinate[0] + self.speed, self.coordinate[1])
                self.set_sprite("right")
            elif self.coordinate[0] > self.path[2][self.path[1]][0]:
                self.coordinate = (self.coordinate[0] - self.speed, self.coordinate[1])
                self.set_sprite("left")
        elif self.coordinate[1] != self.path[2][self.path[1]][1]:
            if self.coordinate[1] < self.path[2][self.path[1]][1]:
                self.coordinate = (self.coordinate[0], self.coordinate[1] + self.speed)
                self.set_sprite("down")
            elif self.coordinate[1] > self.path[2][self.path[1]][1]:
                self.coordinate = (self.coordinate[0], self.coordinate[1] - self.speed)
                self.set_sprite("up")

    def set_sprite(self, side):
        if side == "right":
            self.sprite = (self.sprite_type[0], self.sprite_type[1]+8)
        elif side == "left":
            self.sprite = (self.sprite_type[0]+8, self.sprite_type[1]+8)
        elif side == "up":
            self.sprite = (self.sprite_type[0]+8, self.sprite_type[1])
        else:
            self.sprite = (self.sprite_type[0], self.sprite_type[1])

    def pos(self):
        return self.coordinate
    
    def hitbox(self):
        return (self.coordinate[0], self.coordinate[1], self.coordinate[0]+8, self.coordinate[1]+8)

    def take_damage(self, damage):
        self.health -= damage

    def attack(self):
        return self.attack_damage

    def is_alive(self):
        return self.health > 0