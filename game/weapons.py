from game.classes import Weapon


class Sword(Weapon):
    def __init__(self, damage, attack_range, hit_time) -> None:
        super().__init__(damage, attack_range, hit_time)

    @property
    def damage(self):
        return self.damage

    @property
    def range(self):
        return self.range

    @property
    def hit_time(self):
        return self.hit_time

    def apply_effects(self):
        pass
