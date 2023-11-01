import pygame, sys, globales, math
from pygame.locals import *
from pygame import mixer
from boton import Button
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

        #Creacion de Caja que va a contener tres minirectangulos
        self.box_armas = pygame.Rect(15,470,225,80)
        #Creacion de tres minirectangulos que mostraran tres tipos de bala
        self.minibox_bala1 = pygame.Rect(15,470,75,80)
        self.minibox_bala2 = pygame.Rect(90,470,75,80)
        self.minibox_bala3 = pygame.Rect(165,470,75,80)
        #Creacion de verificadores que se les haya hecho click a uno de los tres botones del inventario
        self.minibox_bala1_active = True
        self.minibox_bala2_active = False
        self.minibox_bala3_active = False
        #Tambien se van a crear variables para que cambien de color a la hora de que se les haga click
        #La bala chica va a estar seleccionada desde el principio de la partida, por eso este tendra su booleano en True y el color de la caja sera rojo
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
        #Voy a usar minibox_bala1, minibox_bala2 y minibox_bala3 como los rectangulos de estas imagenes
        #Creacion de pequenio boton para desplegar un mini menu
        self.boton_abrir_minimenu = "+"
        self.boton_surface_abrir_minimenu = self.vGlobales.font.render(self.boton_abrir_minimenu,True,self.vGlobales.NEGRO)
        self.boton_abrir_minimenu_rect = pygame.Rect(260,0,40,40)
        self.boton_abrir_minimenu_color = self.vGlobales.gris
        #Creacion de booleano que dependiendo de su valor, vera si se debera imprimir el boton para abrir el minimenu o imprimir el minimenu
        self.boton_abrir_minimenu_active = False
        #Creacion de variables de minimenu
        #Boton que dira nueva partida
        self.boton_nueva_partida = "Nueva partida"
        self.boton_surface_nueva_partida = self.vGlobales.font4.render(self.boton_nueva_partida,True,self.vGlobales.NEGRO)
        self.boton_nueva_partida_rect = pygame.Rect(270,10,150,30)
        self.boton_nueva_partida_color = self.vGlobales.verde
        #Boton que dira salir
        self.boton_salir = "Salir"
        self.boton_surface_salir = self.vGlobales.font4.render(self.boton_salir,True,self.vGlobales.NEGRO)
        self.boton_salir_rect = pygame.Rect(430,10,60,30)
        self.boton_salir_color = self.vGlobales.ROJO
        #Boton que servira para cerrar el minimenu
        self.boton_cerrar_minimenu = "x"
        self.boton_surface_cerrar_minimenu = self.vGlobales.font.render(self.boton_cerrar_minimenu,True,self.vGlobales.NEGRO)
        self.boton_cerrar_minimenu_rect = pygame.Rect(500,0,40,50)
        self.boton_cerrar_minimenu_color = self.vGlobales.grisclaro
        #Creacion de variables que mostraran la vida de los tanques
        self.text_vida_jugador1 = ""
        self.text_vida_jugador1_color = self.vGlobales.BLANCO
        self.text_vida_jugador2 = ""
        self.text_vida_jugador2_color = self.vGlobales.BLANCO
        #Creacion de boton para abrir la tienda
        self.boton_abrir_tienda = Button(image=None, pos=(1260,20), text_input="$", font=self.vGlobales.font, base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        self.boton_abrir_tienda_active = False
        #Creacion de boton para volver(cerrar) de la tienda
        self.boton_volver_tienda = Button(image=None, pos=(760,570), text_input="Volver",font=self.vGlobales.font,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        #Creacion de vitrinas de balas 
        self.minibox_bala1_tienda = pygame.Rect(575,300,75,80)
        self.minibox_bala2_tienda = pygame.Rect(725,300,75,80)
        self.minibox_bala3_tienda = pygame.Rect(875,300,75,80)
        #Creacion de botones para comprar balas
        self.boton_comprar_bala_c = Button(image=None, pos=(612,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        self.boton_comprar_bala_m = Button(image=None, pos=(762,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        self.boton_comprar_bala_g = Button(image=None, pos=(912,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        #Creacion de Texto que mostrara el saldo del jugador
        self.text_saldo = "$"
        self.text_saldo_color = self.vGlobales.verde
        #Creacion de Texto que mostrara el titulo "Tienda"
        self.text_tienda = "Tienda de jugador"
        self.text_tienda_surface = self.vGlobales.font.render(self.text_tienda,True,self.vGlobales.BLANCO)
        self.text_tienda_surface_rect = self.text_tienda_surface.get_rect(center=(760,125))
        #Creacion de Texto que mostrara el precio de las balas
        self.text_costo_bala_c = "$1000"
        self.text_costo_bala_m = "$2500"
        self.text_costo_bala_g = "$4000"
        self.text_costo_bala_c_surface = self.vGlobales.font4.render(self.text_costo_bala_c,True,self.vGlobales.BLANCO)
        self.text_costo_bala_m_surface = self.vGlobales.font4.render(self.text_costo_bala_m,True,self.vGlobales.BLANCO)
        self.text_costo_bala_g_surface = self.vGlobales.font4.render(self.text_costo_bala_g,True,self.vGlobales.BLANCO)
        self.text_costo_bala_c_surface_rect = self.text_costo_bala_c_surface.get_rect(center=(610,280))
        self.text_costo_bala_m_surface_rect = self.text_costo_bala_m_surface.get_rect(center=(760,280))
        self.text_costo_bala_g_surface_rect = self.text_costo_bala_g_surface.get_rect(center=(910,280))
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
        #IMPRESION DE RECTANGULO PEQUEÑO QUE ESTARA DEBAJO DEL TEXTO DEL JUGADOR
        #pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.gris,(50,20,140,35))
        self.vGlobales.PANTALLA.blit(self.text_surface_jugador1,self.text_surface_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_angulo_jugador1,self.text_surface_angulo_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_velocidad_jugador1,self.text_surface_velocidad_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_inicial_jugador1,self.text_surface_inicial_jugador1_rect)
   
    def boton_disparar_click (self, bala, tanque, numero_angulo, numero_velocidad_inicial, viento):
        bala.disparar(numero_angulo, math.pi/180 * (numero_angulo + 90), numero_velocidad_inicial,tanque, viento)
        #Se reproduce el sonido de disparo
        Tank_shoot = mixer.Sound("Proyecto Unidad 2/sonidos_musica/tank_shooting.mp3")
        Tank_shoot.play()
        self.textbox_angulo = ""
        self.textbox_velocidad_inicial = ""

    def click_mouse(self, posicion_muose,bala,pos_tanque, turno_pasado, viento):
        #Condicion de click para el cuadro de angulo
        if self.textbox_angulo_rect.collidepoint(posicion_muose):
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
            try:
                numero_angulo = int(self.textbox_angulo)
                numero_velocidad_inicial = int(self.textbox_velocidad_inicial)
                #Por ahora la unica condicion sera que el numero del angulo no supere los 360 grados
                if numero_angulo>360:
                    self.textbox_angulo = ""
                else:
                    self.boton_disparar_click(bala, pos_tanque, numero_angulo, numero_velocidad_inicial, viento)
                    turno_pasado = 0
                    return turno_pasado
            except ValueError:
                self.textbox_angulo = ""
                self.textbox_velocidad_inicial = ""
        #Condicion de click para el boton que desplegara el minimenu
        if self.boton_abrir_minimenu_rect.collidepoint(posicion_muose):
            self.boton_abrir_minimenu_active = True
        #Conidicion de que si se le hizo click al boton para cerrar el minimenu (primero se verifica si el minimenu esta abierto o no)
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
    
    def health_bars(self, tanque):
        ratio = tanque.vida/100 #100 es la vida maxima de los tanques
        #Proceso de impresion de barra de vida
        pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, (tanque.rect.x - 20,tanque.rect.y+12,56,21))
        pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.ROJO, (tanque.rect.x - 17,tanque.rect.y+15,50,15))
        pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.verde_oscuro, (tanque.rect.x - 17,tanque.rect.y+15,50 * ratio,15))
        
    def print_interfaz (self, bala_c, bala_m, bala_g, lista_tanques_test, num_jugadores):
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
        self.vGlobales.PANTALLA.blit(self.text_boton_jugador_surface, (self.text_boton_jugador_rect.x + 55, self.text_boton_jugador_rect.y + 25))
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
        #IMPRESION DE LAS IMAGENES DE LAS BALAS
        self.vGlobales.PANTALLA.blit(self.bala_g_img,(self.minibox_bala3.x + 17, self.minibox_bala3.y + 17))
        self.vGlobales.PANTALLA.blit(self.bala_m_img,(self.minibox_bala2.x + 17, self.minibox_bala2.y + 17))
        self.vGlobales.PANTALLA.blit(self.bala_c_img,(self.minibox_bala1.x + 17, self.minibox_bala1.y + 17))
        #IMPRESION DE BOTON PARA ABRIR EL MINIMENU
        if self.boton_abrir_minimenu_active == False:
            pygame.draw.rect(self.vGlobales.PANTALLA, self.boton_abrir_minimenu_color, self.boton_abrir_minimenu_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_abrir_minimenu,(self.boton_abrir_minimenu_rect.x + 10, self.boton_abrir_minimenu_rect.y + 5))
        else:
            #Se entra a este else cuando el booleano es True (osea, cuando se le haya dado click al boton para abrir el minimenu)
            #IMPRESION DE MINIMENU
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.gris,(260,0,280,50))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_nueva_partida_color,self.boton_nueva_partida_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_nueva_partida,(self.boton_nueva_partida_rect.x + 12, self.boton_nueva_partida_rect.y + 7))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_salir_color,self.boton_salir_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_salir,(self.boton_salir_rect.x + 10,self.boton_salir_rect.y + 7))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_cerrar_minimenu_color,self.boton_cerrar_minimenu_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_cerrar_minimenu,(self.boton_cerrar_minimenu_rect.x + 12, self.boton_cerrar_minimenu_rect.y + 10))
        #RECOLECCION DE DATOS E IMPRESION DE VIDA DEBAJO DE LOS TANQUES
        for i in range (num_jugadores):
            self.health_bars(lista_tanques_test[i])
        for i in range (num_jugadores):
            self.text_vida_jugador1 = str(lista_tanques_test[i].vida)
            if lista_tanques_test[i].vida < 0: self.text_vida_jugador1 = str(0)
            self.text_surface_vida_jugador1 = self.vGlobales.font4.render(self.text_vida_jugador1,True,self.text_vida_jugador1_color)
            self.vGlobales.PANTALLA.blit(self.text_surface_vida_jugador1,(lista_tanques_test[i].rect.x - 10,lista_tanques_test[i].rect.y + 15))
    def print_tienda(self, tanque,event):
        self.contador1 = 0
        while self.contador1<1:
            #RECOLECCION DE DATOS
            self.text_tienda = "Tienda de jugador" + str(self.contador1 + 1)
            self.text_tienda_surface = self.vGlobales.font.render(self.text_tienda,True,self.vGlobales.BLANCO)
            self.text_tienda_surface_rect = self.text_tienda_surface.get_rect(center=(760,125))
            if event == pygame.MOUSEBUTTONDOWN:
                self.contador1 += 1              
            #PROCESO DE IMPRESION
            #IMPRESION DE TIENDA
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.gris_oscuro,(self.vGlobales.ancho_gris + 200,100,600,500))
            #Dibujo de rectangulos verdes que van estar debajo del boton para comprar
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(565,395,100,30))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(715,395,100,30))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(865,395,100,30))
            #Dibujo de rectangulo rojo para el boton Volver
            pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.rojo_oscuro,(700,550,120,40))
            for boton in [self.boton_volver_tienda, self.boton_comprar_bala_c, self.boton_comprar_bala_m, self.boton_comprar_bala_g]:
                boton.update(self.vGlobales.PANTALLA)
            pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala1_tienda, 3)
            pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala2_tienda, 3)
            pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala3_tienda, 3)
            self.vGlobales.PANTALLA.blit(self.bala_g_img,(self.minibox_bala3_tienda.x + 17, self.minibox_bala3_tienda.y + 17))
            self.vGlobales.PANTALLA.blit(self.bala_m_img,(self.minibox_bala2_tienda.x + 17, self.minibox_bala2_tienda.y + 17))
            self.vGlobales.PANTALLA.blit(self.bala_c_img,(self.minibox_bala1_tienda.x + 17, self.minibox_bala1_tienda.y + 17))
            #IMPRESION DE SALDO DE JUGADOR
            self.text_saldo = "$"+str(tanque.saldo)
            self.text_saldo_surface = self.vGlobales.font.render(self.text_saldo,True,self.text_saldo_color)
            self.text_saldo_surface_rect = self.text_saldo_surface.get_rect(center=(1000,125))
            self.vGlobales.PANTALLA.blit(self.text_saldo_surface,self.text_saldo_surface_rect)   
            #IMPRESION DE TEXTO QUE DICE TIENDA EN TIENDA
            self.vGlobales.PANTALLA.blit(self.text_tienda_surface,self.text_tienda_surface_rect)  
            #IMPRESION DE TEXTO QUE MUESTRA LOS COSTOS DE LAS BALAS
            self.vGlobales.PANTALLA.blit(self.text_costo_bala_c_surface,self.text_costo_bala_c_surface_rect)
            self.vGlobales.PANTALLA.blit(self.text_costo_bala_m_surface,self.text_costo_bala_m_surface_rect)
            self.vGlobales.PANTALLA.blit(self.text_costo_bala_g_surface,self.text_costo_bala_g_surface_rect)
#NUEVOS CAMBIOS
#1.- QUIERO AGREGAR UN CUADRO NEGRO EN LA PARTE EN LA QUE SE IMPRIME EL TURNO DEL JUGADOR
#2.- Linea 122 se agrego un rectangulo gris para que se vean algunos textos del jugador
