from abc import ABCMeta, abstractmethod


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def attack(self):
        return NotImplementedError

    @abstractmethod
    def apply_effects(self):
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
