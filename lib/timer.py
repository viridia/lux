from .pattern import Pattern

# Smoothes out the input signal
class Timer:
    def __init__(self, callback):
        self.running = False
        self.duration = 0.0
        self.callback = callback
        Pattern.tracked.append(self)

    def start(self, duration=0.0):
        self.duration = duration
        self.enabled = True

    def advance(self, ms):
        if self.enabled:
            self.duration -= ms
            if self.duration <= 0:
                self.enabled = False
                self.callback()

    def __call__(self):
        return self.duration
