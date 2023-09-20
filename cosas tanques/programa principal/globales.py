import pygame, sys
from pygame.locals import *

class Globaless():
    def __init__(self):
    #COSAS DE LA PANTALLA
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.puntos_terreno = [(260,720),(260,540),(350,520),(390,530),(430,560),(460,600),
                                    (470,610),(520,650),(535,655),(560,650),(580,640),(610,600),(615,590),
                                    (650,510),(660,470),(665,420),(680,380),(700,370),(715,365),
                                    (755,365),(775,370),(790,390),(820,450),(840,510),(860,560),(890,600),
                                    (910,610,),(940,615),(960,610),(980,600),(1000,580),(1030,530),(1070,480),
                                    (1100,470),(1120,475),(1160,480),(1195,520),(1210,560),(1260,630),(1350,720),(1400,800)]
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

