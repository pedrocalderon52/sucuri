import pygame as pg
class Button():
    def __init__(self, coords, dimensions, bg_color = (255, 0, 0), border_color = None, hover_bg_color = (210, 10, 10), hover_border_color = None, command = None, args = None):
        """
        coords: tuple(float, float) = X and Y coordinates of the starting point\n
        dimensions: tuple(float, float) = width and height of the rectangle\n
        bg_color: tuple(int, int, int) = color of the button's background (default: White)\n
        border_color: tuple(int, int, int) | None = color of the button's border (default: None)\n
        hover_bg_color: tuple(int, int, int) = color of the button's background when in hover mode (default: gray)\n
        hover_border_color: tuple(int, int, int) | None = color of the button's border when in hover mode (default: None)

        
        """


        self.posx, self.posy = coords
        self.width, self.height = dimensions
        self.bg_color = bg_color
        self.border_color = border_color
        self.hover_bg_color = hover_bg_color
        self.hover_border_color = hover_border_color
        self.command = command


    
    def is_inside_button(self, mouse):
        return self.posx <= mouse[0] <= self.posx + self.width and self.posy <= mouse[1] <= self.posy + self.height 
    

    def print_button(self, screen, mouse):
        if self.is_inside_button(mouse):
            if self.hover_border_color is not None:
                pg.draw.rect(screen, self.hover_bg_color, ((self.posx, self.posy), (self.width, self.height)))
                pg.draw.rect(screen, self.hover_border_color, ((self.posx, self.posy), (self.width, self.height)), width = 3)
            else:
                pg.draw.rect(screen, self.hover_bg_color, ((self.posx, self.posy), (self.width, self.height)))
        else:
            if self.border_color is not None:
                pg.draw.rect(screen, self.bg_color, ((self.posx, self.posy), (self.width, self.height)))
                pg.draw.rect(screen, self.border_color, ((self.posx, self.posy), (self.width, self.height)), width = 3)
            else:
                pg.draw.rect(screen, self.bg_color, ((self.posx, self.posy), (self.width, self.height)))
        
        pg.display.flip()


    def button_press(self):
        if self.command:
            self.command()
