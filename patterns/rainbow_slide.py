# Rainbow slide effects
def main():
    osc1 = Oscillator(freq=0.2)
    osc2 = Oscillator(freq=0.1, waveform=Oscillator.SINE)
    def update():
        osc1.frequency = 0.1 + osc2() * 0.3
    def eval(i, n, N):
        return HSV(osc1(offset=-n / 4.0, skew=1.0), 1, 1)
    return update, eval
