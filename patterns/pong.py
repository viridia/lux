def main():
    position = Oscillator(freq=0.5, waveform=Oscillator.TRIANGLE)
    hue = Interpolator(random.random(), rate=0.3, wrap=True)
    pulse = AttackRelease(attack=.1, release=1.0)

    def nextColor():
        pulse.trigger()
        hue.next = random.random()
        timer.start(10. + random.random() * 10.)
    timer = Timer(nextColor)
    timer.start(1.0)

    def eval(i, n, N):
        p = abs(1. - n * 2.)
        d = builtins.max(0, abs(p - position()) - 0.5 / N)
        ap = (1.0 / (1.0 + d * 3.0)) ** 3;
        return HSV(hue(), 1. - ap * 0.3, 0.1 + 0.9 * ap)
    return None, eval
