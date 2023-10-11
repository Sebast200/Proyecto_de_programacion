import pygame, sys, globales, math
from pygame.locals import *

class Tankes (pygame.sprite.Sprite):
    #Constructor
    def __init__(self, _color,posicion_inicial):
        super().__init__()
        self.vGlobales = globales.Globaless()

        #Atributos propios
        self.vida = 100
        self.largo = 15
        self.alto = 10
        self.caida = True
        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, 200)

        #actualiza la posicion del tanque
    def update(self):
        incremento = 3
        self.caida_Tanque()
        if (self.caida):
            self.rect.y += incremento

    def caida_Tanque(self):
        #Colision con color del terreno
        color = self.vGlobales.PANTALLA.get_at((self.rect.midbottom[0],self.rect.midbottom[1]))
        color = (color[0], color[1], color[2])
        if (color == self.vGlobales.verde):
            self.caida = False
        else:
            self.caida = True