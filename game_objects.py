import pygame
from settings import screen
from settings import IMAGES_PATH

class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
        
    def show(self):
        screen.blit(self.img, (self.x, self.y))

class Spaceship(GameObject):
    def __init__(self):
        super().__init__()
        self.put_img(IMAGES_PATH['spaceship'])
        self.change_size(50, 80)
        self.move = 5

class Bullet(GameObject):
    def __init__(self):
        super().__init__()
        self.put_img(IMAGES_PATH['bullet'])
        self.change_size(5, 15)
        self.move = 15

class Enemy(GameObject):
    def __init__(self):
        super().__init__()
        self.put_img(IMAGES_PATH['enemy'])
        self.change_size(40, 40)
        self.move = 1