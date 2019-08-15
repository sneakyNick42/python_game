from game.characters import Enemy
from game.classes import Weapon


class Orc(Enemy):
    def __init__(self, name: str, hp: int, weapon: Weapon) -> None:
        super().__init__(name, hp, weapon)
