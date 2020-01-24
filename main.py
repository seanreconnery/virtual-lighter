import kivy
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from random import randrange

woo = SoundLoader.load('data/audio/woo.wav')
#  "WOOOO!"

yeah = SoundLoader.load('data/audio/yeah.wav')
#  "YEEEAAAHH!!"

justthehits = SoundLoader.load('data/audio/justthehits.wav')
#  "just play the hits--none of that new crap you're working on"

boobs = SoundLoader.load('data/audio/boobs.wav')
#  "SHOW US YOUR BOOBS!"

stairway = SoundLoader.load('data/audio/stairway.wav')
#  "now play stairway to heaven!"


class BicLighter(ButtonBehavior, Image):
    def on_press(self):
        #woo.play()
        i = randrange(7)
        if i == 0:
            woo.play()
        elif i == 1:
            yeah.play()
        elif i == 2:
            justthehits.play()
        elif i == 3:
            boobs.play()
        elif i == 4:
            woo.play()
        elif i == 5:
            stairway.play()
        else:
            yeah.play()

class MyGrid(Widget):
    pass

class myapp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    myapp().run()