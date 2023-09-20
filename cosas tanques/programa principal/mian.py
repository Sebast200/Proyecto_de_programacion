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
rect1 = skin1.get_rect()
skin2 = pygame.image.load("imagenes/skin2.png")

#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.ancho_gris,vGlobales.WIDTH/2))
tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint(vGlobales.WIDTH/2, vGlobales.WIDTH))
bala1 = bala.Balas()
sprites.add(tanque1)
sprites.add(tanque2)
sprites.add(bala1)




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
            interfaz.click_mouse(event.pos,bala1, tanque1.rect.midtop)

        if event.type == pygame.KEYDOWN:
            print("aa")
            interfaz.escribir(event)



    #SPRITES
    sprites.update()
    bala1.colision_Tanke((tanque1, tanque2))
    sprites.draw(DISPLAYSURF)

    #Skins
    DISPLAYSURF.blit(skin1, (tanque1.rect.x-15,tanque1.rect.y-10))
    DISPLAYSURF.blit(skin2, (tanque2.rect.x-25,tanque2.rect.y-10))




    interfaz.print_interfaz()

    pygame.display.flip()
    RELOJ.tick(vGlobales.FPS)
