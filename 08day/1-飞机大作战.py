import pygame

pygame.image.lord("./images/images")
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load(
hero = pygame.image.load(
herorect = pygame.Rect(200,500,120.120)#创建长方形
clock = pygame.time.Clock()#创建游戏时钟

enemy = EnemySprite()
enemy = EnemySprite()
enemy1.rect.x = 50
enemy.rect.y = 700
enemy.speed = -2
enemy_group = pygame.sprite.Group(enemy,enemy)

while True:
    clock.tick(60)#一秒刷新60次
    herorect.y-=1#相当速度
    screen.blit(bg,(0,0))
    screen.blit(hero,herorect)
    if herorect.bottom <= 0:#控制飞机返航
        herorect.top = 700
        enemy_group.update()
        enemy_group.draw(screen)
    pygame.display.update()#更新



