import pygame, sys, globales, math
from pygame.locals import *

class Tankes (pygame.sprite.Sprite):
    #constructor
    def __init__(self, _color,posicion_inicial):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.pTer = self.vGlobales.puntos_terreno
        
        
        #atributos propios
        self.largo = 50
        self.alto = 25
        self.caida = True

        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, self.vGlobales.HEIGHT//2)

        #actualiza la posicion del tanque
    def update(self):
        incremento = 5
        self.caida_Tanque()
        if (self.caida):
            self.rect.y += incremento
        else:
            self.caida = False

    def distancia (self,x1,x2,y1,y2):
        valor = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        return int(valor)

    def caida_Tanque(self):
        i = 1
        posicion = 0
        #busca el que rango de puntos se encuentra el centro del tanque con respecto a la matriz del terreno
        while (i<len(self.pTer)-2):
            if (self.rect.midbottom[0] >= self.pTer[i][0]) and (self.rect.midbottom[0] <= self.pTer[i+1][0]):
                posicion = i
                i=len(self.pTer)+1
            else:
                i=i+1
        i = posicion

        if (self.distancia(self.rect.midbottom[0], self.pTer[i][0], self.pTer[i][1], self.rect.midbottom[1]) + (self.distancia(self.pTer[i+1][0], self.rect.midbottom[0], self.rect.midbottom[1], self.pTer[i+1][1])) <= self.distancia(self.pTer[i][0], self.pTer[i+1][0], self.pTer[i+1][1], self.pTer[i][1])):
            self.caida = False

        
        
        