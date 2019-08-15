from game.classes import Effect


class Buff(Effect):
    def __init__(self, heal: int, duration: float, tick: int) -> None:
        self.heal = heal
        self.duration = duration
        self.tick = tick
        super().__init__()

    def has_applied(self):
        pass

    def apply(self):
        pass

    def activate(self):
        pass


class DeBuff(Effect):
    def __init__(self, damage: int, duration: float, tick: int) -> None:
        self.damage = damage
        self.duration = duration
        self.tick = tick
        super().__init__()

    def has_applied(self):
        pass

    def apply(self):
        pass

    def activate(self):
        pass


class Bleed(DeBuff):
    def __init__(self, damage: int, duration: float, tick: int) -> None:
        super().__init__(damage, duration, tick)

    def has_applied(self):
        super().has_applied()

    def apply(self):
        super().apply()

    def activate(self):
        super().activate()
