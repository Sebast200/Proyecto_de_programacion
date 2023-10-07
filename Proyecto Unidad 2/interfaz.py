import pygame, sys, globales, math
from pygame.locals import *
from pygame import mixer
class Interfazz():
    def __init__(self):
        self.vGlobales = globales.Globaless()
        #CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
        self.textbox_angulo = ""
        #Rectangulo de la caja de texto
        self.textbox_angulo_rect = pygame.Rect(150,180,80,40)
        #Esta variable cambiara de false a true una vez que el jugador le haga click al rectangulo para escribir
        self.textbox_angulo_active = False

        self.textbox_velocidad_inicial = ""
        #Rectangulo de la caja de texto
        self.textbox_velocidad_inicial_rect = pygame.Rect(150,355,80,40)
        #Esta variable cambiara de false a true una vez que el jugador le haga click al rectangulo para escribir
        self.textbox_velocidad_inicial_active = False

        #Creacion de boton para disparar
        self.text_boton_jugador = "Dispara"
        self.text_boton_jugador_rect = pygame.Rect(20,600,220,80)
        self.text_boton_jugador_color = self.vGlobales.verde
        
        #Creacion de texto que dira el turno del jugador
        self.text_jugador1 = "Jugador 1"
        self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.AZUL)
        self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))

        #Creacion de texto que dira altura maxima
        self.text_altura_maxima = ""
        self.text_surface_altura_maxima = self.vGlobales.font.render(self.text_altura_maxima, True, self.vGlobales.NEGRO)
        self.text_surface_altura_maxima_rect = self.text_surface_altura_maxima.get_rect(center = (120,700))

        #Creacion de texto que dira distancia maxima
        self.text_distancia_maxima = ""
        self.text_surface_distancia_maxima = self.vGlobales.font.render(self.text_distancia_maxima, True, self.vGlobales.NEGRO)
        self.text_surface_distancia_maxima_rect = self.text_surface_distancia_maxima.get_rect(center = (120,700))
        
        #Creacion de texto que dira game over cuando uno de los tanques muera
        self.text_game_over = ""
        self.text_surface_game_over = self.vGlobales.font.render(self.text_game_over, True, self.vGlobales.rojo_oscuro)
        self.text_surface_game_over_rect = self.text_surface_game_over.get_rect(center = ((self.vGlobales.WIDTH/2) + 140,(self.vGlobales.HEIGHT/2) - 30))

        #Creacion de Caja que va a mostrar tres rectangulos que mostraran las opciones de la bala
        self.box_armas = pygame.Rect(15,510,225,80)
        #Creacion de tres rectangulos que mostraran tres tipos de bala
        self.minibox_bala1 = pygame.Rect(15,510,75,80)
        self.minibox_bala2 = pygame.Rect(90,510,75,80)
        self.minibox_bala3 = pygame.Rect(165,510,75,80)
        #Creacion de verificadores que se les haya hecho click a uno de los tres botones del inventario
        self.minibox_bala1_active = True
        self.minibox_bala2_active = False
        self.minibox_bala3_active = False
        #Tambien se van a crear variables para que cambien de color a la hora de que se les haga click
        self.minibox_bala1_color = self.vGlobales.ROJO
        self.minibox_bala2_color = self.vGlobales.NEGRO
        self.minibox_bala3_color = self.vGlobales.NEGRO
    

    def interfaz(self):
        #Texto que dice Angulo...
        self.text_angulo_jugador1 = "Angulo:"
        self.text_surface_angulo_jugador1 = self.vGlobales.font.render(self.text_angulo_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_angulo_jugador1_rect = self.text_surface_angulo_jugador1.get_rect(center = (80,200))

        #Creacion de texto que dice velocidad
        self.text_velocidad_jugador1 = "Velocidad"
        self.text_surface_velocidad_jugador1 = self.vGlobales.font.render(self.text_velocidad_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_velocidad_jugador1_rect = self.text_surface_velocidad_jugador1.get_rect(center = (80,360))
        
        #Creacion de texto que dice inicial
        self.text_inicial_jugador1 = "inicial:"
        self.text_surface_inicial_jugador1 = self.vGlobales.font.render(self.text_inicial_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_inicial_jugador1_rect = self.text_surface_inicial_jugador1.get_rect(center = (80,390))

        #Proceso de impresion de textos de la interfaz a la pantalla
        self.vGlobales.PANTALLA.blit(self.text_surface_jugador1,self.text_surface_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_angulo_jugador1,self.text_surface_angulo_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_velocidad_jugador1,self.text_surface_velocidad_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_inicial_jugador1,self.text_surface_inicial_jugador1_rect)
   

    def boton_disparar_click (self, bala, tanque, turno_jugador):
        try:
            numero_angulo = int(self.textbox_angulo)
            numero_velocidad_inicial = int(self.textbox_velocidad_inicial)
            #Por ahora la unica condicion sera que el numero del angulo no supere los 360 grados
            if numero_angulo>360:
                self.textbox_angulo = ""
            else:
                bala.disparar(numero_angulo, math.pi/180 * (numero_angulo + 90), numero_velocidad_inicial,tanque)
                #Testeo de sound_effects al inicio del juego tiene que estar atento a cambios
                Tank_shoot = mixer.Sound("Proyecto Unidad 2/sonidos_musica/tank_shooting.mp3")
                Tank_shoot.play()
                text_boton_jugador = "Recarga"
                text_boton_jugador_color = self.vGlobales.ROJO
                pygame.draw.rect(self.vGlobales.PANTALLA,text_boton_jugador_color,self.text_boton_jugador_rect)
                self.text_boton_jugador_surface = self.vGlobales.font.render(text_boton_jugador,True,self.vGlobales.BLANCO)
                self.textbox_angulo = ""
                self.textbox_velocidad_inicial = ""

                if turno_jugador == 1:
                    self.text_jugador1 = "Jugador 2"
                    self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.ROJO)
                    self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))
                elif turno_jugador == 2:
                    self.text_jugador1 = "Jugador 1"
                    self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.AZUL)
                    self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))

        except ValueError:
            self.textbox_angulo = ""
            self.textbox_velocidad_inicial = ""

    def click_mouse(self, posicion_muose,bala,pos_tanque, turno_pasado, turno_jugador):
        #Condicion de click para el cuadro de angulo
        if self.textbox_angulo_rect.collidepoint( posicion_muose):
            self.textbox_angulo_active = True
        else:
            self.textbox_angulo_active = False
        #Condicion de click para el cuadro de velocidad inicial
        if self.textbox_velocidad_inicial_rect.collidepoint(posicion_muose):
            self.textbox_velocidad_inicial_active = True
        else:
            self.textbox_velocidad_inicial_active = False
        #Condicion de click para el boton de disparo
        if self.text_boton_jugador_rect.collidepoint(posicion_muose):
            #ENCONTRE UN ERROR, VOY A ARREGLARLO
            #El error consiste en que cuando una persona pone datos invalidos, el turno cambia de todos modos, voy a ver si ya se arreglo o non
            #Ya lo arregle xd
            try:
                numero_angulo = int(self.textbox_angulo)
                numero_velocidad_inicial = int(self.textbox_velocidad_inicial)
                #Por ahora la unica condicion sera que el numero del angulo no supere los 360 grados
                if numero_angulo>360:
                    self.textbox_angulo = ""
                else:
                    self.boton_disparar_click(bala, pos_tanque, turno_jugador)
                    turno_pasado = 0
                    return turno_pasado
            except ValueError:
                self.textbox_angulo = ""
                self.textbox_velocidad_inicial = ""

    def click_mouse_inventario(self, posicion_muose):
        #Condicion de click para la caja de inventario
        if self.box_armas.collidepoint(posicion_muose):
            #Condicion de click para el cuadro 1 del inventario
            if self.minibox_bala1.collidepoint(posicion_muose):
                self.minibox_bala1_active = True
                self.minibox_bala1_color = self.vGlobales.ROJO
                self.minibox_bala2_active = False
                self.minibox_bala2_color = self.vGlobales.NEGRO
                self.minibox_bala3_active = False
                self.minibox_bala3_color = self.vGlobales.NEGRO
            #Condicion de click para el cuadro 2 del inventario
            if self.minibox_bala2.collidepoint(posicion_muose):
                self.minibox_bala2_active = True
                self.minibox_bala2_color = self.vGlobales.ROJO
                self.minibox_bala1_active = False
                self.minibox_bala1_color = self.vGlobales.NEGRO
                self.minibox_bala3_active = False
                self.minibox_bala3_color = self.vGlobales.NEGRO
            #Condicion de click para el cuadro 3 del inventario
            if self.minibox_bala3.collidepoint(posicion_muose):
                self.minibox_bala3_active = True
                self.minibox_bala3_color = self.vGlobales.ROJO
                self.minibox_bala1_active = False
                self.minibox_bala1_color = self.vGlobales.NEGRO
                self.minibox_bala2_active = False
                self.minibox_bala2_color = self.vGlobales.NEGRO    
    
    def escribir (self, evento):
        #Seccion de codigo de caja de texto de angulo
            if self.textbox_angulo_active == True:
                if evento.key == pygame.K_BACKSPACE:
                    self.textbox_angulo = self.textbox_angulo[:-1]

                if evento.unicode.isnumeric():
                    #limitacion de tres cifras
                    if len(self.textbox_angulo)<3:
                        self.textbox_angulo += evento.unicode
            #Seccion de codigo de caja de texto de velocidad inicial
            if self.textbox_velocidad_inicial_active == True:
                if evento.key == pygame.K_BACKSPACE:
                    self.textbox_velocidad_inicial = self.textbox_velocidad_inicial[:-1]
                if evento.unicode.isnumeric():
                    if len(self.textbox_velocidad_inicial)<3:
                        self.textbox_velocidad_inicial += evento.unicode

    def print_interfaz (self):
        #AQUI SE DIBUJARA Y SE ACTUALIZARA LAS CAJAS DE TEXTO Y EL BOTON DE DISPARO
        pygame.draw.rect(self.vGlobales.PANTALLA ,self.vGlobales.gris, self.textbox_angulo_rect)
        self.textbox_angulo_surface = self.vGlobales.font.render(self.textbox_angulo, True, self.vGlobales.NEGRO)

        pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.gris, self.textbox_velocidad_inicial_rect)
        self.textbox_velocidad_inicial_surface = self.vGlobales.font.render(self.textbox_velocidad_inicial, True, self.vGlobales.NEGRO)

        pygame.draw.rect(self.vGlobales.PANTALLA, self.text_boton_jugador_color, self.text_boton_jugador_rect)
        self.text_boton_jugador_surface = self.vGlobales.font.render(self.text_boton_jugador, True, self.vGlobales.NEGRO)

        #AQUI SE DIBUJARA Y SE ACTUALIZARA EL INVENTARIO
        pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.gris, self.box_armas)
        pygame.draw.rect(self.vGlobales.PANTALLA, self.minibox_bala1_color, self.minibox_bala1, 3)
        pygame.draw.rect(self.vGlobales.PANTALLA, self.minibox_bala2_color, self.minibox_bala2, 3)
        pygame.draw.rect(self.vGlobales.PANTALLA, self.minibox_bala3_color, self.minibox_bala3, 3)        
        
        #NUMEROS MAGICOS
        self.vGlobales.PANTALLA.blit(self.textbox_angulo_surface, (self.textbox_angulo_rect.x + 15, self.textbox_angulo_rect.y + 10))
        self.vGlobales.PANTALLA.blit(self.textbox_velocidad_inicial_surface,(self.textbox_velocidad_inicial_rect.x + 15, self.textbox_velocidad_inicial_rect.y + 10))
        self.vGlobales.PANTALLA.blit(self.text_boton_jugador_surface, (self.text_boton_jugador_rect.x + 65, self.text_boton_jugador_rect.y + 25))
        self.vGlobales.PANTALLA.blit(self.text_surface_jugador1,self.text_surface_jugador1_rect)

        #CAMBIOS REALIZADOS
        #1.- EN INIT SE CREARON LAS VARIABLES PARA HACER LA CAJA DE INVENTARIO
        #2.- EN PRINT_INTERFAZ SE AGREGO LOS COMANDOS PARA DIBUJAR Y ACTUALIZAR EL INVENTARIO
        #3.- SE CREO EL METODO CLICK_MOUSE_INVENTARIO PARA HACER LAS CONDICIONALES DE LA CAJA DEL INVENTARIO DEL JUGADOR
