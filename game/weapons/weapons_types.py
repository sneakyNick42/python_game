from game.classes import Weapon, Character


class Sword(Weapon):
    def __init__(self, name: str, damage: int, hit_time: float, effects: list = None) -> None:
        self.name = name
        self.damage = damage
        self.hit_time = hit_time
        self.effects = effects
        super().__init__()

    def attack(self, target: Character):
        target.hp -= self.damage
        self.apply_effects(target)

    def apply_effects(self, target: Character):
        pass
