import pygame, sys, globales, math

class Balas (pygame.sprite.Sprite):
    #Constructor
    def __init__(self):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.altaura_max = 0  
        self.ancho = 5
        self.alto = 5
        self.contador_recorrido = 1
        self.coordenadas_altura_max = (0,-100)
        #Tamano de la bala
        self.image = pygame.Surface ((self.ancho,self.alto))

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,-100)
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
            self.contador_recorrido+=1
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
        self.altaura_max = 0
        
        

    def caida_Bala(self, tanque, tanque_enmigo):
        #Toma el color para la colision de la bala 
        color = self.vGlobales.celeste
        if (self.rect.y > 0 and self.rect.x < 1280 ):
            color = self.vGlobales.PANTALLA.get_at((self.rect.x,self.rect.y))
            color = (color[0], color[1], color[2])
            print("x:", self.rect.x)
            print("y:",self.rect.y)

        #Verifica la colision con terreno o panel
        if (color == self.vGlobales.verde or color == self.vGlobales.grisclaro):
            self.caida = False
        
        #Verifica los rangos de la pantalla
        if (self.rect.x >= self.vGlobales.WIDTH or self.rect.x <= 0):
            self.caida = False
        
        #Verifica suelo
        if (self.rect.x < 0 and self.rect.y > 720):
            self.caida = False
        
        #Colision con el tanque enemigo
        if tanque_enmigo.rect.x + tanque_enmigo.largo > self.rect.x and \
        tanque_enmigo.rect.x < self.rect.x + self.ancho and \
        tanque_enmigo.rect.y + tanque.alto > self.rect.y and \
        tanque_enmigo.rect.y < self.rect.y + self.alto:
            self.caida = False
            tanque_enmigo.vida = False
        
        #Colision con el tanque propio
        if tanque.rect.x + tanque.largo > self.rect.x and \
        tanque.rect.x < self.rect.x + self.ancho and \
        tanque.rect.y + tanque.alto > self.rect.y and \
        tanque.rect.y < self.rect.y + self.alto:
            self.caida = False
            tanque.vida = False
        
        #Altura maxima
        if self.altaura_max < tanque.rect.y - self.rect.y:
            self.altaura_max = tanque.rect.y - self.rect.y
            self.coordenadas_altura_max = (self.rect.x, self.rect.y - 10)

        if (int(self.rect.right) > self.vGlobales.WIDTH or int(self.rect.bottom) > self.vGlobales.HEIGHT): #cambia numeros
            self.rect.centerx = self.Xi-2
            self.rect.centery = self.Yi-2  
            
    def retorno_bala (self):
        self.rect.center = (500,-100)