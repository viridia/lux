from .pattern import Pattern
from .math import clamp

class Ramp:
    def __init__(self, *, min=0, max=1.0, duration=1.0):
        self.min = min
        self.max = max
        self.duration = duration
        self.value = self.min
        Pattern.tracked.append(self)

    def reset(self):
        self.value = self.min

    def advance(self, ms):
        self.value = clamp(self.value + ms / self.duration, self.min, self.max)

    def __call__(self):
        return self.value
