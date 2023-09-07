import math, pygame, sys, globales, tanque, bala
from pygame.locals import *

#DECLARACIONES
pygame.init()
#variables globales
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()
#pantalla
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanque Volador")
puntos_terreno = [(0,720),(0,540),(410,430),(540,520),(630,590),(670,590),(820,500),(980,600),(1020,620),(vGlobales.WIDTH,vGlobales.HEIGHT)]


#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.AZUL,300)
tanque2 = tanque.Tankes(vGlobales.ROJO,700)
bala1 = bala.Balas(tanque1.rect.center[0], tanque1.rect.center[1])
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
    DISPLAYSURF.fill(vGlobales.BLANCO)
    pygame.draw.polygon(DISPLAYSURF,vGlobales.verde,puntos_terreno)

    #SPRITES
    sprites.update()
    sprites.draw(DISPLAYSURF)

    if (tanque1.caida == False):  #angulo | velocidad
        bala1.disparar(math.pi/180 * 145, 90,tanque1.rect.center)

    RELOJ.tick(vGlobales.FPS)
