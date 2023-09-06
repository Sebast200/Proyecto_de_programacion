import pygame, sys
import math

class Balala (pygame.sprite.Sprite):
        #constructor
    def __init__(self,_velocidad, _angulo):
        super().__init__()
        
        #porte de la bala
        self.image = pygame.Surface ((10,10))
        self.image.fill((255,0,0))

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.timepo=0
        self.gravedad= 9.8

        #movemos la bala al centro          UTIL
        self.velx = math.sin(_angulo) * _velocidad
        self.vely = math.cos(_angulo) * _velocidad
        self.rect.center = (1280// 2, 720 // 2)
        self.Xi = self.rect.x
        self.Yi = self.rect.y

    def update(self):
        #moviemiento de la bala
        self.rect.x = self.Xi + (self.velx * self.timepo)*0.5
        self.rect.y = self.Yi + (self.vely * self.timepo + 0.5 * self.gravedad * self.timepo**2)*0.5
        if (int(self.rect.right) > 1280 or int(self.rect.bottom) > 720):
            self.rect.center=(200,200)
        self.timepo += 0.3


