from game.classes import Weapon


class Sword(Weapon):
    def __init__(self, damage, attack_range, hit_time, effects, name) -> None:
        self.name = name
        super().__init__(damage, attack_range, hit_time, effects)

    def attack(self):
        pass

    def apply_effects(self):
        pass
