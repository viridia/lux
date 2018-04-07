RF = 0.7
GF = 0.2
BF = 0.5

def main():
    red = Oscillator(freq=RF * 0.1, waveform=Oscillator.SINE)
    green = Oscillator(freq=GF * 0.1, waveform=Oscillator.SINE)
    blue = Oscillator(freq=BF * 0.1, waveform=Oscillator.SINE)

    def eval(i, n, N):
        return RGB(
            red(offset=n * RF),
            green(offset=n * GF),
            blue(offset=n * BF))

    return None, eval
