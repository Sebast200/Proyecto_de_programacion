import pygame, sys
from pygame.locals import*
from button import Button
pygame.init()

WIDTH = 1280
HEIGHT = 720

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
#ADVERTENCIA - Este menu es un prototipo, mas adelante sera cambiado por uno mas bonito XD
#Aqui hay que colocar la direccion en la que quedara la imagen, por ahora la tendre en la carpeta assets y vere si funciona o no
IMAGEN_DE_FONDO = pygame.image.load("assets/BG_MAIN_MENU.png")#la imagen de fondo sera cambiada cuando haya tiempo, y lo mismo con botones y todo
#----- DEFINICION DE COLORES
BLANCO = (255,255,255)
ROJO = (255,0,0)
#----- DEFINICION DE COLORES

def get_font(tamaño):
    return pygame.font.Font(None,tamaño)

#def play() - en este def hay que meter todo lo que se trata de jugar la partida de tanques

def opciones():
    pygame.display.set_caption("Opciones")

    while True:
        #blit es un metodo usado para copiar una superficie ya sea una imagen o texto, en otra superficie
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        TEXTO_OPCIONES = get_font(100).render("OPCIONES", True, BLANCO)
        TEXTO_DESCRIPCION = get_font(50).render("De momento no tenemos las opciones listas xd", True, BLANCO)
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(640, 100))
        DESCRIPCION_RECT = TEXTO_DESCRIPCION.get_rect(center=(640,400))


        #Creacion de botones
        BOTON_VOLVER = Button(image=None, pos=(640,550), text_input="VOLVER", font=get_font(75), base_color=ROJO, hovering_color=BLANCO)
        
        #usamos blit para poner el texto de TEXTO_MENU en la ventana centrado con MENU_RECT
        DISPLAYSURF.blit(TEXTO_OPCIONES, OPCIONES_RECT)
        DISPLAYSURF.blit(TEXTO_DESCRIPCION, DESCRIPCION_RECT)
        
        #Aqui damos un for en el que basicamente dice que cuando nosotros pasemos el mouse por encima, cambien de color y se actualice esa informacion en la pantalla principal
        for boton in [BOTON_VOLVER]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Cosas que pasaran si ocurren los siguientes eventos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_VOLVER.checkForInput(MENU_MOUSE_POS):
                    #Si la persona le hace click al boton de volver, regresara al menu principal
                    menu_principal()
        pygame.display.update()


def menu_principal():
    pygame.display.set_caption("Menu")

    while True:
        #blit es un metodo usado para copiar una superficie ya sea una imagen o texto, en otra superficie
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        TEXTO_MENU = get_font(100).render("MENU PRINCIPAL", True, BLANCO)
        MENU_RECT = TEXTO_MENU.get_rect(center=(640, 100))

        #Creacion de botones
        BOTON_JUGAR = Button(image=None, pos=(320,350), text_input="JUGAR", font=get_font(75), base_color=ROJO, hovering_color=BLANCO)
        BOTON_OPCIONES = Button(image=None, pos=(960,350),text_input="OPCIONES", font=get_font(75), base_color=ROJO, hovering_color=BLANCO)
        BOTON_SALIR = Button(image= None, pos=(640,550),text_input="SALIR", font=get_font(75), base_color=ROJO,hovering_color=BLANCO)

        #usamos blit para poner el texto de TEXTO_MENU en la ventana centrado con MENU_RECT
        DISPLAYSURF.blit(TEXTO_MENU, MENU_RECT)
        
        #Aqui damos un for en el que basicamente dice que cuando nosotros pasemos el mouse por encima, cambien de color y se actualice esa informacion en la pantalla principal
        for boton in [BOTON_JUGAR, BOTON_OPCIONES,BOTON_SALIR]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Cosas que pasaran si ocurren los siguientes eventos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS):
                    opciones()
                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    #Si la persona le hace click al boton de salir, se cerrara el programa
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
menu_principal()