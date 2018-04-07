def main():
    patterns = [
        (load('warpcore'), 50),
        (load('aliensunset'), 50),
        (load('pong'), 20),
        (load('zetar'), 20),
        (load('serape'), 20),
    ]
    current = patterns[0][0]

    def nextPattern():
        nonlocal current
        current, duration = random.choice(patterns)
        timer.start(duration)
    timer = Timer(nextPattern)
    timer.start(0.0)

    def update():
        if current.update:
            current.update()

    def eval(i, n, N):
        return current.eval(i, n, N)

    return update, eval
