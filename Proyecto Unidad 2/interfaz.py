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
        self.box_armas = pygame.Rect(15,470,225,80)
        #Creacion de tres rectangulos que mostraran tres tipos de bala
        self.minibox_bala1 = pygame.Rect(15,470,75,80)
        self.minibox_bala2 = pygame.Rect(90,470,75,80)
        self.minibox_bala3 = pygame.Rect(165,470,75,80)
        #Creacion de verificadores que se les haya hecho click a uno de los tres botones del inventario
        self.minibox_bala1_active = True
        self.minibox_bala2_active = False
        self.minibox_bala3_active = False
        #Tambien se van a crear variables para que cambien de color a la hora de que se les haga click
        self.minibox_bala1_color = self.vGlobales.ROJO
        self.minibox_bala2_color = self.vGlobales.NEGRO
        self.minibox_bala3_color = self.vGlobales.NEGRO
        #Creacion de pequeñas cajas de texto que se van a encargar de mostrar la municion de cada bala
        self.text_municion_bala1 = ""
        self.text_surface_municion_bala1 = self.vGlobales.font4.render(self.text_municion_bala1, True,self.vGlobales.NEGRO)
        self.text_surface_municion_bala1_rect = pygame.Rect(15,560,75,40)
        self.text_municion_bala2 = ""
        self.text_surface_municion_bala2 = self.vGlobales.font4.render(self.text_municion_bala2, True,self.vGlobales.NEGRO)
        self.text_surface_municion_bala2_rect = pygame.Rect(90,560,75,40)
        self.text_municion_bala3 = ""
        self.text_surface_municion_bala3 = self.vGlobales.font4.render(self.text_municion_bala3, True,self.vGlobales.NEGRO)
        self.text_surface_municion_bala3_rect = pygame.Rect(165,560,75,40)
        #Creacion de las balas del inventario
        self.bala_g_img = pygame.image.load("Proyecto Unidad 2/imagenes/bala_g_img.png")
        self.bala_m_img = pygame.image.load("Proyecto Unidad 2/imagenes/bala_m_img.png")
        self.bala_c_img = pygame.image.load("Proyecto Unidad 2/imagenes/bala_c_img.png")
        #Voy a usar minibox_bala como los rectangulos de estos textos, despues de todo esto es temporal
        #Creacion de pequeña caja para desplegar un mini menu
        self.boton_abrir_minimenu = "+"
        self.boton_surface_abrir_minimenu = self.vGlobales.font.render(self.boton_abrir_minimenu,True,self.vGlobales.NEGRO)
        self.boton_abrir_minimenu_rect = pygame.Rect(260,0,40,40)
        self.boton_abrir_minimenu_color = self.vGlobales.gris
        #Creacion de booleano que dependiendo de su valor, vera si se debera imprimir el boton para abrir el minimenu o no
        self.boton_abrir_minimenu_active = False
        #Creacion de variables de minimenu
        self.boton_nueva_partida = "Nueva partida"
        self.boton_surface_nueva_partida = self.vGlobales.font4.render(self.boton_nueva_partida,True,self.vGlobales.NEGRO)
        self.boton_nueva_partida_rect = pygame.Rect(270,10,150,30)
        self.boton_nueva_partida_color = self.vGlobales.verde
        self.boton_salir = "Salir"
        self.boton_surface_salir = self.vGlobales.font4.render(self.boton_salir,True,self.vGlobales.NEGRO)
        self.boton_salir_rect = pygame.Rect(430,10,60,30)
        self.boton_salir_color = self.vGlobales.ROJO
        self.boton_cerrar_minimenu = "x"
        self.boton_surface_cerrar_minimenu = self.vGlobales.font.render(self.boton_cerrar_minimenu,True,self.vGlobales.NEGRO)
        self.boton_cerrar_minimenu_rect = pygame.Rect(500,0,40,50)
        self.boton_cerrar_minimenu_color = self.vGlobales.grisclaro
        #Creacion de variables que mostraran la vida de los tanques
        self.text_vida_jugador1 = ""
        self.text_vida_jugador1_color = self.vGlobales.rojo_oscuro
        self.text_vida_jugador2 = ""
        self.text_vida_jugador2_color = self.vGlobales.rojo_oscuro

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

                #Aqui antes se cambiaba de valor text_jugador1, ahora lo borrare
                '''
                if turno_jugador == 1:
                    self.text_jugador1 = "Jugador 2"
                    self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.ROJO)
                    self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))
                elif turno_jugador == 2:
                    self.text_jugador1 = "Jugador 1"
                    self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.AZUL)
                    self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))
                '''

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
        #Condicion de click para el boton que desplegara el minimenu
        if self.boton_abrir_minimenu_rect.collidepoint(posicion_muose):
            self.boton_abrir_minimenu_active = True
        if self.boton_abrir_minimenu_active == True:
            if self.boton_cerrar_minimenu_rect.collidepoint(posicion_muose):
                self.boton_abrir_minimenu_active = False

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

    def print_interfaz (self, bala_c, bala_m, bala_g, tanque1, tanque2):
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

        #AQUI SE CONSEGUIRAN LOS DATOS PARA LA IMPRESION DE LA MUNICION DE LAS BALAS DEL TANQUE
        self.text_municion_bala1 = "x" + str(bala_c)
        self.text_surface_municion_bala1 = self.vGlobales.font4.render(self.text_municion_bala1,True,self.vGlobales.NEGRO)
        self.text_municion_bala2 = "x" + str(bala_m)
        self.text_surface_municion_bala2 = self.vGlobales.font4.render(self.text_municion_bala2,True,self.vGlobales.NEGRO)
        self.text_municion_bala3 = "x" + str(bala_g)
        self.text_surface_municion_bala3 = self.vGlobales.font4.render(self.text_municion_bala3,True,self.vGlobales.NEGRO)
        #IMPRESION DE MUNICION DE BALAS
        self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala1, (self.text_surface_municion_bala1_rect.x + 20, self.text_surface_municion_bala1_rect.y))
        self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala2, (self.text_surface_municion_bala2_rect.x + 20, self.text_surface_municion_bala2_rect.y))
        self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala3, (self.text_surface_municion_bala3_rect.x + 20, self.text_surface_municion_bala3_rect.y))
        #IMPRESION DE LAS BALAS A USAR
        self.vGlobales.PANTALLA.blit(self.bala_g_img,(self.minibox_bala3.x + 17, self.minibox_bala3.y + 17))
        self.vGlobales.PANTALLA.blit(self.bala_m_img,(self.minibox_bala2.x + 17, self.minibox_bala2.y + 17))
        self.vGlobales.PANTALLA.blit(self.bala_c_img,(self.minibox_bala1.x + 17, self.minibox_bala1.y + 17))
        #IMPRESION DE BOTON PARA ABRIR EL MINIMENU
        if self.boton_abrir_minimenu_active == False:
            pygame.draw.rect(self.vGlobales.PANTALLA, self.boton_abrir_minimenu_color, self.boton_abrir_minimenu_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_abrir_minimenu,(self.boton_abrir_minimenu_rect.x + 10, self.boton_abrir_minimenu_rect.y + 5))
        else:
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.gris,(260,0,280,50))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_nueva_partida_color,self.boton_nueva_partida_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_nueva_partida,(self.boton_nueva_partida_rect.x + 5, self.boton_nueva_partida_rect.y + 5))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_salir_color,self.boton_salir_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_salir,(self.boton_salir_rect.x + 5,self.boton_salir_rect.y + 5))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_cerrar_minimenu_color,self.boton_cerrar_minimenu_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_cerrar_minimenu,(self.boton_cerrar_minimenu_rect.x + 12, self.boton_cerrar_minimenu_rect.y + 10))
        #RECOLECCION DE DATOS E IMPRESION DE VIDA DEBAJO DE LOS TANQUES
        self.text_vida_jugador1 = str(tanque1.vida)
        self.text_surface_vida_jugador1 = self.vGlobales.font4.render(self.text_vida_jugador1,True,self.text_vida_jugador1_color)
        self.text_vida_jugador2 = str(tanque2.vida)
        self.text_surface_vida_jugador2 = self.vGlobales.font4.render(self.text_vida_jugador2,True,self.text_vida_jugador2_color)
        self.vGlobales.PANTALLA.blit(self.text_surface_vida_jugador1,(tanque1.rect.x - 10,tanque1.rect.y + 15))
        self.vGlobales.PANTALLA.blit(self.text_surface_vida_jugador2,(tanque2.rect.x - 5,tanque2.rect.y + 15))
        #CAMBIOS REALIZADOS
        #1.- EN INIT SE CREARON LAS VARIABLES PARA HACER LA CAJA DE INVENTARIO
        #2.- EN PRINT_INTERFAZ SE AGREGO LOS COMANDOS PARA DIBUJAR Y ACTUALIZAR EL INVENTARIO
        #3.- SE CREO EL METODO CLICK_MOUSE_INVENTARIO PARA HACER LAS CONDICIONALES DE LA CAJA DEL INVENTARIO DEL JUGADOR

        #NUEVOS CAMBIOS (FRANCO ARENAS) 11-10-2023
        #1.- Voy a intentar hacer que se puedan imprimir las cantidades de balas que quedan en el inventario de cada tanque, estaba pensando que tal vez podria usar print_interfaz para que se le pida como tributo un tanque para que se pueda imprimir desde ahi los datos
        #2.- Linea 59 se agregan variables para las cajas de texto que diran la municion de las armas
        #3.- Linea 232 aprox se empiezan a conseguir e imprimir la municion de las balas
        #4.- Linea 69 aprox, se van a crear ciertas cajas de textos que mas adelante se eliminaran para ser reemplazados por imagenes de balas
        #5.- Linea 243 aprox, se empieza a imprimir el texto temporal

        #NUEVOS CAMBIOS (FRANCO ARENAS) 12-10-2023
        #1.- Voy a intentar hacer que se pueda mostrar una caja con una flecha abajo o algo asi por el estilo para poder imprimir un mini menu en la partida para cuando se quiera reiniciar la partida o salir de esta
        #2.- Linea 77 Creacion de variables para el boton que desplegara el minimenu
        #3.- Linea 254 Impresion de boton para abrir el minimenu
        #4.- Linea 84 Creacion de variables para el boton de nueva partida
        #5.- Linea 174 Condicion para que se despliegue el minimenu
        #6.- Linea 264 Condicion para Impresion de minimenu

        #NUEVOS CAMBIOS (FRANCO ARENAS) 18-10-2023
        #1.- Voy a hacer que se vea la vida en los tanques
        #2.- Linea 235 hice que pida otras cosas adicionales el metodo de print_interfaz()
        #3.- Linea 97 creacion de variables que mostraran la vida de cada uno de los tanques (en este caso por ahora son solo 2)
        #4.- Linea 290 recoleccion e impresion de vida de los tanques
        #5.- Linea 145 se borro la seccion de codigo en la que se cambiaba el valor de text_jugador1 para que mostrara de quien era el turno
