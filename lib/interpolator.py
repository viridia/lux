from .pattern import Pattern
from .math import clamp

# Smoothes out the input signal
class Interpolator:
    def __init__(self, value=0.0, rate=1.0, wrap=False, min=0.0, max=1.0):
        self.value = self._next = float(value)
        self.rate = float(rate)
        self.wrap = wrap
        self.min = float(min)
        self.max = float(max)
        Pattern.tracked.append(self)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = float(value)

    def advance(self, ms):
        diff = self._next - self.value
        rate = self.rate * ms
        if diff == 0: return

        if self.wrap:
            rng = self.max - self.min
            if abs(diff) > rng / 2:
                diff = -diff
            diff = clamp(diff, -rate, rate)
            self.value = (self.value + diff - self.min) % rng + self.min
        else:
            diff = clamp(diff, -rate, rate)
            self.value += diff

    def __call__(self):
        return self.value
