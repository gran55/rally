import pygame as pg

SIZE = WIDTH, HEIGHT =800, 600 
GREY =(128, 128, 128)

pg.init()
pg.display.set_caption('NFS Underground')
screen = pg.display.set_mode(SIZE)


class Car(pg.sprite.Sprite):
    def __init__(self):
       pg.sprite.Sprite.__init__(self)
       self.image = pg.image.load('Image/car3.png')
    

car3 = Car()
car3_image = car3.image
car3_w, car3_h = car3.image.get_width(), car3.image.get_height()
car3.x, car3.y = (WIDTH - car3_w) // 2, (HEIGHT - car3_h) // 2


game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    car3.y -= 1
    if car3.y < -car3_h:
       car3.y = HEIGHT

    screen.fill(GREY)
    screen.blit(car3_image, (car3.x, car3.y))
    pg.display.update()
    pg.time.wait(1)