import pygame, sys
from pygame.locals import *

class Globaless():
    def __init__(self):
    #COSAS DE LA PANTALLA
        self.WIDTH = 1000
        self.HEIGHT = 650
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
        self.FPS = (60)
        RELOJ = pygame.time.Clock()
