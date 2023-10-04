import pygame, sys, globales, math

class Balas (pygame.sprite.Sprite):
    #Constructor
    def __init__(self, tipo, daño, unidades):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.altaura_max = 0  
        self.ancho = 5
        self.alto = 5
        self.tipo = tipo
        self.daño = daño
        self.unidades = unidades
        self.contador_recorrido = 1
        self.coordenadas_altura_max = (0,-100)
        #Tamano de la bala
        self.image = pygame.Surface ((self.ancho,self.alto))

        #obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,-100)
        self.image.fill(self.vGlobales.celeste)
        self.coord = ()
        self.i =0
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
            if (self.i==1):
                contador_circ= 0
                while (contador_circ <= 2000):
                    pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.coord),(self.vGlobales.bala_chica/2),0)
                    contador_circ +=1
                if contador_circ == 2000:
                    self.i = 0
            
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
        
        

    def caida_Bala(self, tanque, tanque_enemigo):
        #Toma el color para la colision de la bala 
        color = self.vGlobales.celeste
        if (self.rect.y > 0 and self.rect.x < 1280 ):
            color = self.vGlobales.PANTALLA.get_at((self.rect.x,self.rect.y))
            color = (color[0], color[1], color[2])

        #Verifica la colision con terreno o panel
        if (color == self.vGlobales.verde or color == self.vGlobales.grisclaro):
            if self.tipo == self.vGlobales.bala_chica:
                self.i=1
                self.coord = (self.rect.x,self.rect.y)
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_chica/2),0)
            self.caida = False
        
        #Verifica los rangos de la pantalla
        if (self.rect.x >= self.vGlobales.WIDTH or self.rect.x <= 0):
            self.caida = False
        
        #Verifica suelo
        if (self.rect.x < 0 and self.rect.y > 720):
            self.caida = False
        
        #Colision con el tanque propio
        if tanque_enemigo.rect.x + tanque_enemigo.largo > self.rect.x and \
        tanque_enemigo.rect.x < self.rect.x + self.ancho and \
        tanque_enemigo.rect.y + tanque.alto > self.rect.y and \
        tanque_enemigo.rect.y < self.rect.y + self.alto:
            self.caida = False
            if self.tipo == self.vGlobales.bala_chica:
                self.i=1
                self.coord = (self.rect.x,self.rect.y)
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_chica/2),0)
            if self.tipo == self.vGlobales.bala_chica:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_chica/2),0)
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_c
            if self.tipo == self.vGlobales.bala_mediana:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_mediana/2),0)
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_m
            if self.tipo == self.vGlobales.bala_grande:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_grande/2),0)
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_g
            print("vida enemigo: ", tanque_enemigo.vida)

        #Colision con el tanque enemigo
        if tanque.rect.x + tanque.largo > self.rect.x and \
        tanque.rect.x < self.rect.x + self.ancho and \
        tanque.rect.y + tanque.alto > self.rect.y and \
        tanque.rect.y < self.rect.y + self.alto:
            self.caida = False
            if self.tipo == self.vGlobales.bala_chica:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_chica/2),0)
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_c
            if self.tipo == self.vGlobales.bala_mediana:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_mediana/2),0)
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_m
            if self.tipo == self.vGlobales.bala_grande:
                pygame.draw.circle(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.rect.x, self.rect.y),(self.vGlobales.bala_grande/2),0)
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_g
            print("vida: ", tanque.vida)

        #Altura maxima
        if self.altaura_max < tanque.rect.y - self.rect.y:
            self.altaura_max = tanque.rect.y - self.rect.y
            #Restriccion para que la bala no se salga del rango y
            if self.rect.y <= 10:
                self.coordenadas_altura_max = (self.rect.x, 20)

            else:
                self.coordenadas_altura_max = (self.rect.x, self.rect.y - 10)
            

        if (int(self.rect.right) > self.vGlobales.WIDTH or int(self.rect.bottom) > self.vGlobales.HEIGHT): #cambia numeros
            self.rect.centerx = self.Xi-2
            self.rect.centery = self.Yi-2  
            
    def retorno_bala (self):
        self.rect.center = (500,-100)
