import math, pygame, sys, globales, tanque, bala, random
from pygame.locals import *

#DECLARACIONES
pygame.init()
#variables globales
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()
#pantalla
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanque Volador")
print("a")

#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(280,620))
tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint(660,1000))
bala1 = bala.Balas()
sprites.add(tanque1)
sprites.add(tanque2)
sprites.add(bala1)


while True:
    pygame.display

    #bucle para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    pygame.display.update()

    #dibujo de la pantalla
    DISPLAYSURF.fill(vGlobales.celeste)
    vGlobales.terreno()

    #SPRITES
    sprites.update()
    #bala1.colision_Tanke((tanque1, tanque2))
    sprites.draw(DISPLAYSURF)

    
    if event.type == pygame.MOUSEBUTTONUP:
        bala1.disparar(math.pi/180 * 130, 70,tanque1.rect.midtop)


    RELOJ.tick(vGlobales.FPS)
