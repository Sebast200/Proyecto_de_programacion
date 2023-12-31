import pygame, sys, globales, math
from pygame.locals import *
from pygame import mixer

class Tankes (pygame.sprite.Sprite):
    #Constructor
    def __init__(self, _color,posicion_inicial, gravedad, es_bot):
        super().__init__()
        self.vGlobales = globales.Globaless()
        #Atributos propios
        self.id = 0
        self.vida = 100
        self.largo = 15
        self.alto = 10
        self.kills = 0
        self.total_kills = 0
        self.suicidio = False
        self.cantidad_suicidios = 0
        self.caida = True
        self.distancia_caida = 0
        self.inmune = True #inmunidad para caida al spawnear
        self.image = pygame.Surface ((self.largo,self.alto))
        self.image.fill(_color)
        self.rect = self.image.get_rect()
        self.rect.center = (posicion_inicial, 100)
        self.color = self.vGlobales.BLANCO  #Por si el tanque llegase a salir de la pantalla se crea el self color para la colision
        self.unidades_c = 0
        self.unidades_m = 0
        self.unidades_g = 0
        self.gravedad = gravedad
        self.timepo = 0
        self.Yi = 100
        self.saldo = 10000
        self.bot = es_bot
        self.muerte_caida = False
        self.vivo = True

    #actualiza la posicion del tanque
    def update(self):
        self.caida_Tanque()
        if (self.caida):
            self.rect.y = self.Yi + 0.5 * self.gravedad * self.timepo**2*0.7
            self.timepo += 0.12
        else:
            self.vida = self.vida - int(self.distancia_caida*self.gravedad/10)
            self.distancia_caida = 0

    def caida_Tanque(self):
        if self.rect.y < self.vGlobales.HEIGHT - self.alto:
            self.color = self.vGlobales.PANTALLA.get_at((self.rect.midbottom[0],self.rect.midbottom[1]))
            self.color = (self.color[0], self.color[1], self.color[2])

        if self.caida == False and self.color != self.vGlobales.grisclaro:
            self.Yi = self.rect.y
            self.timepo = 0
        #Colision con color del terreno
        if (self.color == self.vGlobales.grisclaro or self.rect.y >= self.vGlobales.HEIGHT):
            self.caida = False
            self.inmune = False
        else:
            self.caida = True
            if not(self.inmune):
                self.distancia_caida += 0.5

    def comprar_bala(self, bala):
        if bala.tipo == self.vGlobales.bala_chica and self.saldo >= self.vGlobales.costo_bala_c:
            self.unidades_c += 1
            self.saldo = self.saldo - self.vGlobales.costo_bala_c

        if bala.tipo == self.vGlobales.bala_mediana and self.saldo >= self.vGlobales.costo_bala_m:
            self.unidades_m += 1
            self.saldo = self.saldo - self.vGlobales.costo_bala_m

        if bala.tipo == self.vGlobales.bala_grande and self.saldo >= self.vGlobales.costo_bala_g:
            self.unidades_g += 1
            self.saldo = self.saldo - self.vGlobales.costo_bala_g
    
    def vender_bala(self, bala):
        if bala.tipo == self.vGlobales.bala_chica and self.unidades_c >= 1:
            self.unidades_c -= 1
            self.saldo = self.saldo + self.vGlobales.costo_bala_c

        if bala.tipo == self.vGlobales.bala_mediana and self.unidades_m >= 1:
            self.unidades_m -= 1
            self.saldo = self.saldo + self.vGlobales.costo_bala_m

        if bala.tipo == self.vGlobales.bala_grande and self.unidades_g >= 1:
            self.unidades_g -= 1
            self.saldo = self.saldo + self.vGlobales.costo_bala_g

#Correcion de gravedad, Arreglo de bug de daño y proceso de Ia
