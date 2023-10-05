
from pygame import *
from random import randint

win_width= 400
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('pole.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_R(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    

player1 = Player('racket.png', 5, 100,  10, 65, 65)
player2 = Player('racket.png', 320, 100,  10, 65, 65)
ball = GameSprite('ball.jpg', 170, 500, 5, 60,60)
FPS = 60 
clock = time.Clock()
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    window.blit(background,(0,0))
    player1.update_L()
    player2.update_R()
    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)




