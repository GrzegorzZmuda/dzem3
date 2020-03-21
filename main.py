import pygame
import pygame
import numpy as np
import pygame.surfarray as sfr
import time
import random
import math
from sys import exit

rd=0
rstate=0


tab=np.zeros((10,4,3))



class klocek():
    def __init__(self, rot):
        self.posx=200
        self.posy = 600
        self.rt=rot


def rotdir(a):
    if a==1:
        return 0
    else:
        return 1


def rotstt(a,b):
    if b==1:
        if a<360:
            a=a+0.2
        else:
            a=0
    if b == 0:
        if a>0:
            a=a-0.2
        else:
            a=359
    return a




pygame.init()
screen = pygame.display.set_mode((400,700))
points=0
actual=np.zeros((400,700))
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render(str(points), True, (200, 200, 200), (0, 0, 0))
Running=True

gamearea=np.full((400,600,3),200)
lowarea=np.full((400,100,3),100)
treeimg = pygame.image.load('a.png')


load=input()
for i in range(40):
    if i<len(load):
        if load[i]=='a':
            tab[i//4][i%4][0]=200
            tab[i // 4][i % 4][1]=255
            tab[i // 4][i % 4][2] =255
        else:
            tab[i//4][i%4][0]=200
            tab[i // 4][i % 4][1]=200
            tab[i // 4][i % 4][2] =200
    else:
        tab[i // 4][i % 4][0] = 200
        tab[i // 4][i % 4][1] = 200
        tab[i // 4][i % 4][2] = 200

print(tab)

while Running:
    text = font.render(str(points), True, (255, 255, 255), (100, 100, 100))


    surf1 = pygame.surfarray.make_surface(gamearea)
    surf2 = pygame.surfarray.make_surface(lowarea)
    surf3 = pygame.surfarray.make_surface(tab)

    screen.blit(surf1, (0, 0))
    screen.blit(surf2,  (0, 600))
    screen.blit(text, (0, 650))
    screen.blit(pygame.transform.rotate(treeimg,rstate), (200, 600))
    screen.blit(pygame.transform.scale(surf3, (400, 160)), (0, 0))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rstate = rotstt(rstate, rd)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                rd=rotdir(rd)

