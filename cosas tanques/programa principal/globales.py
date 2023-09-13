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
        #Agregue un gris mas claro para apegarme al diseño de canva
        self.grisclaro = (217,217,217)
        #Agregue un rojo mas oscuro para apegarme al diseño de canva
        self.rojo_oscuro = (189,17,17)
        #FPS
        self.FPS = (90)
        RELOJ = pygame.time.Clock()
        #Fuente
        self.font = pygame.font.Font(None, 36)

    def terreno(self):
        pygame.draw.polygon(self.PANTALLA,self.verde,self.puntos_terreno)
        pygame.draw.rect(self.PANTALLA,self.grisclaro,(0,0,260,720))
        pygame.draw.rect(self.PANTALLA,self.grisclaro,(1020,0,260,720))

    def interfaz(self):
    #CREACION DE INTERFAZ PARA JUGADOR 1

    #Texto que dice jugador 1 con letras azules
    text_jugador1 = "Jugador 1"
    text_surface_jugador1 = self.font.render(text_jugador1, True, self.AZUL)
    text_surface_jugador1_rect = text_surface_jugador1.get_rect(center = (120,40))

    #Rectangulo de color gris que dira Espera...
    pygame.draw.rect(self.PANTALLA, self.gris, (20,80,220,40))
    text_turno_jugador1 = "Espera..."
    text_surface_turno_jugador1 = self.font.render(text_turno_jugador1, True, self.NEGRO)
    text_surface_turno_jugador1_rect = text_surface_turno_jugador1.get_rect(center = (120,100))
    #Por ahora dejare el rectangulo gris para ambos lados hasta que definamos bien el
    #metodo de turnos y que por ende vaya cambiando de color dependiendo de los turnos de los jugadores

    #Texto que dice Angulo...
    text_angulo_jugador1 = "Angulo:"
    text_surface_angulo_jugador1 = self.font.render(text_angulo_jugador1, True, self.NEGRO)
    text_surface_angulo_jugador1_rect = text_surface_angulo_jugador1.get_rect(center = (80,200))

    #Texto que dice Velocidad inicial
    #Forma 1
    '''
    text_velocidad_inicial_jugador1 = "Velocidad\n   inicial:" #hay espacios para intentar centrar la palabra inicial
    lineas = text_velocidad_inicial_jugador1.split("\n")
    line_height = self.font.get_linesize()
    y = 260
    for linea in lineas:
        text_surface = self.font.render(linea, True, self.NEGRO)
        x = 80
        self.PANTALLA.blit(text_surface, (x, y))
        y += line_height
    '''
    #Forma 2 (posiblemente la mas facil pero pajera(?))
    #Esta forma consiste en crear dos textos, uno que diga velocidad y otra que diga inicial, para intentar ser un poco mas ordenado xd
    text_velocidad_jugador1 = "Velocidad"
    text_surface_velocidad_jugador1 = self.font.render(text_velocidad_jugador1, True, self.NEGRO)
    text_surface_velocidad_jugador1_rect = text_surface_velocidad_jugador1.get_rect(center = (80,360))
    
    text_inicial_jugador1 = "inicial:"
    text_surface_inicial_jugador1 = self.font.render(text_inicial_jugador1, True, self.NEGRO)
    text_surface_inicial_jugador1_rect = text_surface_inicial_jugador1.get_rect(center = (80,390))


    self.PANTALLA.blit(text_surface_jugador1,text_surface_jugador1_rect)
    self.PANTALLA.blit(text_surface_turno_jugador1,text_surface_turno_jugador1_rect)
    self.PANTALLA.blit(text_surface_angulo_jugador1,text_surface_angulo_jugador1_rect)
    #Esto forma parte de la forma 2
    self.PANTALLA.blit(text_surface_velocidad_jugador1,text_surface_velocidad_jugador1_rect)
    self.PANTALLA.blit(text_surface_inicial_jugador1,text_surface_inicial_jugador1_rect)
    #de aqui a abajo ya no forma parte de la forma 2 xd

    #Aqui me separare de lo otro que hice para no confundirme, de aqui a abajo solo hare el cubo rojo que dira recarga...
    pygame.draw.rect(self.PANTALLA, self.rojo_oscuro, (20,600,220,80))
    text_boton_jugador1 = "Recarga"
    text_surface_boton_jugador1 = self.font.render(text_boton_jugador1, True, self.BLANCO)
    text_surface_boton_jugador1_rect = text_surface_boton_jugador1.get_rect(center = (130,640))
    self.PANTALLA.blit(text_surface_boton_jugador1,text_surface_boton_jugador1_rect)
    #FIN DE CREACION DE INTERFAZ PARA JUGADOR 1
    #-----
    #INICIO DE CREACION DE INTERFAZ PARA JUGADOR 2
    #Esto basicamente va a ser un copia pega de la interfaz del jugador 1 pero con un ligero cambio de coordenadas

    #Texto que dice jugador 2 con letras rojas
    text_jugador2 = "Jugador 2"
    text_surface_jugador2 = self.font.render(text_jugador2, True, self.ROJO)
    text_surface_jugador2_rect = text_surface_jugador2.get_rect(center = (1150,40))

    #Rectangulo de color gris que dira Espera...
    pygame.draw.rect(self.PANTALLA, self.gris, (1040,80,220,40))
    text_turno_jugador2 = "Espera..."
    text_surface_turno_jugador2 = self.font.render(text_turno_jugador2, True, self.NEGRO)
    text_surface_turno_jugador2_rect = text_surface_turno_jugador2.get_rect(center = (1150,100))

    #Texto que dice Angulo...
    text_angulo_jugador2 = "Angulo:"
    text_surface_angulo_jugador2 = self.font.render(text_angulo_jugador2, True, self.NEGRO)
    text_surface_angulo_jugador2_rect = text_surface_angulo_jugador2.get_rect(center = (1100,200))

    #Escribire velocidad inicial del jugador 2 de la forma pajera xdd
    text_velocidad_jugador2 = "Velocidad"
    text_surface_velocidad_jugador2 = self.font.render(text_velocidad_jugador2, True, self.NEGRO)
    text_surface_velocidad_jugador2_rect = text_surface_velocidad_jugador2.get_rect(center = (1100,360))
    
    text_inicial_jugador2 = "inicial:"
    text_surface_inicial_jugador2 = self.font.render(text_inicial_jugador2, True, self.NEGRO)
    text_surface_inicial_jugador2_rect = text_surface_inicial_jugador2.get_rect(center = (1100,390))
    
    self.PANTALLA.blit(text_surface_jugador2,text_surface_jugador2_rect)
    self.PANTALLA.blit(text_surface_turno_jugador2, text_surface_turno_jugador2_rect)
    self.PANTALLA.blit(text_surface_angulo_jugador2,text_surface_angulo_jugador2_rect)
    self.PANTALLA.blit(text_surface_velocidad_jugador2,text_surface_velocidad_jugador2_rect)
    self.PANTALLA.blit(text_surface_inicial_jugador2,text_surface_inicial_jugador2_rect)

    #Creacion del cubito rojo
    pygame.draw.rect(self.PANTALLA, self.rojo_oscuro, (1040,600,220,80))
    text_boton_jugador2 = "Recarga"
    text_surface_boton_jugador2 = self.font.render(text_boton_jugador2, True, self.BLANCO)
    text_surface_boton_jugador2_rect = text_surface_boton_jugador2.get_rect(center = (1150,640))
    self.PANTALLA.blit(text_surface_boton_jugador2,text_surface_boton_jugador2_rect)


