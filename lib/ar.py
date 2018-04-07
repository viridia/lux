from .pattern import Pattern
from .math import clamp

# Simple attack/release envelope
class AttackRelease:
    def __init__(self, *, min=0, max=1.0, attack=1.0, release=1.0):
        self.min = min
        self.max = max
        self.attack = attack
        self.release = release
        self.value = self.min
        self.active = False
        Pattern.tracked.append(self)

    def trigger(self):
        self.active = True
        self.value = self.min

    def advance(self, ms):
        if self.active:
            rate = ms * (self.max - self.min) / self.attack
            self.value = clamp(self.value + rate, self.min, self.max)
            if self.value == self.max:
                self.active = False
        else:
            rate = ms * (self.max - self.min) / self.release
            self.value = clamp(self.value - rate, self.min, self.max)

    def __call__(self):
        return self.value
