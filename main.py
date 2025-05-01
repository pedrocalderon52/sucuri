import pygame as pg
from Button import Button
from text import Text


pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

pg.display.set_caption("Sucuri")

BG_COLOR = (13, 13, 13)

running = True

screen.fill(BG_COLOR)

button1 = Button(coords = (300, 200), dimensions = (90, 90), bg_color = (0, 255, 0), hover_bg_color = (20, 180, 20))
buttons_list = [button1]

title = Text("Su", 128, (73, 135, 50), "fonts/SankofaDisplay-Regular.ttf", hover_color= (255, 0, 0))

while running:
    mouse = pg.mouse.get_pos()
    button1.print_button(screen, mouse)
    title.display_text(screen, (620, 100), mouse)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
        if ev.type == pg.MOUSEBUTTONDOWN:
            for b in buttons_list:
                if b.is_inside_button(mouse):
                    b.button_press()

    


