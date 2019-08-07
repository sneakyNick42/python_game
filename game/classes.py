import abc


class Weapon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, damage: int, attack_range: int, hit_time: float, effects: list = None) -> None:
        self.damage = damage
        self.attack_range = attack_range
        self.hit_time = hit_time
        self.effects = effects

    @abc.abstractmethod
    def attack(self):
        return NotImplemented

    @abc.abstractmethod
    def apply_effects(self):
        return NotImplemented


class Effect(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self) -> None:
        super().__init__()
