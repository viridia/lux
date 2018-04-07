from .pattern import Pattern
from .math import clamp

# Simply stores a value until changed
class Cell:
    def __init__(self, value=0.0):
        self.value = float(value)

    def advance(self, ms): pass

    def __call__(self):
        return self.value
