#!/usr/bin/env python3

"""
Zachary Meisner

tetris_main.py

A manager file to initially load all game assets and manage whether or not
the game begins or ends.  This is also where the primary game loop is held
in addition to tracking whether or not we want to exit the game.

This game was created following a tutorial on Youtube by Coder Space.
The video can be watched here: https://www.youtube.com/watch?v=RxWS5h1UfI4
Github: https://github.com/StanislavPetrovV/Tetris/tree/main

The primary goal behind the creation of this game is to help define
an overall baseline for the creation of our project Trivial Compute.
In this tutorial, we can find common programming patterns that define
the creation of our game graphical interface, logic, and much more.

Additionally, we use this game to help define base functionality for the team
to assure that there is a common ability for everyone to run the project
in its current configuration.  Testing can also be done for future configuration
pertaining to project deliverables and other experimental ideas prior
to their integration.
"""

from settings import *
from tetris import Tetris, Text
import sys
import pathlib


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        pg.mixer.music.play(loops=-1, start=0.0, fade_ms=10000)
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)


    def load_images(self):
        files = [item for item in
                 pathlib.Path(SPRITE_DIR_PATH).rglob('*.png')
                 if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) 
                  for image in images]
        return images


    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)


    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)


    def draw(self):
        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()


    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                         and event.key == pg.K_ESCAPE):
                pg.mixer.music.stop()
                pg.mixer.music.unload()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
