import pygame as pg

SIZE = WIDTH, HEIGHT =800, 600 
GREY =(128, 128, 128)
GREEN = (0, 128, 0)
WHITE = (200, 200, 200)

pg.init()
pg.display.set_caption('NFS Underground')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()
bg_image_2_rect = bg_image.get_rect(topleft=(0, HEIGHT))


def bg():
    pg.draw.line(screen,  GREEN, (20, 0), (20, 600), 40)
    pg.draw.line(screen,  GREEN, (780, 0), (780, 600), 40)
    for xx in range(10):
        for yy in range(10):
            pg.draw.line(
                screen, WHITE,
                (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60), 
                (40 + xx * 80,600 if xx == 0 or xx == 9 else 50 + yy *60), 5)
   


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
    #bg()
    screen.blit(car3_image, (car3.x, car3.y))
    screen.blit(bg)
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'NFS Underground       FPS: {int(clock.get_fps())}')
    
#pg.image.save(screen, 'road.jpg')