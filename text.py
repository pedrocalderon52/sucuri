import pygame as pg

class Text():
    def __init__(self, content, size, color, font=None, hover_color=None):
        self.content = content
        self.size = size
        self.color = color
        self.font = font
        self.hover_color = hover_color


    def display_text(self, screen: pg.Surface, pos: tuple[int, int], mouse: tuple[int, int]):
        text_font = pg.font.Font(self.font, self.size)
        text_surface = text_font.render(self.content, True, self.color)
        text_width, text_height = text_surface.get_size()

        if pos[0] <= mouse[0] <= pos[0] + text_width and pos[1] <= mouse[1] <= pos[1] + text_height:
            color = self.hover_color if self.hover_color else self.color
        else:
            color = self.color

        text_surface = text_font.render(self.content, True, color)
        screen.blit(text_surface, pos)
