import pygame, sys
from pygame.locals import *

class Globaless():
    def __init__(self):
    #COSAS DE LA PANTALLA
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.puntos_terreno = [(260,720),(260,540),(350,460),(410,430),(500,480),(540,520),(630,590),(670,590),(730,540),(820,500),(920,550),(980,600),(1020,620),(1280,720)]

        self.PANTALLA = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #COLORES
        self.NEGRO = (0,0,0)
        self.BLANCO = (255,255,255)
        self.ROJO = (255,0,0)
        self.AZUL = (0,0,255)
        self.verde = (81,255,64)
        self.gris = (177,177,177)
        self.celeste = (53,197,255)

        #FPS
        self.FPS = (90)
        RELOJ = pygame.time.Clock()

    def terreno(self):
        pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno)
        pygame.draw.rect(self.PANTALLA,self.gris,(0,0,260,720))
        pygame.draw.rect(self.PANTALLA,self.gris,(1020,0,260,720))

