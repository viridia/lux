import sys
import time
from neopixel import *
from pathlib import Path
from lib import Animator, Loader, Pattern
import argparse

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(
    LED_COUNT,
    LED_PIN,
    LED_FREQ_HZ,
    LED_DMA,
    LED_INVERT,
    LED_BRIGHTNESS,
    LED_CHANNEL,
    LED_STRIP)

# Intialize the library (must be called once before other functions).
strip.begin()

# setup option parser
argParser = argparse.ArgumentParser(
    description='''Simulate NeoPixel animations.\n''')
argParser.add_argument('pattern', help="Pattern to display.", default='carousel', nargs='?')
args = argParser.parse_args()

animator = Animator()
loader = Loader(animator, Path(__file__).parent / 'patterns')
animator.pattern = loader.loadPattern(args.pattern)

UPDATE_INTERVAL = 1.0 / 60.0 # 120 fps

try:
    while True:
        animator.advance(UPDATE_INTERVAL)
        for i in range(0, LED_COUNT):
            r, g, b = animator.output[i]
            strip.setPixelColor(i, Color(int(r * 255.0), int(g * 255.0), int(b * 255.0)))
        strip.show()
        time.sleep(UPDATE_INTERVAL)
except KeyboardInterrupt:
    print('Exiting...')
    del strip
    sys.exit()
