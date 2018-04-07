import colorsys
import builtins

class Color(tuple):
    pass

def HSV(h, s, v):
    return RGB(*colorsys.hsv_to_rgb(h, s, v))

def RGB(r, g, b):
    return (r, g, b)

def lerp(a, b, t):
    return tuple(ai + (bi - ai) * t for ai, bi in zip(a, b))

def add(a, b):
    return tuple(ai + bi for ai, bi in zip(a, b))

def mul(a, t):
    return tuple(ai * t for ai in a)

def max(*args):
    return tuple(builtins.max(*elements) for elements in zip(*args))

def min(*args):
    return tuple(builtins.min(*elements) for elements in zip(*args))

def norm(a):
    return tuple(clamp(ai, 0.0, 1.0) for ai in a)
