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
icono = pygame.image.load("imagenes/tanque.png")
pygame.display.set_icon(icono)
#fondo
fondo = pygame.image.load("imagenes/fondo.png")
DISPLAYSURF.blit(fondo, (0,0))

#jugador 1
skin1 = pygame.image.load("imagenes/skin1.png")
skin2 = pygame.image.load("imagenes/skin2.png")

#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.ancho_gris + 10,(vGlobales.WIDTH - vGlobales.ancho_gris)/2 + vGlobales.ancho_gris ))
tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint((vGlobales.WIDTH- vGlobales.ancho_gris)/2 + tanque1.rect.x, vGlobales.WIDTH - 10))
bala1 = bala.Balas()
sprites.add(tanque1)
sprites.add(tanque2)
sprites.add(bala1)
a = []

#Creacion de variables en main (por ahora)
turno_jugador = 2
turno_pasado = 0



while True:
    #dibujo de la pantalla
    DISPLAYSURF.blit(fondo,(0,0))
    vGlobales.terreno()
    #interfaz
    interfaz.interfaz()
    
    #proceso de cambio de turno
    if turno_jugador == 1 and turno_pasado == 0:
        turno_jugador = 2
        turno_pasado = 1
        print("Es el turno del jugador 2")
    elif turno_jugador == 2 and turno_pasado == 0:
        turno_jugador = 1
        turno_pasado = 1
        print("Es el turno del jugador 1")

    #bucle para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if bala1.caida != True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turno_jugador == 1:
                    turno_pasado = interfaz.click_mouse(event.pos,bala1,tanque1, turno_pasado, turno_jugador)
                    a.clear()
                else:
                    turno_pasado = interfaz.click_mouse(event.pos,bala1, tanque2, turno_pasado, turno_jugador)
                    a.clear()

        if event.type == pygame.KEYDOWN:
            interfaz.escribir(event)



    #SPRITES
    tanque1.update()
    tanque2.update()

    if turno_jugador == 1:
        bala1.update(tanque1,tanque2)
    else:
        bala1.update(tanque2, tanque1)
    sprites.draw(DISPLAYSURF)

    if (bala1.i % 5) == 0 and bala1.caida == True :
        a = a + [(bala1.rect.x, bala1.rect.y)]
    i=0
    while (i<len(a)):
        pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(a[i]),5)
        i+=1

    #Skins
    DISPLAYSURF.blit(skin1, (tanque1.rect.x-15,tanque1.rect.y-10))
    DISPLAYSURF.blit(skin2, (tanque2.rect.x-25,tanque2.rect.y-10))

    if (tanque1.vida == False or tanque2.vida == False):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()



    interfaz.print_interfaz()

    pygame.display.flip()
    RELOJ.tick(vGlobales.FPS)

