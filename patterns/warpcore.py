def main():
    wave = Oscillator(freq=4.0, waveform=Oscillator.SINE)
    hue1 = Interpolator(random.random(), rate=0.3, wrap=True)
    hue2 = Interpolator(random.random(), rate=0.3, wrap=True)
    speed = Interpolator(random.random(), rate=0.3)
    pulse = Ramp(min=-0.5, max=1.5, duration=0.5)

    def nextColor():
        hue1.next = (hue1.next + random.uniform(-.1, .1)) % 1.0
        hue2.next = (hue1.next + random.uniform(-.13, .13)) % 1.0
        speed.next = clamp(speed.next + random.uniform(-.2, .2), 0.5, 6.0)
        timer.start(1 + random.random() * 3)
    timer = Timer(nextColor)
    timer.start(0.0)

    def nextPulse():
        pulse.reset()
        timer2.start(0.5 + random.random() * 2)
    timer2 = Timer(nextPulse)
    timer2.start(1.0)

    def update():
        wave.frequency = speed()
    def eval(i, n, N):
        # Wave
        c0 = HSV(hue1(), 1, 0.3)
        c1 = HSV(hue2(), 1, 1)
        cc = lerp(c0, c1, wave(offset=-n * 1.9))

        # Pluse
        d = builtins.max(0, abs(n - pulse()) - 0.5 / N)
        ap = (1.0 / (1.0 + d * 10.0)) ** 3;
        c2 = HSV(hue1(), 0.5, ap)

        return max(cc, c2)
    return update, eval
