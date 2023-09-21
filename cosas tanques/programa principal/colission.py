import pygame, sys
from pygame.locals import *
pygame.init()
from math import sqrt

DISPLAYSURF = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Tanque Volador")

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
verde = (81,255,64)
gris = (177,177,177)
celeste = (53,197,255)
tanque2 = pygame.draw.rect(DISPLAYSURF,AZUL,(900,500,100,50))
print(tanque2)
fuerzaG = 1
direccion = True
pos_x, pos_y = 400, 100
direccion2 = True
pos_x2, pos_y2 = 700,100
puntos_terreno = [(260,720),(260,540),(350,520),(390,530),(430,560),(460,600),
                                    (470,610),(520,650),(535,655),(560,650),(580,640),(630,600),(645,590),
                                    (670,510),(680,470),(675,420),(700,380),(700,370),(715,365),
                                    (755,365),(775,370),(790,390),(820,450),(840,510),(860,560),(890,600),
                                    (910,610,),(940,615),(960,610),(980,600),(1000,580),(1030,530),(1070,480),
                                    (1100,470),(1120,475),(1160,480),(1195,520),(1210,560),(1260,630),(1350,720),(1400,800)]

def distancia (x1,x2,y1,y2):
    valor = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return int(valor)
    

def terreno():
    pygame.draw.polygon(DISPLAYSURF,verde,puntos_terreno)
    pygame.draw.rect(DISPLAYSURF,gris,(0,0,260,720))
    
while True: 
    DISPLAYSURF.fill(celeste)
    terreno()
    pygame.draw.rect(DISPLAYSURF,ROJO,(pos_x, pos_y,10,10))
    pygame.draw.rect(DISPLAYSURF,AZUL,(pos_x2, pos_y2,10,10))
    #-----implementacion de colision
    if direccion == True:
        i = 1
        posicion = 0
        while (i<len(puntos_terreno)-2):
            if (pos_x >= puntos_terreno[i][0]) and (pos_x <= puntos_terreno[i+1][0]):
                posicion = i
                i=len(puntos_terreno)+1
            else:
                i=i+1
        i=posicion
        print(i)
        if (((distancia(pos_x,puntos_terreno[i][0],puntos_terreno[i][1],pos_y)) + 
            (distancia(puntos_terreno[i+1][0],pos_x,pos_y,puntos_terreno[i+1][1]))) <=
            distancia(puntos_terreno[i][0],puntos_terreno[i+1][0],puntos_terreno[i+1][1],puntos_terreno[i][1])):
            direccion = False
        else:
            pos_y += fuerzaG

    if direccion2 == True:
        i = 1
        posicion = 0
        while (i<len(puntos_terreno)-2):
            if (pos_x2 >= puntos_terreno[i][0]) and (pos_x2 <= puntos_terreno[i+1][0]):
                posicion = i
                i=len(puntos_terreno)+1
            else:
                i=i+1
        i=posicion
        print(i)
        if (((distancia(pos_x2,puntos_terreno[i][0],puntos_terreno[i][1],pos_y2)) + 
            (distancia(puntos_terreno[i+1][0],pos_x2,pos_y2,puntos_terreno[i+1][1]))) <=
            distancia(puntos_terreno[i][0],puntos_terreno[i+1][0],puntos_terreno[i+1][1],puntos_terreno[i][1])):
            direccion2 = False
        else:
            pos_y2 += fuerzaG
    #-----implementacion de colision
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()