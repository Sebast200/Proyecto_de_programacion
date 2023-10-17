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
        self.puntos_terreno2 = [(260, 720), (260, 440), (290, 430), (350, 420), (370, 430), (375,440), (380,450), (385,460), (390,470), 
                        (410, 500), (430,520), (450, 520), (480, 500), (540, 390), (550,380), (580, 400),
                        (620, 390), (660,415), (680, 420), (700, 410),  (760, 280), (770, 270), (780,265), (810,265), (820, 270), (830, 280), 
                        (880, 435), (900,450), (920, 455), (940,450),  (960, 435),
                        (1020, 350), (1050, 335), (1070, 340), (1090, 350), (1130, 420), (1140,425), (1150,427), (1160,425), (1170, 420), (1200, 350), 
                        (1210, 347), (1220,350), (1250, 360), (1280, 373),
                        (1400, 800)]
        self.puntos_terreno3 = [(260, 720), 
                        (260, 280), (270,275), (310,275), (330,280), (380,390), (390,395), (400,397), (410,395), (420,390), 
                        (440,340), (450,335), (470,325), (490,325), (520,325), (540,330), (555,335), (570,345), 
                        (620,450), (640,480), (650,490), (660,495), (670,495), (680,490), (690,480), (700,450), 
                        (770,200), (790,192), (800,190), (820,185), (860,185), (880,190), (890,192), (910,200), 
                        (990,390), (1005,410), (1020,420), (1030,425), (1050,425), (1060,420), (1075,410), (1090,390), 
                        (1150,290), (1180,285), (1230,290), (1280,305)
                        ,(1400, 800)]
        self.PANTALLA = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.ancho_gris = 260
        #Atributos balas
        self.bala_chica = 60         #Radio
        self.bala_mediana = 80       #Radio  
        self.bala_grande = 120       #Radio
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
        self.verde_oscuro = (25,142,13)

        #FPS
        self.FPS = (90)
        RELOJ = pygame.time.Clock()

        #Fuente
        self.font = pygame.font.Font(None,36)
        self.font2 = pygame.font.Font(None,50)
        self.font3 = pygame.font.Font(None,100)
        self.font4 = pygame.font.Font(None,30)

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

