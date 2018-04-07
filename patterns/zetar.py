def pulser():
    position = Cell()
    hue = Cell()
    saturation = Cell()
    pulse = AttackRelease(attack=.1, release=1.0)

    def nextPulse():
        pulse.trigger()
        position.value = random.random()
        hue.value = random.random()
        saturation.value = random.random()
        timer.start(1. + random.random() * 0.7)
    timer = Timer(nextPulse)
    timer.start(1.0)

    def eval(i, n, N):
        brightness = pulse() ** 2
        ap = (1.0 / (1.0 + abs(n - position()) * 10.0)) ** 2;
        c2 = HSV(hue(), 1, ap * brightness)
        return c2
    return None, eval

def main():
    instances = [pulser() for _ in range(0, 4)]

    def eval(i, n, N):
        colors = tuple(e(i, n, N) for _, e in instances)
        return max(*colors)
    return None, eval
