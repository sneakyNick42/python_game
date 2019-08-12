from game.weapons_types import Sword


class Katana(Sword):
    def __init__(self, name: str, damage: int, attack_range: int, hit_time: float, effects: list = None) -> None:
        super().__init__(name, damage, attack_range, hit_time, effects)