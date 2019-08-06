import abc


class Weapon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, damage, attack_range, hit_time) -> None:
        self.damage = damage
        self.attack_range = attack_range
        self.hit_time = hit_time

    @abc.abstractmethod
    def apply_effects(self):
        return NotImplemented
