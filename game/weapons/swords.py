from game.weapons.weapons_types import Sword


class Katana(Sword):
    def __init__(self, name: str, damage: int, hit_time: float, effects: list = None) -> None:
        self.attack_range = 1
        super().__init__(name, damage, hit_time, effects)
