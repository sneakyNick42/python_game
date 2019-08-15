from game.characters import Enemy


class Orc(Enemy):
    def __init__(self, name, weapon) -> None:
        self.name = name
        self.hp = 10
        self.weapon = weapon
        super().__init__(self.name, self.weapon)

    def attack(self):
        self.weapon.attack()
