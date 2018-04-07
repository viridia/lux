def clamp(t, minVal, maxVal):
    if t <= minVal: return minVal
    if t >= maxVal: return maxVal
    return t
