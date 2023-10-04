import pygame, sys, random
from pygame.locals import *

class Globaless():
    def __init__(self):
    #Atributos de pantalla
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.seleccion_terreno = 0
        self.puntos_terreno1 = [(260, 720), (260, 390), (350, 370), (390, 380), (430, 410), (460, 450),
                                    (470, 460), (520, 500), (550, 510), (570, 505), (580, 500), (600, 490),
                                    (740, 250), (770, 240), (800, 235), (830, 240), (850, 250), (960, 430),
                                    (980, 440), (990, 445), (1020, 450), (1050, 445), (1070, 435), (1080, 430),
                                    (1140, 330), (1150, 320), (1180, 315), (1220, 315), (1240, 320), (1280, 330),
                                    (1400, 800)]
        self.puntos_terreno2 = [(260, 720), (260, 420), (350, 420), (410, 470), (480, 470), (540, 390),
                        (620, 390), (660, 395), (760, 280), (830, 280), (880, 400), (960, 400),
                        (1020, 350), (1090, 350), (1130, 430), (1170, 430), (1200, 350), (1280, 350),
                        (1400, 800)]
        self.puntos_terreno3 = [(260, 720), (260, 280), (330,280), (380,370), (420,370), (440,340), (490,340), (570,345), (630,450),
                        (700,450), (770,200), (910,200), (990,390), (1090,390), (1150,290), (1280,290)
                        ,(1400, 800)]
        self.PANTALLA = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.ancho_gris = 260
        #Atributos balas
        self.bala_chica = 60
        self.bala_mediana = 80
        self.bala_grande = 100
        self.daño_bala_c = 30
        self.daño_bala_m = 40
        self.daño_bala_g = 50
        self.unidades_cyg = 3
        self.unidades_m = 10

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
        self.font2 = pygame.font.Font(None, 50)
        self.font3 = pygame.font.Font(None, 100)

    def generar_terreno(self):
        if self.seleccion_terreno == 0:
            self.seleccion_terreno = random.randint(1,3)
        if (self.seleccion_terreno == 1):
            pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno1)
        elif (self.seleccion_terreno == 2):
            pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno2)
        else:
            pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno3)
        pygame.draw.rect(self.PANTALLA,self.grisclaro,(0,0,self.ancho_gris,self.HEIGHT))

