import pygame, sys, globales
import math

class Balas (pygame.sprite.Sprite):
        #constructor
    def __init__(self, _x, _y):
        super().__init__()
        self.vGlobales = globales.Globaless()
        
        
        #porte de la bala
        self.image = pygame.Surface ((10,10))
        

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,50)
        self.image.fill(self.vGlobales.BLANCO)
        self.timepo=0
        self.gravedad= 9.8

        #movemos la bala al centro          UTIL
        #self.rect.center = (_x, _y)
        
        self.disparo = False

    def update(self):
        print("a")
        #solo empezara el disparo si se ejecuto la funcion disparo
        if (self.disparo == True):
            #moviemiento de la bala
            print("entro")
            self.image.fill (self.vGlobales.NEGRO)
            self.rect.x = self.Xi + (self.velx * self.timepo)*0.5
            self.rect.y = self.Yi + (self.vely * self.timepo + 0.5 * self.gravedad * self.timepo**2)*0.5
            #se detiene el movimiento al tocar con algun borde
            if (int(self.rect.right) > 1280 or int(self.rect.bottom) > 720):
                self.disparo = False
            self.timepo += 0.1
    
    def disparar (self, _angulo, _velocidad, _posicion):
        self.velx = math.sin(_angulo) * _velocidad
        self.vely = math.cos(_angulo) * _velocidad
        self.rect.x= _posicion[0]
        self.rect.y = _posicion[1]
        self.Xi = self.rect.x
        self.Yi = self.rect.y
        self.disparo = True