import pygame
from MySprite import *
class PlaneGame(object):
    def __init__(self):
       s self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #self._create_sprites()
        self.clock = pygame.time.Clock()
        self.__create_sprites
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)



def start_game(self):
    while True:
        self.clock.tick(60)
        self.__event_handler()
        self.__check_collide()
        self.__update_sprites()
        pygame.display.update()
def __create_sprites(self):
    pass
def __event_handler(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            planeGame.__game_over()
        elif event.type == CREATE_ENEMY_EVENT:
            enemy = EnemySprite()
            self.enemy_group.add(enmey)
def __check_collide(self):
    pass
def __update_sprites(self):
    pass
@staticmethod
def __game_over():
    print("游戏结束")
    pygame.quit()
    exit()



if __name__ == '__name__':
    game = planeGame
    game.start_game()


