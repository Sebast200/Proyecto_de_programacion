import pygame, sys, globales
import math

class Balas (pygame.sprite.Sprite):
        #constructor
    def __init__(self):
        super().__init__()
        self.vGlobales = globales.Globaless()
        
        
        #porte de la bala
        self.image = pygame.Surface ((5,5))
        

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,50)
        self.image.fill(self.vGlobales.celeste)
        self.timepo=0
        self.gravedad= 9.8

        
        self.caida = False

    def update(self):
        #solo empezara el disparo si se ejecuto la funcion disparo

        if (self.caida == True):
            self.caida_Bala()
            #moviemiento de la bala
            self.image.fill (self.vGlobales.NEGRO)
            self.rect.x = self.Xi + (self.velx * self.timepo)*0.5
            self.rect.y = self.Yi + (self.vely * self.timepo + 0.5 * self.gravedad * self.timepo**2)*0.5

            #se detiene el movimiento al tocar con algun borde
            if (int(self.rect.right) > 1020 or int(self.rect.bottom) > 720): #cambia numeros
                self.rect.centerx = self.Xi-2
                self.rect.centery = self.Yi-2
            self.timepo += 0.12
    
    def disparar (self, _angulo, _velocidad, _posicion):
        self.velx = math.sin(_angulo) * _velocidad
        self.vely = math.cos(_angulo) * _velocidad
        self.rect.x= _posicion[0]
        self.rect.y = _posicion[1]
        self.Xi = self.rect.centerx
        self.Yi = self.rect.centery
        self.caida = True

    def caida_Bala(self):
        i = 1
        posicion = 0
        #busca el que rango de puntos se encuentra el centro del tanque con respecto a la matriz del terreno
        while (i<len(self.vGlobales.puntos_terreno)-2):
            if (self.rect.x >= self.vGlobales.puntos_terreno[i][0]) and (self.rect.x <= self.vGlobales.puntos_terreno[i+1][0]):
                posicion = i
                i=len(self.vGlobales.puntos_terreno)+1 #salir del bucle
            else:
                i=i+1
        i = posicion
        print(self.distancia(self.rect.x, self.vGlobales.puntos_terreno[i][0], self.vGlobales.puntos_terreno[i][1], self.rect.y) + (self.distancia(self.vGlobales.puntos_terreno[i+1][0], self.rect.x, self.rect.y, self.vGlobales.puntos_terreno[i+1][1])), " ", self.distancia(self.vGlobales.puntos_terreno[i][0], self.vGlobales.puntos_terreno[i+1][0], self.vGlobales.puntos_terreno[i+1][1], self.vGlobales.puntos_terreno[i][1]))

        #Colision con el suelo
        if (self.distancia(self.rect.x, self.vGlobales.puntos_terreno[i][0], self.vGlobales.puntos_terreno[i][1], self.rect.y) + (self.distancia(self.vGlobales.puntos_terreno[i+1][0], self.rect.x, self.rect.y, self.vGlobales.puntos_terreno[i+1][1])) <= self.distancia(self.vGlobales.puntos_terreno[i][0], self.vGlobales.puntos_terreno[i+1][0], self.vGlobales.puntos_terreno[i+1][1], self.vGlobales.puntos_terreno[i][1])):
            self.caida = False
            print("toco terreno")

        if (self.rect.x >= 1020):
            self.caida = False

    def distancia (self,x1,x2,y1,y2):
        valor = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        return int(valor)
    
    def colision_Tanke (self, listaTanke):
        i=0
        print("a")

        while i < len(listaTanke):
            print("b")

            if (self.distancia(self.rect.centerx, listaTanke[i].rect.centerx, self.rect.centery, listaTanke[i].rect.centery) <= listaTanke[i].radio):
                print("c")

                self.caida = False
                print("Toco tanque")
                i = len(listaTanke)
