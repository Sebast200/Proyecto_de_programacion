import pygame, sys, globales, math, random
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
        self.bala_g_img = pygame.image.load("imagenes/bala_g_img.png")
        self.bala_m_img = pygame.image.load("imagenes/bala_m_img.png")
        self.bala_c_img = pygame.image.load("imagenes/bala_c_img.png")
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
        self.boton_pasar_turno = "Pasar Turno"
        self.boton_surface_pasar_turno = self.vGlobales.font4.render(self.boton_pasar_turno,True,self.vGlobales.NEGRO)
        self.boton_pasar_turno_rect = pygame.Rect(270,10,150,30)
        self.boton_pasar_turno_color = self.vGlobales.verde
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
        self.boton_finalizar_tienda = Button(image=None, pos=(760,570), text_input="Finalizar",font=self.vGlobales.font,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        #Creacion de vitrinas de balas 
        self.minibox_bala1_tienda = pygame.Rect(575,280,75,80)
        self.minibox_bala2_tienda = pygame.Rect(725,280,75,80)
        self.minibox_bala3_tienda = pygame.Rect(875,280,75,80)
        #Creacion de botones para comprar balas
        self.boton_comprar_bala_c = Button(image=None, pos=(612,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        self.boton_comprar_bala_m = Button(image=None, pos=(762,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        self.boton_comprar_bala_g = Button(image=None, pos=(912,410), text_input="Comprar",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO, hovering_color=self.vGlobales.BLANCO)
        #Creacion de botones para vender balas
        self.boton_vender_bala_c = Button(image=None, pos=(612,450), text_input="Vender",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO,hovering_color=self.vGlobales.BLANCO)
        self.boton_vender_bala_m = Button(image=None, pos=(762,450), text_input="Vender",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO,hovering_color=self.vGlobales.BLANCO)
        self.boton_vender_bala_g = Button(image=None, pos=(912,450), text_input="Vender",font=self.vGlobales.font4,base_color=self.vGlobales.NEGRO,hovering_color=self.vGlobales.BLANCO)

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
        Tank_shoot = mixer.Sound("sonidos_musica/tank_shooting.mp3")
        Tank_shoot.play()
        self.textbox_angulo = ""
        self.textbox_velocidad_inicial = ""

    def click_mouse(self, posicion_muose, bala, pos_tanque, turno_pasado, viento):
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
                    #if interfaz.minibox_bala1_active == True and lista_tanques_OG[turno_jugador-1].unidades_c > 0 and lista_tanques_OG[turno_jugador-1].vida > 0
                    if self.minibox_bala1_active == True and pos_tanque.unidades_c>0:
                        self.boton_disparar_click(bala, pos_tanque, numero_angulo, numero_velocidad_inicial, viento)
                        turno_pasado = 0
                        return turno_pasado
                    if self.minibox_bala2_active == True and pos_tanque.unidades_m>0:
                        self.boton_disparar_click(bala, pos_tanque, numero_angulo, numero_velocidad_inicial, viento)
                        turno_pasado = 0
                        return turno_pasado
                    if self.minibox_bala3_active == True and pos_tanque.unidades_g>0:
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
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_pasar_turno_color,self.boton_pasar_turno_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_pasar_turno,(self.boton_pasar_turno_rect.x + 22, self.boton_pasar_turno_rect.y + 7))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_salir_color,self.boton_salir_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_salir,(self.boton_salir_rect.x + 10,self.boton_salir_rect.y + 7))
            pygame.draw.rect(self.vGlobales.PANTALLA,self.boton_cerrar_minimenu_color,self.boton_cerrar_minimenu_rect)
            self.vGlobales.PANTALLA.blit(self.boton_surface_cerrar_minimenu,(self.boton_cerrar_minimenu_rect.x + 12, self.boton_cerrar_minimenu_rect.y + 10))
        #RECOLECCION DE DATOS E IMPRESION DE VIDA DEBAJO DE LOS TANQUES
        for i in range (num_jugadores):
            self.health_bars(lista_tanques_test[i])
        for i in range (num_jugadores):
            self.text_vida_jugador1 = str(int(lista_tanques_test[i].vida))
            if lista_tanques_test[i].vida < 0: self.text_vida_jugador1 = str(0)
            self.text_surface_vida_jugador1 = self.vGlobales.font4.render(self.text_vida_jugador1,True,self.text_vida_jugador1_color)
            self.vGlobales.PANTALLA.blit(self.text_surface_vida_jugador1,(lista_tanques_test[i].rect.x - 10,lista_tanques_test[i].rect.y + 15))

    def print_tienda(self,lista_tanques_OG,compraron_todos,num_jugadores,bala_c,bala_m,bala_g):
        #Proceso de impresion de tienda
        self.contadortienda = 0
        blur_image = pygame.image.load("imagenes/Blur.png")
        self.vGlobales.PANTALLA.blit(blur_image, (0,0))
        while compraron_todos == False:
            if self.contadortienda<num_jugadores:
                if lista_tanques_OG[self.contadortienda].bot == False:
                    #RECOLECCION DE DATOS
                    self.text_tienda = "Tienda de jugador " + str(self.contadortienda + 1)
                    self.text_tienda_surface = self.vGlobales.font.render(self.text_tienda,True,self.vGlobales.BLANCO)
                    self.text_tienda_surface_rect = self.text_tienda_surface.get_rect(center=(760,125))
                    #Creacion de Texto que mostrara el precio de las balas
                    self.text_costo_bala_c = "$1000"
                    self.text_costo_bala_m = "$2500"
                    self.text_costo_bala_g = "$4000"
                    self.text_costo_bala_c_surface = self.vGlobales.font4.render(self.text_costo_bala_c,True,self.vGlobales.BLANCO)
                    self.text_costo_bala_m_surface = self.vGlobales.font4.render(self.text_costo_bala_m,True,self.vGlobales.BLANCO)
                    self.text_costo_bala_g_surface = self.vGlobales.font4.render(self.text_costo_bala_g,True,self.vGlobales.BLANCO)
                    self.text_costo_bala_c_surface_rect = self.text_costo_bala_c_surface.get_rect(center=(610,260))
                    self.text_costo_bala_m_surface_rect = self.text_costo_bala_m_surface.get_rect(center=(760,260))
                    self.text_costo_bala_g_surface_rect = self.text_costo_bala_g_surface.get_rect(center=(910,260))
                    #PROCESO DE IMPRESION
                    #IMPRESION DE TIENDA
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.gris_oscuro,(self.vGlobales.ancho_gris + 200,100,600,500))
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.negro_azulado,(self.vGlobales.ancho_gris + 200,100,600,500),5)
                    #Dibujo de rectangulos verdes que van estar debajo del boton para comprar
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(565,395,100,30))
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(715,395,100,30))
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.verde,(865,395,100,30))
                    #Dibujo de rectangulos amarillos que van a estar debajo de los botones para vender
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.amarillo,(565,435,100,30))
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.amarillo,(715,435,100,30))
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.amarillo,(865,435,100,30))
                    #Dibujo de rectangulo rojo para el boton Volver
                    pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.rojo_oscuro,(690,550,140,40))
                    for boton in [self.boton_finalizar_tienda, self.boton_comprar_bala_c, self.boton_comprar_bala_m, self.boton_comprar_bala_g, self.boton_vender_bala_c, self.boton_vender_bala_m, self.boton_vender_bala_g]:
                        boton.update(self.vGlobales.PANTALLA)
                    pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala1_tienda, 3)
                    pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala2_tienda, 3)
                    pygame.draw.rect(self.vGlobales.PANTALLA, self.vGlobales.NEGRO, self.minibox_bala3_tienda, 3)
                    
                    self.vGlobales.PANTALLA.blit(self.bala_g_img,(self.minibox_bala3_tienda.x + 17, self.minibox_bala3_tienda.y + 17))
                    self.vGlobales.PANTALLA.blit(self.bala_m_img,(self.minibox_bala2_tienda.x + 17, self.minibox_bala2_tienda.y + 17))
                    self.vGlobales.PANTALLA.blit(self.bala_c_img,(self.minibox_bala1_tienda.x + 17, self.minibox_bala1_tienda.y + 17))
                    #IMPRESION DE SALDO DE JUGADOR
                    self.text_saldo = "Saldo: $"+str(lista_tanques_OG[self.contadortienda].saldo)
                    self.text_saldo_color = self.vGlobales.verde
                    self.text_saldo_surface = self.vGlobales.font.render(self.text_saldo,True,self.text_saldo_color)
                    self.text_saldo_surface_rect = self.text_saldo_surface.get_rect(center=(760,165))
                    self.vGlobales.PANTALLA.blit(self.text_saldo_surface,self.text_saldo_surface_rect)   
                    #IMPRESION DE TEXTO QUE DICE TIENDA EN TIENDA
                    self.vGlobales.PANTALLA.blit(self.text_tienda_surface,self.text_tienda_surface_rect)  
                    #IMPRESION DE TEXTO QUE MUESTRA LOS COSTOS DE LAS BALAS
                    self.vGlobales.PANTALLA.blit(self.text_costo_bala_c_surface,self.text_costo_bala_c_surface_rect)
                    self.vGlobales.PANTALLA.blit(self.text_costo_bala_m_surface,self.text_costo_bala_m_surface_rect)
                    self.vGlobales.PANTALLA.blit(self.text_costo_bala_g_surface,self.text_costo_bala_g_surface_rect)
                    #creacion e impresion de pequeñas cajas de texto que se van a encargar de mostrar la municion de cada bala
                    self.text_municion_bala1_tienda = "x" + str(lista_tanques_OG[self.contadortienda].unidades_c)
                    self.text_surface_municion_bala1_tienda = self.vGlobales.font4.render(self.text_municion_bala1_tienda, True,self.vGlobales.BLANCO)
                    self.text_surface_municion_bala1_tienda_rect = pygame.Rect(605,365,75,40)
                    self.text_municion_bala2_tienda = "x" + str(lista_tanques_OG[self.contadortienda].unidades_m)
                    self.text_surface_municion_bala2_tienda = self.vGlobales.font4.render(self.text_municion_bala2_tienda, True,self.vGlobales.BLANCO)
                    self.text_surface_municion_bala2_tienda_rect = pygame.Rect(745,365,75,40)
                    self.text_municion_bala3_tienda = "x" + str(lista_tanques_OG[self.contadortienda].unidades_g)
                    self.text_surface_municion_bala3_tienda = self.vGlobales.font4.render(self.text_municion_bala3_tienda, True,self.vGlobales.BLANCO)
                    self.text_surface_municion_bala3_tienda_rect = pygame.Rect(905,365,75,40)
                    self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala1_tienda,self.text_surface_municion_bala1_tienda_rect)
                    self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala2_tienda,self.text_surface_municion_bala2_tienda_rect)
                    self.vGlobales.PANTALLA.blit(self.text_surface_municion_bala3_tienda,self.text_surface_municion_bala3_tienda_rect)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            #Condicionales de botones
                            if self.boton_finalizar_tienda.checkForInput(event.pos):
                                self.contadortienda += 1
                            if self.boton_comprar_bala_c.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].comprar_bala(bala_c)
                            if self.boton_comprar_bala_m.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].comprar_bala(bala_m)
                            if self.boton_comprar_bala_g.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].comprar_bala(bala_g)
                            if self.boton_vender_bala_c.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].vender_bala(bala_c)
                            if self.boton_vender_bala_m.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].vender_bala(bala_m)
                            if self.boton_vender_bala_g.checkForInput(event.pos):
                                lista_tanques_OG[self.contadortienda].vender_bala(bala_g)
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    pygame.display.flip()
                else:
                    #Compra automatica del bot
                    contador_compra = 0
                    while contador_compra < 10:
                        item_comprar = random.randint(1, 3)
                        if item_comprar == 1 and lista_tanques_OG[self.contadortienda].saldo > self.vGlobales.costo_bala_c:
                            lista_tanques_OG[self.contadortienda].unidades_c += 1
                            lista_tanques_OG[self.contadortienda].saldo -= self.vGlobales.costo_bala_c
                            contador_compra += 1
                        if item_comprar == 2 and lista_tanques_OG[self.contadortienda].saldo > self.vGlobales.costo_bala_m:
                            lista_tanques_OG[self.contadortienda].unidades_m += 1
                            lista_tanques_OG[self.contadortienda].saldo -= self.vGlobales.costo_bala_m
                            contador_compra += 1
                        if item_comprar == 3 and lista_tanques_OG[self.contadortienda].saldo > self.vGlobales.costo_bala_g:
                            lista_tanques_OG[self.contadortienda].unidades_g += 1
                            lista_tanques_OG[self.contadortienda].saldo -= self.vGlobales.costo_bala_g
                            contador_compra += 1
                        else:
                            contador_compra += 1
                    self.contadortienda += 1
            else:                
                return True       

    def print_resultados(self,lista_tanques_OG,i,num_jugadores):
        self.interfaz()
        self.print_interfaz(lista_tanques_OG[i].unidades_c,lista_tanques_OG[i].unidades_m,lista_tanques_OG[i].unidades_g,lista_tanques_OG,num_jugadores)
        #Dibujo de rectangulo negro
        pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.negro_azulado,(self.vGlobales.ancho_gris + 70,60,900,600))
        pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.vGlobales.ancho_gris + 70,60,900,600),10)
        #Recoleccion de datos e impresion de texto
        #Texto que dira "Fin de la ronda"
        self.text_fin_ronda = "Fin de la Ronda"
        self.text_fin_ronda_surface = self.vGlobales.font2.render(self.text_fin_ronda,True,self.vGlobales.BLANCO)
        self.text_fin_ronda_rect = self.text_fin_ronda_surface.get_rect(center=(800,120))
        #Texto que dira quien es el ganador
        #Aqui se buscara quien es el jugador vivo, si hay mas de uno vivo significa que es empate
        contador = 0
        lista_tanques_vivos = []
        while contador<len(lista_tanques_OG):
            if lista_tanques_OG[contador].vida>0:
                lista_tanques_vivos.append(contador + 1)
            contador += 1
        if len(lista_tanques_vivos) == 1:
            self.text_ganador_ronda = "Ganador de esta ronda: Jugador " + str(lista_tanques_vivos[0])
        else:
            self.text_ganador_ronda = "Ganador de esta ronda: Empate"
        self.text_ganador_ronda_surface = self.vGlobales.font4.render(self.text_ganador_ronda,True,self.vGlobales.BLANCO)
        self.text_ganador_ronda_rect = self.text_ganador_ronda_surface.get_rect(center=(800,170))
        #Texto que dira "Bajas"
        self.text_bajas = "Bajas"
        self.text_bajas_surface = self.vGlobales.font4.render(self.text_bajas,True,self.vGlobales.BLANCO)
        self.text_bajas_rect = self.text_bajas_surface.get_rect(center=(800,240))
        #Texto que dira "Suicidios"
        self.text_suicidios = "Suicidios"
        self.text_suicidios_surface = self.vGlobales.font4.render(self.text_suicidios,True,self.vGlobales.BLANCO)
        self.text_suicidios_rect = self.text_suicidios_surface.get_rect(center=(970,240))
        #Texto que dira "Saldo"
        self.text_saldo_resultado = "Saldo"
        self.text_saldo_resultado_surface = self.vGlobales.font4.render(self.text_saldo_resultado,True,self.vGlobales.BLANCO)
        self.text_saldo_resultado_rect = self.text_saldo_resultado_surface.get_rect(center=(1140,240))
        #Texto que dira "Jugador 1"
        self.text_jugador1_resultado = "Jugador 1"
        self.text_jugador1_resultado_surface = self.vGlobales.font4.render(self.text_jugador1_resultado,True,self.vGlobales.AZUL)
        self.text_jugador1_resultado_rect = self.text_jugador1_resultado_surface.get_rect(center=(420,300))
        #Texto que mostrara las kills del jugador 1
        self.text_kills_jugador1 = str(lista_tanques_OG[0].total_kills)
        self.text_kills_jugador1_surface = self.vGlobales.font4.render(self.text_kills_jugador1,True,self.vGlobales.BLANCO)
        self.text_kills_jugador1_rect = self.text_kills_jugador1_surface.get_rect(center=(800,300))
        #Texto que mostrara las veces que se mato el jugador 1
        self.text_suicidios_jugador1 = str(lista_tanques_OG[0].cantidad_suicidios)
        self.text_suicidios_jugador1_surface = self.vGlobales.font4.render(self.text_suicidios_jugador1,True,self.vGlobales.BLANCO)
        self.text_suicidios_jugador1_rect = self.text_suicidios_jugador1_surface.get_rect(center=(970,300))
        #Texto que mostrara el saldo del jugador 1
        self.text_saldo_jugador1 = "$" + str(lista_tanques_OG[0].saldo)
        self.text_saldo_jugador1_surface = self.vGlobales.font4.render(self.text_saldo_jugador1,True,self.vGlobales.BLANCO)
        self.text_saldo_jugador1_rect = self.text_saldo_jugador1_surface.get_rect(center=(1140,300))
        #Texto que dira "Jugador 2"
        self.text_jugador2_resultado = "Jugador 2"
        self.text_jugador2_resultado_surface = self.vGlobales.font4.render(self.text_jugador2_resultado,True,self.vGlobales.ROJO)
        self.text_jugador2_resultado_rect = self.text_jugador2_resultado_surface.get_rect(center=(420,350))
        #Texto que mostrara las kills del jugador 2
        self.text_kills_jugador2 = str(lista_tanques_OG[1].total_kills)
        self.text_kills_jugador2_surface = self.vGlobales.font4.render(self.text_kills_jugador2,True,self.vGlobales.BLANCO)
        self.text_kills_jugador2_rect = self.text_kills_jugador2_surface.get_rect(center=(800,350))
        #Texto que mostrara las veces que se mato el jugador 2
        self.text_suicidios_jugador2 = str(lista_tanques_OG[1].cantidad_suicidios)
        self.text_suicidios_jugador2_surface = self.vGlobales.font4.render(self.text_suicidios_jugador2,True,self.vGlobales.BLANCO)
        self.text_suicidios_jugador2_rect = self.text_suicidios_jugador2_surface.get_rect(center=(970,350))
        #Texto que mostrara el saldo del jugador 2
        self.text_saldo_jugador2 = "$" + str(lista_tanques_OG[1].saldo)
        self.text_saldo_jugador2_surface = self.vGlobales.font4.render(self.text_saldo_jugador2,True,self.vGlobales.BLANCO)
        self.text_saldo_jugador2_rect = self.text_saldo_jugador2_surface.get_rect(center=(1140,350))
        #Proceso de verificacion de impresion de jugadores (para que no se impriman los 6 jugadores en caso de que estan jugando solo 4 o 3, etc)
        #A pesar de que tengo una ZONA DE IMPRESION, me temo que tendre que imprimir los nombres de los jugadores dentro de estas condicionales, de otro modo, esto no funcionara 
        if num_jugadores>=3:
            #Texto que dira "Jugador 3"
            self.text_jugador3_resultado = "Jugador 3"
            self.text_jugador3_resultado_surface = self.vGlobales.font4.render(self.text_jugador3_resultado,True,self.vGlobales.amarillo)
            self.text_jugador3_resultado_rect = self.text_jugador3_resultado_surface.get_rect(center=(420,400))
            self.vGlobales.PANTALLA.blit(self.text_jugador3_resultado_surface,self.text_jugador3_resultado_rect)
            #Texto que mostrara las kills del jugador 3
            self.text_kills_jugador3 = str(lista_tanques_OG[2].total_kills)
            self.text_kills_jugador3_surface = self.vGlobales.font4.render(self.text_kills_jugador3,True,self.vGlobales.BLANCO)
            self.text_kills_jugador3_rect = self.text_kills_jugador3_surface.get_rect(center=(800,400))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador3_surface,self.text_kills_jugador3_rect)
            #Texto que mostrara las veces que se mato el jugador 3
            self.text_suicidios_jugador3 = str(lista_tanques_OG[2].cantidad_suicidios)
            self.text_suicidios_jugador3_surface = self.vGlobales.font4.render(self.text_suicidios_jugador3,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador3_rect = self.text_suicidios_jugador3_surface.get_rect(center=(970,400))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador3_surface,self.text_suicidios_jugador3_rect)
            #Texto que mostrara el saldo del jugador 3
            self.text_saldo_jugador3 = "$" + str(lista_tanques_OG[2].saldo)
            self.text_saldo_jugador3_surface = self.vGlobales.font4.render(self.text_saldo_jugador3,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador3_rect = self.text_saldo_jugador3_surface.get_rect(center=(1140,400))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador3_surface,self.text_saldo_jugador3_rect)
        if num_jugadores>=4:
            #Texto que dira "Jugador 4"
            self.text_jugador4_resultado = "Jugador 4"
            self.text_jugador4_resultado_surface = self.vGlobales.font4.render(self.text_jugador4_resultado,True,self.vGlobales.celeste)
            self.text_jugador4_resultado_rect = self.text_jugador4_resultado_surface.get_rect(center=(420,450))                            
            self.vGlobales.PANTALLA.blit(self.text_jugador4_resultado_surface,self.text_jugador4_resultado_rect)
            #Texto que mostrara las kills del jugador 4
            self.text_kills_jugador4 = str(lista_tanques_OG[3].total_kills)
            self.text_kills_jugador4_surface = self.vGlobales.font4.render(self.text_kills_jugador4,True,self.vGlobales.BLANCO)
            self.text_kills_jugador4_rect = self.text_kills_jugador4_surface.get_rect(center=(800,450))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador4_surface,self.text_kills_jugador4_rect)
            #Texto que mostrara las veces que se mato el jugador 4
            self.text_suicidios_jugador4 = str(lista_tanques_OG[3].cantidad_suicidios)
            self.text_suicidios_jugador4_surface = self.vGlobales.font4.render(self.text_suicidios_jugador4,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador4_rect = self.text_suicidios_jugador4_surface.get_rect(center=(970,450))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador4_surface,self.text_suicidios_jugador4_rect)
            #Texto que mostrara el saldo del jugador 4
            self.text_saldo_jugador4 = "$" + str(lista_tanques_OG[3].saldo)
            self.text_saldo_jugador4_surface = self.vGlobales.font4.render(self.text_saldo_jugador4,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador4_rect = self.text_saldo_jugador4_surface.get_rect(center=(1140,450))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador4_surface,self.text_saldo_jugador4_rect)
        if num_jugadores>=5:
            #Texto que dira "Jugador 5"
            self.text_jugador5_resultado = "Jugador 5"
            self.text_jugador5_resultado_surface = self.vGlobales.font4.render(self.text_jugador5_resultado,True,self.vGlobales.morado)
            self.text_jugador5_resultado_rect = self.text_jugador5_resultado_surface.get_rect(center=(420,500))            
            self.vGlobales.PANTALLA.blit(self.text_jugador5_resultado_surface,self.text_jugador5_resultado_rect)
            #Texto que mostrara las kills del jugador 5
            self.text_kills_jugador5 = str(lista_tanques_OG[4].total_kills)
            self.text_kills_jugador5_surface = self.vGlobales.font4.render(self.text_kills_jugador5,True,self.vGlobales.BLANCO)
            self.text_kills_jugador5_rect = self.text_kills_jugador5_surface.get_rect(center=(800,500))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador5_surface,self.text_kills_jugador5_rect)
            #Texto que mostrara las veces que se mato el jugador 5
            self.text_suicidios_jugador5 = str(lista_tanques_OG[4].cantidad_suicidios)
            self.text_suicidios_jugador5_surface = self.vGlobales.font4.render(self.text_suicidios_jugador5,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador5_rect = self.text_suicidios_jugador5_surface.get_rect(center=(970,500))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador5_surface,self.text_suicidios_jugador5_rect)
            #Texto que mostrara el saldo del jugador 5
            self.text_saldo_jugador5 = "$" + str(lista_tanques_OG[4].saldo)
            self.text_saldo_jugador5_surface = self.vGlobales.font4.render(self.text_saldo_jugador5,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador5_rect = self.text_saldo_jugador5_surface.get_rect(center=(1140,500))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador5_surface,self.text_saldo_jugador5_rect)
        if num_jugadores>=6:
            #Texto que dira "Jugador 6"
            self.text_jugador6_resultado = "Jugador 6"
            self.text_jugador6_resultado_surface = self.vGlobales.font4.render(self.text_jugador6_resultado,True,self.vGlobales.naranjo)
            self.text_jugador6_resultado_rect = self.text_jugador6_resultado_surface.get_rect(center=(420,550))            
            self.vGlobales.PANTALLA.blit(self.text_jugador6_resultado_surface,self.text_jugador6_resultado_rect)
            #Texto que mostrara las kills del jugador 6
            self.text_kills_jugador6 = str(lista_tanques_OG[5].total_kills)
            self.text_kills_jugador6_surface = self.vGlobales.font4.render(self.text_kills_jugador6,True,self.vGlobales.BLANCO)
            self.text_kills_jugador6_rect = self.text_kills_jugador6_surface.get_rect(center=(800,550))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador6_surface,self.text_kills_jugador6_rect)
            #Texto que mostrara las veces que se mato el jugador 6
            self.text_suicidios_jugador6 = str(lista_tanques_OG[5].cantidad_suicidios)
            self.text_suicidios_jugador6_surface = self.vGlobales.font4.render(self.text_suicidios_jugador6,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador6_rect = self.text_suicidios_jugador6_surface.get_rect(center=(970,550))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador6_surface,self.text_suicidios_jugador6_rect)
            #Texto que mostrara el saldo del jugador 6
            self.text_saldo_jugador6 = "$" + str(lista_tanques_OG[5].saldo)
            self.text_saldo_jugador6_surface = self.vGlobales.font4.render(self.text_saldo_jugador6,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador6_rect = self.text_saldo_jugador6_surface.get_rect(center=(1140,550))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador6_surface,self.text_saldo_jugador6_rect)
        #Texto que dira "Haga Click para Continuar"
        self.text_click = "Haga Click para Continuar"
        self.text_click_surface = self.vGlobales.font2.render(self.text_click,True,self.vGlobales.BLANCO)
        self.text_click_rect = self.text_click_surface.get_rect(center=(800,620))        
        #ZONA DE IMPRESION
        self.vGlobales.PANTALLA.blit(self.text_fin_ronda_surface,self.text_fin_ronda_rect)
        self.vGlobales.PANTALLA.blit(self.text_ganador_ronda_surface,self.text_ganador_ronda_rect)
        self.vGlobales.PANTALLA.blit(self.text_bajas_surface,self.text_bajas_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_surface,self.text_suicidios_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_resultado_surface,self.text_saldo_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_jugador1_resultado_surface,self.text_jugador1_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_kills_jugador1_surface,self.text_kills_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador1_surface,self.text_suicidios_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_jugador1_surface,self.text_saldo_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_jugador2_resultado_surface,self.text_jugador2_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_kills_jugador2_surface,self.text_kills_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador2_surface,self.text_suicidios_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_jugador2_surface,self.text_saldo_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_click_surface,self.text_click_rect)

    #ESTE METODO ES LITERALMENTE print_resultados, aunque tiene algunas diferencias, entre estas son que ya no imprime la interfaz de la partida, no imprime ciertos textos y tiene una posicion diferente
    def print_resultados_finales(self,lista_tanques_OG,num_jugadores):
        #Dibujo de rectangulo negro transparente
        pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.negro_azulado,(self.vGlobales.ancho_gris + 90,90,900,600))
        pygame.draw.rect(self.vGlobales.PANTALLA,self.vGlobales.NEGRO,(self.vGlobales.ancho_gris + 90,90,900,600),10)
        #Recoleccion de datos e impresion de texto
        #Texto que dira "Resultados Finales"
        self.text_resultados_finales = self.vGlobales.font2.render("Resultados Finales",True,self.vGlobales.BLANCO)
        self.text_resultados_finales_rect = self.text_resultados_finales.get_rect(center=(820,150))
        #Texto que dira "Bajas"
        self.text_bajas = "Bajas"
        self.text_bajas_surface = self.vGlobales.font4.render(self.text_bajas,True,self.vGlobales.BLANCO)
        self.text_bajas_rect = self.text_bajas_surface.get_rect(center=(820,270))
        #Texto que dira "Suicidios"
        self.text_suicidios = "Suicidios"
        self.text_suicidios_surface = self.vGlobales.font4.render(self.text_suicidios,True,self.vGlobales.BLANCO)
        self.text_suicidios_rect = self.text_suicidios_surface.get_rect(center=(990,270))
        #Texto que dira "Saldo"
        self.text_saldo_resultado = "Saldo"
        self.text_saldo_resultado_surface = self.vGlobales.font4.render(self.text_saldo_resultado,True,self.vGlobales.BLANCO)
        self.text_saldo_resultado_rect = self.text_saldo_resultado_surface.get_rect(center=(1160,270))
        #Texto que dira "Jugador 1"
        self.text_jugador1_resultado = "Jugador 1"
        self.text_jugador1_resultado_surface = self.vGlobales.font4.render(self.text_jugador1_resultado,True,self.vGlobales.AZUL)
        self.text_jugador1_resultado_rect = self.text_jugador1_resultado_surface.get_rect(center=(440,330))
        #Texto que mostrara las kills del jugador 1
        self.text_kills_jugador1 = str(lista_tanques_OG[0].total_kills)
        self.text_kills_jugador1_surface = self.vGlobales.font4.render(self.text_kills_jugador1,True,self.vGlobales.BLANCO)
        self.text_kills_jugador1_rect = self.text_kills_jugador1_surface.get_rect(center=(820,330))
        #Texto que mostrara las veces que se mato el jugador 1
        self.text_suicidios_jugador1 = str(lista_tanques_OG[0].cantidad_suicidios)
        self.text_suicidios_jugador1_surface = self.vGlobales.font4.render(self.text_suicidios_jugador1,True,self.vGlobales.BLANCO)
        self.text_suicidios_jugador1_rect = self.text_suicidios_jugador1_surface.get_rect(center=(990,330))
        #Texto que mostrara el saldo del jugador 1
        self.text_saldo_jugador1 = "$" + str(lista_tanques_OG[0].saldo)
        self.text_saldo_jugador1_surface = self.vGlobales.font4.render(self.text_saldo_jugador1,True,self.vGlobales.BLANCO)
        self.text_saldo_jugador1_rect = self.text_saldo_jugador1_surface.get_rect(center=(1160,330))
        #Texto que dira "Jugador 2"
        self.text_jugador2_resultado = "Jugador 2"
        self.text_jugador2_resultado_surface = self.vGlobales.font4.render(self.text_jugador2_resultado,True,self.vGlobales.ROJO)
        self.text_jugador2_resultado_rect = self.text_jugador2_resultado_surface.get_rect(center=(440,380))
        #Texto que mostrara las kills del jugador 2
        self.text_kills_jugador2 = str(lista_tanques_OG[1].total_kills)
        self.text_kills_jugador2_surface = self.vGlobales.font4.render(self.text_kills_jugador2,True,self.vGlobales.BLANCO)
        self.text_kills_jugador2_rect = self.text_kills_jugador2_surface.get_rect(center=(820,380))
        #Texto que mostrara las veces que se mato el jugador 2
        self.text_suicidios_jugador2 = str(lista_tanques_OG[1].cantidad_suicidios)
        self.text_suicidios_jugador2_surface = self.vGlobales.font4.render(self.text_suicidios_jugador2,True,self.vGlobales.BLANCO)
        self.text_suicidios_jugador2_rect = self.text_suicidios_jugador2_surface.get_rect(center=(990,380))
        #Texto que mostrara el saldo del jugador 2
        self.text_saldo_jugador2 = "$" + str(lista_tanques_OG[1].saldo)
        self.text_saldo_jugador2_surface = self.vGlobales.font4.render(self.text_saldo_jugador2,True,self.vGlobales.BLANCO)
        self.text_saldo_jugador2_rect = self.text_saldo_jugador2_surface.get_rect(center=(1160,380))
        #Proceso de verificacion de impresion de jugadores (para que no se impriman los 6 jugadores en caso de que estan jugando solo 4 o 3, etc)
        #A pesar de que tengo una ZONA DE IMPRESION, me temo que tendre que imprimir los nombres de los jugadores dentro de estas condicionales, de otro modo, esto no funcionara 
        if num_jugadores>=3:
            #Texto que dira "Jugador 3"
            self.text_jugador3_resultado = "Jugador 3"
            self.text_jugador3_resultado_surface = self.vGlobales.font4.render(self.text_jugador3_resultado,True,self.vGlobales.amarillo)
            self.text_jugador3_resultado_rect = self.text_jugador3_resultado_surface.get_rect(center=(440,430))
            self.vGlobales.PANTALLA.blit(self.text_jugador3_resultado_surface,self.text_jugador3_resultado_rect)
            #Texto que mostrara las kills del jugador 3
            self.text_kills_jugador3 = str(lista_tanques_OG[2].total_kills)
            self.text_kills_jugador3_surface = self.vGlobales.font4.render(self.text_kills_jugador3,True,self.vGlobales.BLANCO)
            self.text_kills_jugador3_rect = self.text_kills_jugador3_surface.get_rect(center=(820,430))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador3_surface,self.text_kills_jugador3_rect)
            #Texto que mostrara las veces que se mato el jugador 3
            self.text_suicidios_jugador3 = str(lista_tanques_OG[2].cantidad_suicidios)
            self.text_suicidios_jugador3_surface = self.vGlobales.font4.render(self.text_suicidios_jugador3,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador3_rect = self.text_suicidios_jugador3_surface.get_rect(center=(990,430))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador3_surface,self.text_suicidios_jugador3_rect)
            #Texto que mostrara el saldo del jugador 3
            self.text_saldo_jugador3 = "$" + str(lista_tanques_OG[2].saldo)
            self.text_saldo_jugador3_surface = self.vGlobales.font4.render(self.text_saldo_jugador3,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador3_rect = self.text_saldo_jugador3_surface.get_rect(center=(1160,430))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador3_surface,self.text_saldo_jugador3_rect)
        if num_jugadores>=4:
            #Texto que dira "Jugador 4"
            self.text_jugador4_resultado = "Jugador 4"
            self.text_jugador4_resultado_surface = self.vGlobales.font4.render(self.text_jugador4_resultado,True,self.vGlobales.celeste)
            self.text_jugador4_resultado_rect = self.text_jugador4_resultado_surface.get_rect(center=(440,480))                            
            self.vGlobales.PANTALLA.blit(self.text_jugador4_resultado_surface,self.text_jugador4_resultado_rect)
            #Texto que mostrara las kills del jugador 4
            self.text_kills_jugador4 = str(lista_tanques_OG[3].total_kills)
            self.text_kills_jugador4_surface = self.vGlobales.font4.render(self.text_kills_jugador4,True,self.vGlobales.BLANCO)
            self.text_kills_jugador4_rect = self.text_kills_jugador4_surface.get_rect(center=(820,480))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador4_surface,self.text_kills_jugador4_rect)
            #Texto que mostrara las veces que se mato el jugador 4
            self.text_suicidios_jugador4 = str(lista_tanques_OG[3].cantidad_suicidios)
            self.text_suicidios_jugador4_surface = self.vGlobales.font4.render(self.text_suicidios_jugador4,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador4_rect = self.text_suicidios_jugador4_surface.get_rect(center=(990,480))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador4_surface,self.text_suicidios_jugador4_rect)
            #Texto que mostrara el saldo del jugador 4
            self.text_saldo_jugador4 = "$" + str(lista_tanques_OG[3].saldo)
            self.text_saldo_jugador4_surface = self.vGlobales.font4.render(self.text_saldo_jugador4,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador4_rect = self.text_saldo_jugador4_surface.get_rect(center=(1160,480))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador4_surface,self.text_saldo_jugador4_rect)
        if num_jugadores>=5:
            #Texto que dira "Jugador 5"
            self.text_jugador5_resultado = "Jugador 5"
            self.text_jugador5_resultado_surface = self.vGlobales.font4.render(self.text_jugador5_resultado,True,self.vGlobales.morado)
            self.text_jugador5_resultado_rect = self.text_jugador5_resultado_surface.get_rect(center=(440,530))            
            self.vGlobales.PANTALLA.blit(self.text_jugador5_resultado_surface,self.text_jugador5_resultado_rect)
            #Texto que mostrara las kills del jugador 5
            self.text_kills_jugador5 = str(lista_tanques_OG[4].total_kills)
            self.text_kills_jugador5_surface = self.vGlobales.font4.render(self.text_kills_jugador5,True,self.vGlobales.BLANCO)
            self.text_kills_jugador5_rect = self.text_kills_jugador5_surface.get_rect(center=(820,530))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador5_surface,self.text_kills_jugador5_rect)
            #Texto que mostrara las veces que se mato el jugador 5
            self.text_suicidios_jugador5 = str(lista_tanques_OG[4].cantidad_suicidios)
            self.text_suicidios_jugador5_surface = self.vGlobales.font4.render(self.text_suicidios_jugador5,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador5_rect = self.text_suicidios_jugador5_surface.get_rect(center=(990,530))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador5_surface,self.text_suicidios_jugador5_rect)
            #Texto que mostrara el saldo del jugador 5
            self.text_saldo_jugador5 = "$" + str(lista_tanques_OG[4].saldo)
            self.text_saldo_jugador5_surface = self.vGlobales.font4.render(self.text_saldo_jugador5,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador5_rect = self.text_saldo_jugador5_surface.get_rect(center=(1160,530))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador5_surface,self.text_saldo_jugador5_rect)
        if num_jugadores>=6:
            #Texto que dira "Jugador 6"
            self.text_jugador6_resultado = "Jugador 6"
            self.text_jugador6_resultado_surface = self.vGlobales.font4.render(self.text_jugador6_resultado,True,self.vGlobales.naranjo)
            self.text_jugador6_resultado_rect = self.text_jugador6_resultado_surface.get_rect(center=(440,580))            
            self.vGlobales.PANTALLA.blit(self.text_jugador6_resultado_surface,self.text_jugador6_resultado_rect)
            #Texto que mostrara las kills del jugador 6
            self.text_kills_jugador6 = str(lista_tanques_OG[5].total_kills)
            self.text_kills_jugador6_surface = self.vGlobales.font4.render(self.text_kills_jugador6,True,self.vGlobales.BLANCO)
            self.text_kills_jugador6_rect = self.text_kills_jugador6_surface.get_rect(center=(820,580))
            self.vGlobales.PANTALLA.blit(self.text_kills_jugador6_surface,self.text_kills_jugador6_rect)
            #Texto que mostrara las veces que se mato el jugador 6
            self.text_suicidios_jugador6 = str(lista_tanques_OG[5].cantidad_suicidios)
            self.text_suicidios_jugador6_surface = self.vGlobales.font4.render(self.text_suicidios_jugador6,True,self.vGlobales.BLANCO)
            self.text_suicidios_jugador6_rect = self.text_suicidios_jugador6_surface.get_rect(center=(990,580))
            self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador6_surface,self.text_suicidios_jugador6_rect)
            #Texto que mostrara el saldo del jugador 6
            self.text_saldo_jugador6 = "$" + str(lista_tanques_OG[5].saldo)
            self.text_saldo_jugador6_surface = self.vGlobales.font4.render(self.text_saldo_jugador6,True,self.vGlobales.BLANCO)
            self.text_saldo_jugador6_rect = self.text_saldo_jugador6_surface.get_rect(center=(1160,580))
            self.vGlobales.PANTALLA.blit(self.text_saldo_jugador6_surface,self.text_saldo_jugador6_rect)
        #Texto que dira "Haga Click para Continuar"
        self.text_click = "Haga Click para Continuar"
        self.text_click_surface = self.vGlobales.font2.render(self.text_click,True,self.vGlobales.BLANCO)
        self.text_click_rect = self.text_click_surface.get_rect(center=(820,650))        
        #ZONA DE IMPRESION
        self.vGlobales.PANTALLA.blit(self.text_resultados_finales,self.text_resultados_finales_rect)
        self.vGlobales.PANTALLA.blit(self.text_bajas_surface,self.text_bajas_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_surface,self.text_suicidios_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_resultado_surface,self.text_saldo_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_jugador1_resultado_surface,self.text_jugador1_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_kills_jugador1_surface,self.text_kills_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador1_surface,self.text_suicidios_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_jugador1_surface,self.text_saldo_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_jugador2_resultado_surface,self.text_jugador2_resultado_rect)
        self.vGlobales.PANTALLA.blit(self.text_kills_jugador2_surface,self.text_kills_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_suicidios_jugador2_surface,self.text_suicidios_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_saldo_jugador2_surface,self.text_saldo_jugador2_rect)
        self.vGlobales.PANTALLA.blit(self.text_click_surface,self.text_click_rect)