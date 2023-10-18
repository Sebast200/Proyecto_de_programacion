import pygame, sys, globales, math
from pygame.locals import *
from pygame import mixer

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
        self.distancia_caida = 0
        self.inmune= True
        self.a=2
        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, 200)
        self.color = self.vGlobales.BLANCO  #Por si el tanque llegase a salir de la pantalla se crea el self color para 
                                            #la colision, sujeto a cambios de ser necesario

        #actualiza la posicion del tanque
    def update(self):
        incremento = 3
        self.caida_Tanque()
        if (self.caida):
            self.rect.y += incremento
            
        else:
            self.vida = self.vida - self.distancia_caida
            print(self.vida)
            self.distancia_caida = 0

    def caida_Tanque(self):
        #Colision con color del terreno
        if self.rect.y < self.vGlobales.HEIGHT - self.alto:
            self.color = self.vGlobales.PANTALLA.get_at((self.rect.midbottom[0],self.rect.midbottom[1]))
            self.color = (self.color[0], self.color[1], self.color[2])
        if (self.color == self.vGlobales.verde or self.rect.y >= self.vGlobales.HEIGHT):
            self.caida = False
            self.inmune = False
        else:
            self.caida = True
            if not(self.inmune):
                self.distancia_caida += 0.5