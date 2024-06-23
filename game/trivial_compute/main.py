#!/usr/bin/env python3

"""
Zachary Meisner
main.py

Provides a basic interface for players to interact with.
Creates the initial pygame framework in which the screen and main game loop
are established.  This interface will primarily interact with the settings.py
file in addition to the trivial_compute.py file which will house core logic.
"""

from settings import pg, MAX_WIN_RES, MED_WIN_RES, MIN_WIN_RES, FPS, FIELD_COLOR
from gameboard import GameBoard
from menu import Menu
import sys

resolution = MIN_WIN_RES
res_mode = pg.FULLSCREEN

a = 1
n = len(sys.argv)
while a < n:
    if (sys.argv[a] == "-r" and a + 1 < n):
        res = sys.argv[a + 1].lower()
        if res == "max":
            resolution = MAX_WIN_RES
        elif res == "med":
            resolution = MED_WIN_RES
        elif res == "min":
            resolution = MIN_WIN_RES
        a += 1
    elif (sys.argv[a] == "-m" and a + 1 < n):
        mode = sys.argv[a + 1].lower()
        if mode == "full":
            res_mode = pg.FULLSCREEN
        elif mode == "sized":
            res_mode = pg.RESIZABLE
        elif mode == "windowed":
            res_mode = pg.NOFRAME
        a += 1
    a += 1


"""
Add class docstring here.
"""
class App:
    """
    Add function docstring here.
    """
    def __init__(self):
        pg.init()
        pg.display.set_caption('Byte-Builders Trivial Compute')
        self.screen = pg.display.set_mode(resolution, res_mode)
        self.res = (self.x, self.y) = self.screen.get_size()
        self.clock = pg.time.Clock()
        self.menu = Menu(self)
        self.scale = pg.transform.scale(self.menu.bg_img, self.res)
        self.gameboard = GameBoard(self)
        self.mode = "menu"

    """
    Add function docstring here.
    """
    def update(self):
        if (self.mode == "menu"):
            self.menu.update()
        elif (self.mode == "play"):
            self.gameboard.update()
        self.clock.tick(FPS)

    """
    Add function docstring here.
    """
    def draw(self):
        if (self.mode == "menu"):
            self.screen.fill(color=FIELD_COLOR)
            self.menu.bg_img = self.scale
            # Menu background goes here image spans entire screen.
            # self.screen.blit(self.menu.bg_img, (0, 0))
            self.menu.draw()
            pg.display.flip()
        elif (self.mode == "play"):
            self.screen.fill(color=FIELD_COLOR)
            self.gameboard.draw()
            pg.display.flip()

    """
    Add function docstring here.
    """
    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT
                or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if (self.mode == "menu"):
                    for i in self.menu.btn_list:
                        button = getattr(self.menu, i[0])
                        if button.area.get_rect(topleft=
                                                button.pos).collidepoint(pos):
                            if (i[4] == "Play"):
                                self.mode = "play"
                            elif (i[4] == "Options"):
                                print(f"{i[4]} was clicked!")
                            elif (i[4] == "Mute"):
                                print(f"{i[4]} was clicked!")
                            elif (i[4] == "Achievements"):
                                print(f"{i[4]} was clicked!")
                            elif (i[4] == "Credits"):
                                print(f"{i[4]} was clicked!")
                            elif (i[4] == "Quit"):
                                pg.quit()
                                sys.exit()
                elif (self.mode == "play"):
                    # game interactive event logic
                    pass
            elif event.type == pg.VIDEORESIZE:
                self.screen = pg.display.set_mode((event.w, event.h), res_mode)
                if (self.mode == "menu"):
                    self.scale = pg.transform.scale(self.menu.bg_img,
                                                    (event.w, event.h))
                elif (self.mode == "play"):
                    # sizable image background
                    pass

    """
    Add function docstring here.
    """
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
