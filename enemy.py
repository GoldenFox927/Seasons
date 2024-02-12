class Enemy:
    def __init__(self, name, health, attack_damage, sprite, pos=(0, 0)):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.path = []
        self.sprite = sprite
        self.coordinate = pos

    def get_sprite(self):
        return self.sprite

    def set_path(self, type, path):
        self.path = [[type, 0], path]

    def pos(self):
        return self.coordinate

    def take_damage(self, damage):
        self.health -= damage

    def attack(self):
        return self.attack_damage

    def is_alive(self):
        return self.health > 0