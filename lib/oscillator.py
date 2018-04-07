from .pattern import Pattern
from .math import clamp
import math

class Oscillator:
    TRIANGLE = 1
    SINE = 2
    SQUARE = 3

    def __init__(self, *, waveform=None, start=0, freq=1.0, skew=0.5):
        self.value = start
        self.frequency = freq
        self._skew = skew
        self._lower = 0.0
        self._upper = 1.0
        if waveform is None:
            waveform = Oscillator.TRIANGLE
        self.waveform = waveform
        Pattern.tracked.append(self)

    @property
    def frequency(self):
        return self._freq

    @frequency.setter
    def frequency(self, value):
        self._freq = clamp(value, 0, 100)

    @property
    def period(self):
        return 1.0 / self._freq

    @period.setter
    def period(self, value):
        self._freq = 1.0 / clamp(value, .010, 1.0e10)

    @property
    def skew(self):
        return self._skew

    @skew.setter
    def skew(self, value):
        self._skew = clamp(value, 0.0, 1.0)

    def advance(self, ms):
        self.value = math.fmod(self.value + ms * self._freq, 1.0)

    def __call__(self, *, offset=0, skew=None):
        value = (self.value + offset) % 1.0
        if self.waveform == Oscillator.SINE:
            return math.sin(value * math.pi * 2) * 0.5 + 0.5

        skew = self._skew if skew is None else clamp(skew, 0.0, 1.0)
        if value <= skew:
            if self.waveform == Oscillator.TRIANGLE:
                return value / skew
            elif self.waveform == Oscillator.SQUARE:
                return 0
        else:
            if self.waveform == Oscillator.TRIANGLE:
                return (1 - value) / (1 - skew)
            elif self.waveform == Oscillator.SQUARE:
                return 1
        return 0
