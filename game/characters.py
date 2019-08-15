from game.classes import Weapon, Character


class Enemy(Character):
    def __init__(self, name: str, hp: int, weapon: Weapon) -> None:
        self.name = name
        self.hp = hp
        self.weapon = weapon
        super().__init__(name=self.name, hp=self.hp)

    def equip(self, new_weapon):
        self.weapon = new_weapon

    def attack(self, target: Character):
        self.weapon.attack(target)


class Player(Character):
    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name = name
        self.hp = 100
        self.weapon = weapon
        super().__init__(name=self.name, hp=self.hp)

    def equip(self, new_weapon):
        self.weapon = new_weapon

    def attack(self, target: Enemy):
        self.weapon.attack(target)
