import pyxel
class Enemy:
    def __init__(self, name, health, attack_damage, speed, sprite, pos=(0, 0)):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.speed = speed
        self.path = []
        self.sprite = sprite
        self.coordinate = pos

    def get_sprite(self):
        return self.sprite

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
            elif self.coordinate[0] > self.path[2][self.path[1]][0]:
                self.coordinate = (self.coordinate[0] - self.speed, self.coordinate[1])
        elif self.coordinate[1] != self.path[2][self.path[1]][1]:
            if self.coordinate[1] < self.path[2][self.path[1]][1]:
                self.coordinate = (self.coordinate[0], self.coordinate[1] + self.speed)
            elif self.coordinate[1] > self.path[2][self.path[1]][1]:
                self.coordinate = (self.coordinate[0], self.coordinate[1] - self.speed)

    def pos(self):
        return self.coordinate

    def take_damage(self, damage):
        self.health -= damage

    def attack(self):
        return self.attack_damage

    def is_alive(self):
        return self.health > 0