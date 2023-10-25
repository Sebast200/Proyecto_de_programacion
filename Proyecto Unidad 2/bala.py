import pygame, sys, globales, math
from pygame import mixer
from math import sqrt
class Balas (pygame.sprite.Sprite):
    #Constructor
    def __init__(self, tipo, daño, unidades):
        super().__init__()
        self.vGlobales = globales.Globaless()
        self.altaura_max = 0  
        self.distancia_max = 0
        self.ancho = 5
        self.alto = 5
        self.tipo = tipo          #Id de bala/Diametro de la bala
        self.daño = daño
        self.unidades_tanque1 = unidades
        self.unidades_tanque2 = unidades
        self.contador_recorrido = 1
        self.coordenadas_altura_max = (0,-100)
        self.coordenadas_distancia = (0,-100)
        #Tamano de la bala
        self.image = pygame.Surface ((self.ancho,self.alto))
        #Obtiene el rectangulo (Sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (500,-100)
        self.image.fill(self.vGlobales.celeste)
        self.explosion = 0
        self.gravedad = 9.8
        self.shoot_impact = mixer.Sound("Proyecto Unidad 2/sonidos_musica/explosion.mp3")
        self.caida = False
        self.timepo=0

    def update(self, tanque, tanque_enemigo, superficie, pixel_array, lista_tanques, num_jugadores):
        #Solo empezara el disparo si se ejecuto la funcion disparo
        if (self.caida == True):
            self.caida_Bala(tanque, tanque_enemigo, lista_tanques, num_jugadores)
            #Moviemiento de la bala
            self.image.fill (self.vGlobales.NEGRO)
            self.rect.x = self.Xi + (self.velx * self.timepo)*0.5
            self.rect.y = self.Yi + (self.vely * self.timepo + 0.5 * self.gravedad * self.timepo**2)*0.8
            self.timepo += 0.12
            self.contador_recorrido+=1
            return superficie
            
        else:
            if(self.explosion == 1):
                superficie = self.destruccion_terreno(pixel_array, superficie) 
            self.retorno_bala()
            return superficie

    #Modifica el terreno despues de ubna explosion
    def destruccion_terreno(self, pixel_array, nueva_superficie):
        pixel_array = self.rompe_terreno(pixel_array,self.tipo/2,self.rect.center)
        nueva_superficie = pixel_array.make_surface()
        self.explosion=0
        return nueva_superficie

    #Ejecuta el disparo de bala
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

    def caida_Bala(self, tanque, tanque_enemigo, lista_tanques, num_jugadores):
        #Toma el color para la colision de la bala 
        color = self.vGlobales.celeste
        if (self.rect.y > 0 and self.rect.x < 1280 ):
            color = self.vGlobales.PANTALLA.get_at((self.rect.x,self.rect.y))
            color = (color[0], color[1], color[2])

        #Verifica la colision con terreno o panel
        if (color == self.vGlobales.verde or color == self.vGlobales.grisclaro):
            self.shoot_impact.play()
            self.caida = False
            self.explosion = 1
            self.colision_explosion_tanque(tanque, tanque_enemigo, lista_tanques, num_jugadores)
        
        #Verifica los rangos de la pantalla
        if (self.rect.x >= self.vGlobales.WIDTH or self.rect.x <= self.vGlobales.ancho_gris ):
            self.shoot_impact.play()
            self.caida = False
        
        #Verifica suelo
        if (self.rect.x < 0 and self.rect.y > 720):
            self.shoot_impact.play()
            self.caida = False
        
        #Colision con el tanque enemigo
        if tanque_enemigo.rect.x + tanque_enemigo.largo > self.rect.x and \
            tanque_enemigo.rect.x < self.rect.x + self.ancho and \
            tanque_enemigo.rect.y + tanque.alto > self.rect.y and \
            tanque_enemigo.rect.y < self.rect.y + self.alto:
            self.shoot_impact.play()
            self.caida = False
            self.explosion = 1
            if self.tipo == self.vGlobales.bala_chica:
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_c
            if self.tipo == self.vGlobales.bala_mediana:
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_m
            if self.tipo == self.vGlobales.bala_grande:
                tanque_enemigo.vida = tanque_enemigo.vida - self.vGlobales.daño_bala_g
        
        #saño a lista
        for i in range (num_jugadores):
            if lista_tanques[i].rect.x + lista_tanques[i].largo > self.rect.x and \
            lista_tanques[i].rect.x < self.rect.x + self.ancho and \
            lista_tanques[i].rect.y + tanque.alto > self.rect.y and \
            lista_tanques[i].rect.y < self.rect.y + self.alto:
                self.shoot_impact.play()
                self.caida = False
                self.explosion = 1
                if self.tipo == self.vGlobales.bala_chica:
                    lista_tanques[i].vida = lista_tanques[i].vida - self.vGlobales.daño_bala_c
                if self.tipo == self.vGlobales.bala_mediana:
                    lista_tanques[i].vida = lista_tanques[i].vida - self.vGlobales.daño_bala_m
                if self.tipo == self.vGlobales.bala_grande:
                    lista_tanques[i].vida = lista_tanques[i].vida - self.vGlobales.daño_bala_g

        #Colision con el tanque propio
        if tanque.rect.x + tanque.largo > self.rect.x and \
        tanque.rect.x < self.rect.x + self.ancho and \
        tanque.rect.y + tanque.alto > self.rect.y and \
        tanque.rect.y < self.rect.y + self.alto:
            self.shoot_impact.play()
            self.caida = False
            self.explosion = 1
            if self.tipo == self.vGlobales.bala_chica:
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_c
            if self.tipo == self.vGlobales.bala_mediana:
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_m
            if self.tipo == self.vGlobales.bala_grande:
                tanque.vida = tanque.vida - self.vGlobales.daño_bala_g
        
        #Altura maxima
        if self.altaura_max < tanque.rect.y - self.rect.y:
            self.altaura_max = tanque.rect.y - self.rect.y
            #Restriccion para que la bala no se salga del rango Y
            if self.rect.y <= 10:
                self.coordenadas_altura_max = (self.rect.x, 20)
            else:
                self.coordenadas_altura_max = (self.rect.x, self.rect.y - 10)
        
        #Distancia Maxima
        if self.caida == True:
            self.coordenadas_distancia = (self.rect.x,self.rect.y+20)
            self.distancia_max = self.distancia(self.rect.x,tanque.rect.x,self.rect.y,tanque.rect.y)
        if (int(self.rect.right) > self.vGlobales.WIDTH or int(self.rect.bottom) > self.vGlobales.HEIGHT): #cambia numeros
            self.rect.centerx = self.Xi-2
            self.rect.centery = self.Yi-2  
            
    def retorno_bala (self):
        self.rect.center = (500,-100)
    
    #Distancia entre dos puntos
    def distancia (self,x1,x2,y1,y2):
        valor = sqrt(((x2-x1)**2) + ((y2-y1)**2))
        return int(valor)
    
    #Destruccion del terreno
    def rompe_terreno(self,terreno,radio,posicion_explosion):
        i = 0
        while (i < self.vGlobales.WIDTH-self.vGlobales.ancho_gris):
            j = 0
            while (j < self.vGlobales.HEIGHT):
                if (int(self.distancia(posicion_explosion[0]-self.vGlobales.ancho_gris,i,posicion_explosion[1],j) <= radio)):
                    terreno[i][j] = (0,0,0,0)
                j+=1
            i+=1
        return terreno
    
    #Daño producido por la explosion de bala
    def colision_explosion_tanque (self, tanque1, tanque2, lista_tanques, num_jugadores):
        Distancia1 = self.distancia(tanque1.rect.x, self.rect.x, tanque1.rect.y, self.rect.y)
        Distancia2 = self.distancia(tanque2.rect.x, self.rect.x, tanque2.rect.y, self.rect.y)
        Distancias  = []
        for i in range (num_jugadores):
            Distancias.append(self.distancia(lista_tanques[i].rect.x, self.rect.x, lista_tanques[i].rect.y, self.rect.y))
        
        if (Distancia1 <= self.tipo/2):
            tanque1.vida = int(tanque1.vida - self.daño * math.cos(Distancia1 / (22* math.acos(0))))
        if (Distancia2 <= self.tipo/2):
            tanque2.vida = int(tanque2.vida - self.daño * math.cos(Distancia2 / (22* math.acos(0))))
        
        for i in range (num_jugadores):
            if (Distancias[i] <= self.tipo/2):
                lista_tanques[i].vida = int(lista_tanques[i].vida - self.daño * math.cos(Distancias[i] / (22* math.acos(0))))