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
from gameboard import GameBoard
from menu import Menu
import sys

resolution = MIN_WIN_RES
res_mode = pg.FULLSCREEN

i = 1
n = len(sys.argv)
while i < n:
    if (sys.argv[i] == "-r" and i + 1 < n):
        res = sys.argv[i + 1].lower()
        if res == "max":
            resolution = MAX_WIN_RES
        elif res == "med":
            resolution = MED_WIN_RES
        elif res == "min":
            resolution = MIN_WIN_RES
        i += 1
    elif (sys.argv[i] == "-m" and i + 1 < n):
        mode = sys.argv[i + 1].lower()
        if mode == "full":
            res_mode = pg.FULLSCREEN
        elif mode == "sized":
            res_mode = pg.RESIZABLE
        elif mode == "windowed":
            res_mode = pg.NOFRAME
        i += 1
    i += 1

class App:
    global res_mode
    global resolution

    def __init__(self):
        pg.init()
        pg.display.set_caption('Byte-Builders Trivial Compute')
        self.screen = pg.display.set_mode(resolution, res_mode)
        self.res = (self.x, self.y) = self.screen.get_size()
        self.clock = pg.time.Clock()
        self.menu = Menu(self)
        self.scale = pg.transform.scale(self.menu.bg_img, self.res)
        self.gameboard = GameBoard(self)

    def update(self):
        self.menu.update()
        # self.gameboard.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.menu.bg_img = self.scale
        # self.screen.blit(self.menu.bg_img, (0, 0))
        self.menu.draw()
        # self.gameboard.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT
                or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for i in self.menu.btn_list:
                    button = getattr(self.menu, i[0])
                    if button.area.get_rect(topleft=
                                            button.pos).collidepoint(pos):
                        print(f"{i[4]} was clicked!")
            elif event.type == pg.VIDEORESIZE:
                self.screen = pg.display.set_mode((event.w, event.h), res_mode)
                self.scale = pg.transform.scale(self.menu.bg_img,
                                                (event.w, event.h))

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
