from game.classes import Weapon, Character


class Player(Character):
    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name = name
        self.hp = 100
        self.weapon = weapon
        super().__init__()

    def equip(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        self.weapon.attack()


class Enemy(Character):
    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name = name
        self.weapon = weapon
        super().__init__()

    def equip(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        self.weapon.attack()
