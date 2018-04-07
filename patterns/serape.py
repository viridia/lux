RF = 1.7
GF = 2.1
BF = 1.5

def main():
    red = Oscillator(freq=RF * 0.1, waveform=Oscillator.TRIANGLE, skew=0.2)
    green = Oscillator(freq=GF * 0.1, waveform=Oscillator.TRIANGLE, skew=0.2)
    blue = Oscillator(freq=BF * 0.1, waveform=Oscillator.TRIANGLE, skew=0.2)

    def eval(i, n, N):
        return RGB(
            red(offset=n * 2),
            green(offset=n * 3),
            blue(offset=n))

    return None, eval
