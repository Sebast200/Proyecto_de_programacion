import pygame, sys
from pygame.locals import *
pygame.init()

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
fuerzaG = 2
direccion = True
pos_x, pos_y = 300, 0
puntos_terreno = [(200,720),(200,500),(300,450),(400,400),(600,450),(700,500),(800,550),(900,600),(1000,550),(1280,720)]

def terreno():
    pygame.draw.polygon(DISPLAYSURF,verde,puntos_terreno)
    pygame.draw.rect(DISPLAYSURF,gris,(0,0,260,720))
    pygame.draw.rect(DISPLAYSURF,gris,(1020,0,260,720))
    
while True: 
    DISPLAYSURF.fill(celeste)
    terreno()
    pygame.draw.rect(DISPLAYSURF,ROJO,(pos_x, pos_y,100,50))
    pygame.draw.rect(DISPLAYSURF,AZUL,(900, pos_y,100,50))
    #-----implementacion de colision
    if direccion == True:
        if pos_y < (540 - 50):
            pos_y += fuerzaG
        else:
            direccion = False
    #-----implementacion de colision
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()