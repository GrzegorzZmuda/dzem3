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



def shot(ang,targ,pt):
    ls=[]
    temp=400
    for i in range(4):
        temp=temp+40
        x=200-math.sin(math.radians(ang))*temp
        if x>0 and x<400:
            ls.append([4-i-1,int(x//40)])

    if ls==[]:
        pygame.quit()
        exit()

    else:
        flag=False
        for i in range(len(ls)):
            if targ[ls[i][1]][ls[i][0]][1]==255:
                targ[ls[i][1]][ls[i][0]][0] = 200
                targ[ls[i][1]][ls[i][0]][1] = 200
                targ[ls[i][1]][ls[i][0]][2] = 200
                flag=True
                pt=pt+1
                d=ls[i][0]-1
                fl=True
                b=1
                while d>-1 and fl==True:
        
                    if targ[ls[i][1]][d][1]==255:
                        targ[ls[i][1]][d][0] = 200
                        targ[ls[i][1]][d][1] = 200
                        targ[ls[i][1]][d][2] = 200
                        d=d-1
                        b=b*2
                        pt = pt + 1+b
                        b = b * 2
                    else:
                        fl=False
                break
        if flag==False:
            i=len(ls)-1
            targ[ls[i][1]][ls[i][0]][0] = 200
            targ[ls[i][1]][ls[i][0]][1] = 255
            targ[ls[i][1]][ls[i][0]][2] = 255
            pt = pt - 2
    return pt


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                points=shot(rstate,tab,points)
