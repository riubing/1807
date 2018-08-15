import pygame

pygame.image.lord("./images/images")
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load(
hero = pygame.image.load(
herorect = pygame.Rect(200,500,120.120)#创建长方形
clock = pygame.time.Clock()#创建游戏时钟
while True:
    clock.tick(60)#一秒刷新60次
    herorect.y-=1#相当速度
    screen.blit(bg,(0,0))
    screen.blit(hero,herorect)
    if herorect.bottom <= 0:#控制飞机返航
        herorect.top = 700
    pygame.display.update()#更新



