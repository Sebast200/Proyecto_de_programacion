import pygame, sys, globales
from pygame.locals import *

class Tankes (pygame.sprite.Sprite):
    #constructor
    def __init__(self, _color,posicion_inicial):
        super().__init__()
        self.vGlobales = globales.Globaless()
        
        
        #atributos propios
        self.largo = 100
        self.alto = 50

        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, self.vGlobales.HEIGHT//2)
        """#pantalla
        self.COLOR = _color
        self.pantalla = _pantalla
        impresion del tanque
        self.tanque2 = pygame.draw.rect(vGlobales.PANTALLA,self.COLOR,(900,500,self.largo,self.alto))
        print(self.tanque2)"""

        #actualiza la posicion del tanque
    def update(self):
        self.caida = True
        incremento = 5
        if (self.rect.bottom < self.vGlobales.HEIGHT):
            self.rect.y += incremento
        else:
            incremento = 0
            self.caida = False

        
        
        



    #imrpime el tanque
    def print (self, num):
        pygame.draw.rect(self.pantalla,self.COLOR,(900, num,self.largo,self.alto))
        