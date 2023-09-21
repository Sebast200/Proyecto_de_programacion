import math, pygame, sys, globales, tanque, bala, random, interfaz
from pygame.locals import *

#DECLARACIONES
pygame.init()
interfaz = interfaz.Interfazz()
#variables globales
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()
#pantalla
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanque Volador")

#imagenes
icono = pygame.image.load("cosas tanques/programa principal/imagenes/tanque.png")
pygame.display.set_icon(icono)
#fondo
fondo = pygame.image.load("cosas tanques/programa principal/imagenes/fondo.png")
DISPLAYSURF.blit(fondo, (0,0))

#jugador 1
skin1 = pygame.image.load("cosas tanques/programa principal/imagenes/skin1.png")
skin2 = pygame.image.load("cosas tanques/programa principal/imagenes/skin2.png")

#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.ROJO,random.randint(vGlobales.ancho_gris,vGlobales.WIDTH/2))
tanque2 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.WIDTH/2, vGlobales.WIDTH))
bala1 = bala.Balas()
sprites.add(tanque1)
sprites.add(tanque2)
sprites.add(bala1)
a = []


while True:
    #dibujo de la pantalla
    DISPLAYSURF.blit(fondo,(0,0))
    vGlobales.terreno()
    #interfaz
    interfaz.interfaz()
    

    #bucle para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            interfaz.click_mouse(event.pos,bala1, tanque2)

        if event.type == pygame.KEYDOWN:
            interfaz.escribir(event)



    #SPRITES
    tanque1.update()
    tanque2.update()
    bala1.update(tanque2)
    sprites.draw(DISPLAYSURF)

    if (bala1.i % 5) == 0 and bala1.caida == True :
        a = a + [(bala1.rect.x, bala1.rect.y)]
    i=0
    while (i<len(a)):
        pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(a[i]),5)
        i+=1
    print("-")

    #Skins
    DISPLAYSURF.blit(skin1, (tanque1.rect.x-15,tanque1.rect.y-10))
    DISPLAYSURF.blit(skin2, (tanque2.rect.x-25,tanque2.rect.y-10))




    interfaz.print_interfaz()

    pygame.display.flip()
    RELOJ.tick(vGlobales.FPS)
