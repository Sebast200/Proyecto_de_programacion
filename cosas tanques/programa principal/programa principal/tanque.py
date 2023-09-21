import pygame, sys, globales, math
from pygame.locals import *

class Tankes (pygame.sprite.Sprite):
    #constructor
    def __init__(self, _color,posicion_inicial):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.pTer = self.vGlobales.puntos_terreno
        
        
        #atributos propios
        self.largo = 25
        self.alto = 15
        self.radio = 20
        self.caida = True

        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, 200)

        #actualiza la posicion del tanque
    def update(self):
        #pygame.draw.circle(self.vGlobales.PANTALLA, self.vGlobales.BLANCO, self.rect.center,self.radio)
        incremento = 3
        self.caida_Tanque()
        if (self.caida):
            self.rect.y += incremento
        else:
            self.caida = False

    def distancia (self,x1,x2,y1,y2):
        valor = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        return int(valor)

    def caida_Tanque(self):
        
        color = self.vGlobales.PANTALLA.get_at((self.rect.midbottom[0],self.rect.midbottom[1]))
        color = (color[0], color[1], color[2])

        
        if (color == self.vGlobales.verde):
            self.caida = False


        
        
        