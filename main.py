import pygame as pg
from Button import Button

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

running = True


button1 = Button((300, 200), (90, 90), (0, 255, 0), (20, 180, 20))
while running:
    mouse = pg.mouse.get_pos()
    button1.print_button(screen, mouse)
    


