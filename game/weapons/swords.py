from game.weapons_types import Sword


class Katana(Sword):
    def __init__(self, damage, attack_range, hit_time, effects, name) -> None:
        super().__init__(damage, attack_range, hit_time, effects, name)
