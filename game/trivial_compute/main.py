#!/usr/bin/env python3

"""
Zachary Meisner
main.py

Provides a basic interface for players to interact with.
Creates the initial pygame framework in which the screen and main game loop
are established.  This interface will primarily interact with the settings.py
file in addition to the trivial_compute.py file which will house core logic.
"""

from settings import *
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Byte-Builders Trivial Compute')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT
                or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
