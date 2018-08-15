import pygame
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,imagename,speed=1)
        super().__init__()
        self.image = pygame.image.load(imagename)
        self.speed = speen

    def update(self):
        self.rect.y+=self.speed







class EnemySprite(GameSprite):
    def__init__(self):
        self.imagename = "./images/enemy0.png
        super().__init__(self,imagename)
    def update(self):
        super().update()
