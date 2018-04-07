from abc import abstractmethod
from .colors import RGB

# Animate NeoPixels from a pattern.
class Animator:
    def __init__(self, numPixels = 30, pattern=None): # 120 fps
        self.pattern = pattern
        self.numPixels = numPixels
        self.output = [RGB(0, 0, 0) for i in range(0, numPixels)]

    # Advance the animation by the specified number of milliseconds
    def advance(self, ms):
        if self.pattern:
            self.pattern.advance(ms)
            if self.pattern.update:
                self.pattern.update()
            for i in range(0, self.numPixels):
                self.output[i] = self.pattern.eval(i, float(i) / self.numPixels, self.numPixels)
