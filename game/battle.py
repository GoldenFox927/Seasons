class Battle:
    def __init__(self, party:list, enemy):
        self.player = party
        self.enemy = enemy

    def start(self):
        print(f"Player: {self.player.name} vs Enemy: {self.enemy.name}")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        if self.player.is_alive():
            print(f"{self.player.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")