import pygame, sys, globales
import math

class Balas (pygame.sprite.Sprite):
        #constructor
    def __init__(self):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.altaura_max = 720  
        self.ancho = 5
        self.alto = 5
        self.i = 1
        #porte de la bala
        self.image = pygame.Surface ((self.ancho,self.alto))

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,50)
        self.image.fill(self.vGlobales.celeste)

        self.gravedad= 9.8

        
        self.caida = False

    def update(self, tanque, tanque_enemigo):
        #solo empezara el disparo si se ejecuto la funcion disparo
        if (self.caida == True):
            self.caida_Bala(tanque, tanque_enemigo)
            #moviemiento de la bala
            self.image.fill (self.vGlobales.NEGRO)
            self.rect.x = self.Xi + (self.velx * self.timepo)*0.5
            self.rect.y = self.Yi + (self.vely * self.timepo + 0.5 * self.gravedad * self.timepo**2)*0.5
            self.timepo += 0.12
            self.i+=1
        else:
            self.retorno_bala()


    def disparar (self,_angulo_grados, _angulo, _velocidad, tanque):
        self.velx = math.sin(_angulo) * _velocidad
        self.vely = math.cos(_angulo) * _velocidad
        self.rect.x= tanque.rect.x 
        self.rect.y = tanque.rect.y - tanque.alto
        self.Xi = self.rect.centerx
        self.Yi = self.rect.centery
        self.angulo = _angulo_grados
        self.timepo=0
        self.caida = True
        

    def caida_Bala(self, tanque, tanque_enmigo):
        color = self.vGlobales.celeste
        if (self.rect.y > 0 and self.rect.x < 1280):
            color = self.vGlobales.PANTALLA.get_at((self.rect.x,self.rect.y))
            color = (color[0], color[1], color[2])

        if (color == self.vGlobales.verde or color == self.vGlobales.grisclaro):
            self.caida = False
            print(self.distancia(self.rect.x,tanque.rect.x,self.rect.y,tanque.rect.y))
            
        if (self.rect.x >= self.vGlobales.WIDTH):
            self.caida = False
            print(self.distancia(self.rect.x,tanque.rect.x,self.rect.y,tanque.rect.y))
        
        if tanque_enmigo.rect.x + tanque_enmigo.largo > self.rect.x and \
        tanque_enmigo.rect.x < self.rect.x + self.ancho and \
        tanque_enmigo.rect.y + tanque.alto > self.rect.y and \
        tanque_enmigo.rect.y < self.rect.y + self.alto:
            print("tanke propio")
            self.caida = False
        
        if tanque.rect.x + tanque.largo > self.rect.x and \
        tanque.rect.x < self.rect.x + self.ancho and \
        tanque.rect.y + tanque.alto > self.rect.y and \
        tanque.rect.y < self.rect.y + self.alto:
            print("tanke enemigo")
            self.caida = False

        if self.altaura_max >= self.rect.y:
            self.altaura_max = self.rect.y
        
        if (int(self.rect.right) > self.vGlobales.WIDTH or int(self.rect.bottom) > self.vGlobales.HEIGHT): #cambia numeros
            self.rect.centerx = self.Xi-2
            self.rect.centery = self.Yi-2 

            

    def distancia (self,x1,x2,y1,y2):
        valor = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        return int(valor)
    
    def retorno_bala (self):
        self.rect.center = (500,-100)