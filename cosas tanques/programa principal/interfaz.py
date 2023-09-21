import pygame, sys, globales, math
from pygame.locals import *

class Interfazz():
    def __init__(self):
        self.vGlobales = globales.Globaless()
        #           self.font=self.font = pygame.font.Font(None,36)
       #Creo que aqui toca dibujar la interfaz

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
        #FIN DE CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
        #Ahora que lo pienso, quizas tambien tenga que crear en el main el rectangulo que va a decir disparar, ya que asi puedo colocar las condiciones aqui de una forma mas sencilla
        #Voy a probar a crear el rectangulo aqui, ya que la idea es que el usuario pueda hacerle click al rectangulo en vez de apretar enter
        self.text_boton_jugador = "Dispara"
        self.text_boton_jugador_rect = pygame.Rect(20,600,220,80)
        self.text_boton_jugador_color = self.vGlobales.verde
        #Voy a crear


    def interfaz(self):
        #CREACION DE INTERFAZ PARA JUGADOR 1

        #Texto que dice jugador 1 con letras azules
        self.text_jugador1 = "Jugador 1"
        self.text_surface_jugador1 = self.vGlobales.font.render(self.text_jugador1, True, self.vGlobales.AZUL)
        self.text_surface_jugador1_rect = self.text_surface_jugador1.get_rect(center = (120,40))

        #Texto que dice Angulo...
        self.text_angulo_jugador1 = "Angulo:"
        self.text_surface_angulo_jugador1 = self.vGlobales.font.render(self.text_angulo_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_angulo_jugador1_rect = self.text_surface_angulo_jugador1.get_rect(center = (80,200))

        #Forma 2 (posiblemente la mas facil pero pajera(?))
        #Esta forma consiste en crear dos textos, uno que diga velocidad y otra que diga inicial, para intentar ser un poco mas ordenado xd
        self.text_velocidad_jugador1 = "Velocidad"
        self.text_surface_velocidad_jugador1 = self.vGlobales.font.render(self.text_velocidad_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_velocidad_jugador1_rect = self.text_surface_velocidad_jugador1.get_rect(center = (80,360))
        
        self.text_inicial_jugador1 = "inicial:"
        self.text_surface_inicial_jugador1 = self.vGlobales.font.render(self.text_inicial_jugador1, True, self.vGlobales.NEGRO)
        self.text_surface_inicial_jugador1_rect = self.text_surface_inicial_jugador1.get_rect(center = (80,390))


        self.vGlobales.PANTALLA.blit(self.text_surface_jugador1,self.text_surface_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_angulo_jugador1,self.text_surface_angulo_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_velocidad_jugador1,self.text_surface_velocidad_jugador1_rect)
        self.vGlobales.PANTALLA.blit(self.text_surface_inicial_jugador1,self.text_surface_inicial_jugador1_rect)
        #de aqui a abajo ya no forma parte de la forma 2 xd

        #CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
        #Rectangulo de la caja de texto
        self.textbox_angulo_rect = pygame.Rect(150,180,80,40)
        #Rectangulo de la caja de texto
        self.textbox_velocidad_inicial_rect = pygame.Rect(150,355,80,40)
        #FIN DE CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
        #Ahora que lo pienso, quizas tambien tenga que crear en el main el rectangulo que va a decir disparar, ya que asi puedo colocar las condiciones aqui de una forma mas sencilla
        #Voy a probar a crear el rectangulo aqui, ya que la idea es que el usuario pueda hacerle click al rectangulo en vez de apretar enter
        self.text_boton_jugador = "Dispara"
        self.text_boton_jugador_rect = pygame.Rect(20,600,220,80)
        self.text_boton_jugador_color = self.vGlobales.verde
        #FIN DE CREACION DE INTERFAZ PARA JUGADOR 1
        #-----
        #Voy a probar con implementar los cuadros de texto por aqui y ver si sale bien algo o no xddd    

    def boton_disparar_click (self, bala, pos_tanque):
        try:
            numero_angulo = int(self.textbox_angulo)
            numero_velocidad_inicial = int(self.textbox_velocidad_inicial)
            #Por ahora la unica condicion sera que el numero del angulo no supere los 360 grados
            if numero_angulo>360:
                self.textbox_angulo = ""
            else:
                #Voy a colocar por ahora aqui el metodo disparo para simular que el boton cause el disparo y que por ende tambien cambie de color
                bala.disparar(numero_angulo, math.pi/180 * (numero_angulo + 90), numero_velocidad_inicial,pos_tanque)
                text_boton_jugador = "Recarga"
                text_boton_jugador_color = self.vGlobales.ROJO
                pygame.draw.rect(self.vGlobales.PANTALLA,text_boton_jugador_color,self.text_boton_jugador_rect)
                self.text_boton_jugador_surface = self.vGlobales.font.render(text_boton_jugador,True,self.vGlobales.BLANCO)

        except ValueError:
            self.textbox_angulo = ""
            self.textbox_velocidad_inicial = ""

    def click_mouse(self, posicion_muose,bala,pos_tanque):
        if self.textbox_angulo_rect.collidepoint( posicion_muose):
            self.textbox_angulo_active = True
        else:
            self.textbox_angulo_active = False
        #Condicion de click para el cuadro de velocidad inicial
        if self.textbox_velocidad_inicial_rect.collidepoint(posicion_muose):
            self.textbox_velocidad_inicial_active = True
        else:
            self.textbox_velocidad_inicial_active = False

        if self.text_boton_jugador_rect.collidepoint(posicion_muose):
            self.boton_disparar_click(bala, pos_tanque)

    def escribir (self, evento):
        #Seccion de codigo de caja de texto de angulo
            if self.textbox_angulo_active == True:
                if evento.key == pygame.K_BACKSPACE:
                    self.textbox_angulo = self.textbox_angulo[:-1]

                if evento.unicode.isnumeric():
                    #Voy a ver si hay una forma de limitar a que solo hayan tres numeros ingresados
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

        #NUMEROS MAGICOS
        self.vGlobales.PANTALLA.blit(self.textbox_angulo_surface, (self.textbox_angulo_rect.x + 15, self.textbox_angulo_rect.y + 10))
        self.vGlobales.PANTALLA.blit(self.textbox_velocidad_inicial_surface,(self.textbox_velocidad_inicial_rect.x + 15, self.textbox_velocidad_inicial_rect.y + 10))
        self.vGlobales.PANTALLA.blit(self.text_boton_jugador_surface, (self.text_boton_jugador_rect.x + 65, self.text_boton_jugador_rect.y + 25))
