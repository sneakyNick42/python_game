from game.classes import Weapon


class Sword(Weapon):
    def __init__(self, name: str, damage: int, attack_range: int, hit_time: float, effects: list = None) -> None:
        self.name = name
        self.damage = damage
        self.attack_range = attack_range
        self.hit_time = hit_time
        self.effects = effects
        super().__init__()

    def attack(self):
        pass

    def apply_effects(self):
        pass
