#!/usr/bin/python3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.clock import Clock
from lib import Animator, Loader, Pattern
from pathlib import Path
import argparse

# from patterns import warpcore

Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '600')

INTERVAL = 1.0 / 60.0
GAMMA = 1.0 / 1.7

class PatternDisplay(Widget):
    def repaint(self, colors):
        count = len(colors)
        self.canvas.clear()
        with self.canvas:
            for i, color in enumerate(colors):
                y0 = self.height - (self.height * i / count)
                y1 = self.height - (self.height * (i + 1) / count)
                r, g, b = color
                Color(r ** GAMMA, g ** GAMMA, b ** GAMMA) # Gamma correct to emulate neopixels
                Rectangle(pos=(0, y0), size=(self.width, y1 - y0))

class TestApp(App):
    def on_start(self):
        Clock.schedule_interval(self.animate, INTERVAL)

    def animate(self, ms):
        self.animator.advance(ms)
        self.display.repaint(self.animator.output)

    def build(self):
        self.display = PatternDisplay()
        self.animator = Animator()
        self.loader = Loader(self.animator, Path(__file__).parent / 'patterns')
        self.animator.pattern = self.loader.loadPattern(args.pattern)
        return self.display

# setup option parser
argParser = argparse.ArgumentParser(
    description='''Simulate NeoPixel animations.\n''')
argParser.add_argument('pattern', help="Pattern to display.", default='warpcore', nargs='?')
args = argParser.parse_args()

TestApp().run()
