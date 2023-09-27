import pygame, sys
from pygame.locals import *

class Globaless():
    def __init__(self):
    #Atributos de pantalla
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.puntos_terreno = [(260,720),(260,540),(350,520),(390,530),(430,560),(460,600),
                                    (470,610),(520,650),(550,660),(570,655),(580,650),(600,640),
                                    (740,400),(770,390),(800,385),(830,390),(850,400),(960,580),
                                    (980,590),(990,595),(1020,600),(1050,595),(1070,585),(1080,580),
                                    (1140,480),(1150,470),(1180,465),(1220,465),(1240,470),(1280,480),(1400,800)]
        self.PANTALLA = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.ancho_gris = 260

        #COLORES
        self.NEGRO = (0,0,0)
        self.BLANCO = (255,255,255)
        self.ROJO = (255,0,0)
        self.AZUL = (0,0,255)
        self.verde = (81,255,64)
        self.gris = (177,177,177)
        self.celeste = (53,197,255)
        self.grisclaro = (217,217,217)
        self.rojo_oscuro = (189,17,17)

        #FPS
        self.FPS = (90)
        RELOJ = pygame.time.Clock()

        #Fuente
        self.font = pygame.font.Font(None,36)

    def terreno(self):
        pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno)
        pygame.draw.rect(self.PANTALLA,self.grisclaro,(0,0,self.ancho_gris,self.HEIGHT))

