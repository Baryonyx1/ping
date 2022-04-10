#Создай собственный Шутер!

from pygame import *
from pygame import *
from random import randint

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,scale_x,scale_y):
        super().__init__()
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = transform.scale(image.load(player_image), (self.scale_x, self.scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class rocket(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class rocket1(Gamesprite):
    def update(self):
        if keys_pressed[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y < win_width - 80:
            self.rect.y += self.speed

  


        

win_width = 700
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("ff.jpg"), (win_width, win_height))
player1 = rocket('f.png',5, win_height - 80, 4,100,100)
player2 = rocket('f.png',5, win_height - 80, 4,100,100)

monsters = sprite.Group()

game = True
clock = time.Clock()
FPS = 60


h = False
l = 0

while game:
    
    player1.update()
    player1.reset()
    display.update()
    clock.tick(FPS)
