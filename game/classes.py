from abc import ABCMeta, abstractmethod


class Character(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
        super().__init__()


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def attack(self, target: Character):
        return NotImplementedError

    @abstractmethod
    def apply_effects(self, target: Character):
        return NotImplementedError


class Effect(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def has_applied(self):
        return NotImplementedError

    @abstractmethod
    def apply(self):
        return NotImplementedError

    @abstractmethod
    def activate(self):
        return NotImplementedError
