"""
Zachary Meisner
menu.py

Add module docstring here
"""

from settings import pg, ft, FONT_PATH, MENU_BG_PATH, BTN_W_LOC, BTN_W, BTN_H

class Text:
    """
    Add class docstring here.
    """
    def __init__(self, app, size, name, color):
        self.app = app
        self.size = size
        self.name = name
        self.color = color
        self.font = ft.Font(FONT_PATH, self.size)
        self.area, self.rect = self.font.render(self.name, fgcolor=self.color)

    def render(self, off_x, off_y):
        """
        Add function docstring here.
        """
        x = (self.app.x - self.rect.width) / 2 * off_x
        y = (self.app.y - self.rect.height) / 2 * off_y
        return x, y

    def draw(self, offset_x, offset_y):
        """
        Add function docstring here.
        """
        x, y = self.render(offset_x, offset_y)
        self.font.render_to(self.app.app.app.screen, (x, y),text=self.name,
                            fgcolor=self.color, size=self.size)


class Button:
    """
    Add class docstring here.
    """
    def __init__(self, app, pos, size, text=''):
        self.app = app
        self.pos = pos[0], pos[1]
        self.size = size
        self.text = text
        self.font = pg.font.Font(pg.font.get_default_font(), self.size[1])
        self.area = pg.Surface((self.size[0], self.size[1]))

    def render(self, text, text_color):
        """
        Add function docstring here.
        """
        text_area = self.font.render(f"{text}", True, text_color)
        return text_area

    def draw(self, win, color, text_color):
        """
        Add function docstring here.
        """
        text_area = self.render(self.text, text_color)
        win.blit(self.area, (self.pos[0], self.pos[1]))
        win.blit(text_area, (self.pos[0]+1, self.pos[1]+5))
        self.area.fill((color))


class Menu:
    """
    Add class docstring here.
    """
    def __init__(self, app):
        self.app = app
        self.res = (self.x, self.y) = (self.app.app.x, self.app.app.y)
        self.bg_img = pg.image.load(MENU_BG_PATH)
        self.text_list = [("t1", 150, "Trivial Compute", "black", "title"),
                          ("t2", 80, "Team Byte-Builders", "black", "team")]
        self.btn_list = [("b1", (255, 255, 0), 350, (0, 0, 0), 'Play'),
                         ("b2", (255, 0, 0), 350, (0, 0, 0), 'Options'),
                         ("b3", (255, 0, 0), 350, (0, 0, 0), 'Mute'),
                         ("b4", (255, 0, 0), 350, (0, 0, 0), 'Achievements'),
                         ("b5", (0, 255, 0), 350, (0, 0, 0), 'Credits'),
                         ("b6", (0, 255, 0), 350, (0, 0, 0), 'Quit')]

        # Create the buttons on the main menu
        j = 0
        for i in self.btn_list:
            setattr(self, i[0], Button(self, ((self.x / 2 - BTN_W_LOC),
                                        i[2] + j), (BTN_W, BTN_H), i[4]))
            j += 75

        for i in self.text_list:
            setattr(self, i[0], Text(self, i[1], i[2], i[3]))

    def draw_menu(self):
        """
        Add function docstring here.
        """
        for i in self.text_list:
            text = getattr(self, i[0])
            if i[4] == "title":
                text.draw(1, 0)
            elif i[4] == "team":
                text.draw(1.9, 1.9)

        for i in self.btn_list:
            button = getattr(self, i[0])
            button.draw(self.app.app.screen, i[1], i[3])

    def update(self):
        """
        Add function docstring here.
        """
        pg.display.update()

    def draw(self):
        """
        Add function docstring here.
        """
        self.draw_menu()
