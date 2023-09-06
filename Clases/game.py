from typing import Any
from pygame.locals import *
import bala
import pygame, sys, math
#from boton import Button

pygame.init()

FPS= 60
RELOJ= pygame.time.Clock()
HEIGHT = 1280
WIDTH = 720

DISPLAYSURF = pygame.display.set_mode((HEIGHT,WIDTH))

pygame.display.set_caption("Los amantes de los tanques")

#COSAS DE LA BALA
vel = 70
angulo = math.pi/180 * 120
sprites = pygame.sprite.Group()
bala_prueba = bala.Balala(vel,angulo)
sprites.add(bala_prueba)

while True: 
    pygame.display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
    pygame.display.update()
    DISPLAYSURF.fill((0,0,0))
    #COSAS DE SPRITES
    sprites.update()
    sprites.draw(DISPLAYSURF)

    #control de fps
    RELOJ.tick(FPS)