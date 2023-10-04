import pygame, sys, globales, tanque, bala, random, interfaz
from pygame.locals import *
from boton import Button
from pygame import mixer   
#DECLARACIONES
pygame.init()
interfaz = interfaz.Interfazz()
#Musica de fondo
mixer.music.load("Proyecto Unidad 2/sonidos_musica/background.mp3")
mixer.music.play(-1)
#variables globales
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()
#pantalla
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanques Lovers Juego")
#Creacion de variable de imagen de fondo
IMAGEN_DE_FONDO = pygame.image.load("Proyecto Unidad 2/imagenes/BG_MAIN_MENU.png")
#Creacion de metodos del menu. estos metodos los podemos intentar tirar a una clase despues si quieren
def get_font(tamaño):
    return pygame.font.Font(None,tamaño)
def opciones():
    pygame.display.set_caption("Opciones")

    while True:
        #blit es un metodo usado para copiar una superficie ya sea una imagen o texto, en otra superficie
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        TEXTO_OPCIONES = vGlobales.font3.render("OPCIONES", True, vGlobales.BLANCO)
        TEXTO_DESCRIPCION = vGlobales.font2.render("De momento no tenemos las opciones listas xd", True, vGlobales.BLANCO)
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(640, 100))
        DESCRIPCION_RECT = TEXTO_DESCRIPCION.get_rect(center=(640,400))


        #Creacion de botones
        BOTON_VOLVER = Button(image=None, pos=(640,550), text_input="VOLVER", font=get_font(75), base_color=vGlobales.ROJO, hovering_color=vGlobales.BLANCO)
        
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

        TEXTO_MENU = vGlobales.font3.render("MENU PRINCIPAL", True, vGlobales.BLANCO)
        MENU_RECT = TEXTO_MENU.get_rect(center=(640, 100))

        #Creacion de botones
        BOTON_JUGAR = Button(image=None, pos=(320,350), text_input="JUGAR", font=get_font(75), base_color=vGlobales.ROJO, hovering_color=vGlobales.BLANCO)
        BOTON_OPCIONES = Button(image=None, pos=(960,350),text_input="OPCIONES", font=get_font(75), base_color=vGlobales.ROJO, hovering_color=vGlobales.BLANCO)
        BOTON_SALIR = Button(image= None, pos=(640,550),text_input="SALIR", font=get_font(75), base_color=vGlobales.ROJO,hovering_color=vGlobales.BLANCO)

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
                if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                    #Testeoaa de musica al inicio del juego tiene que estar atento a cambios
                    mixer.music.fadeout(1500)
                    mixer.music.load("Proyecto Unidad 2/sonidos_musica/init_game.mp3")
                    mixer.music.play(-1)
                    partida()
        pygame.display.update()

def partida():

    #imagenes
    icono = pygame.image.load("Proyecto Unidad 2/imagenes/tanque.png")
    pygame.display.set_icon(icono)
    #fondo
    fondo = pygame.image.load("Proyecto Unidad 2/imagenes/fondo.png")
    DISPLAYSURF.blit(fondo, (0,0))

    #jugador 1
    skin1 = pygame.image.load("Proyecto Unidad 2/imagenes/skin1.png")
    skin2 = pygame.image.load("Proyecto Unidad 2/imagenes/skin2.png")

    #objetos en pantalla
    sprites = pygame.sprite.Group()
    tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.ancho_gris + 10,(vGlobales.WIDTH - vGlobales.ancho_gris)/2 + vGlobales.ancho_gris ))
    tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint((vGlobales.WIDTH- vGlobales.ancho_gris)/2 + tanque1.rect.x, vGlobales.WIDTH - 10))    
    bala_g = bala.Balas(vGlobales.bala_grande, vGlobales.daño_bala_g, vGlobales.unidades_cyg)
    bala_m = bala.Balas(vGlobales.bala_mediana, vGlobales.daño_bala_m, vGlobales.unidades_m)
    bala_c = bala.Balas(vGlobales.bala_chica, vGlobales.daño_bala_c, vGlobales.unidades_cyg)
    sprites.add(tanque1)
    sprites.add(tanque2)
    sprites.add(bala_g)
    sprites.add(bala_m)
    sprites.add(bala_c)
    recorrido = []

    #Creacion de variables en main (por ahora)
    turno_jugador = 2
    turno_pasado = 0
    tipo_bala = 1

    def mostrar_altura(tanque1, tanque2, bala):
        bala.update(tanque1,tanque2)
        interfaz.text_altura_maxima = str(bala.altaura_max) + " metros"
        interfaz.text_surface_altura_maxima = interfaz.vGlobales.font.render(interfaz.text_altura_maxima, True, interfaz.vGlobales.NEGRO)
        interfaz.text_surface_altura_maxima_rect = interfaz.text_surface_altura_maxima.get_rect(center = (bala.coordenadas_altura_max))

    while True:
        #Dibujo de la pantalla
        DISPLAYSURF.blit(fondo,(0,0))
        vGlobales.terreno()
        #Interfaz
        interfaz.interfaz()
        
        #proceso de cambio de turno
        if turno_jugador == 1 and turno_pasado == 0:
            turno_jugador = 2
            turno_pasado = 1
            print("Es el turno del jugador 2")
        elif turno_jugador == 2 and turno_pasado == 0:
            turno_jugador = 1
            turno_pasado = 1
            print("Es el turno del jugador 1")

        #bucle para cerrar el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if bala_g.caida != True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turno_jugador == 1:
                        if tipo_bala == 1:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_c,tanque1, turno_pasado, turno_jugador)
                            recorrido.clear()
                        if tipo_bala == 2:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_m,tanque1, turno_pasado, turno_jugador)
                            recorrido.clear()
                        if tipo_bala == 3:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_g,tanque1, turno_pasado, turno_jugador)
                            recorrido.clear()
                    else:
                        if tipo_bala == 1:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_c,tanque2, turno_pasado, turno_jugador)
                            recorrido.clear()
                        if tipo_bala == 2:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_m,tanque2, turno_pasado, turno_jugador)
                            recorrido.clear()
                        if tipo_bala == 3:
                            turno_pasado = interfaz.click_mouse(event.pos,bala_g,tanque2, turno_pasado, turno_jugador)
                            recorrido.clear()

            if event.type == pygame.KEYDOWN:
                interfaz.escribir(event)

        #SPRITES
        tanque1.update()
        tanque2.update()

        if turno_jugador == 1:
            if tipo_bala == 1:
                mostrar_altura(tanque2, tanque1, bala_c)
            if tipo_bala == 2:
                mostrar_altura(tanque2, tanque1, bala_m)
            if tipo_bala == 3:
                mostrar_altura(tanque2, tanque1, bala_g)

        elif turno_jugador == 2:
            if tipo_bala == 1:
                mostrar_altura(tanque1, tanque2, bala_c)
            if tipo_bala == 2:
                mostrar_altura(tanque1, tanque2, bala_m)
            if tipo_bala == 3:
                mostrar_altura(tanque1, tanque2, bala_g)

        sprites.draw(DISPLAYSURF)
        
        #Recorrido de la bala
        if tipo_bala == 1:
            if (bala_c.contador_recorrido % 5) == 0 and bala_c.caida == True :
                recorrido = recorrido + [(bala_c.rect.x, bala_c.rect.y)]
            i=0
            while (i<len(recorrido)):
                pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(recorrido[i]),5)
                i+=1

        if tipo_bala == 2:
            if (bala_m.contador_recorrido % 5) == 0 and bala_m.caida == True :
                recorrido = recorrido + [(bala_m.rect.x, bala_m.rect.y)]
            i=0
            while (i<len(recorrido)):
                pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(recorrido[i]),5)
                i+=1

        if tipo_bala == 3:
            if (bala_g.contador_recorrido % 5) == 0 and bala_g.caida == True :
                recorrido = recorrido + [(bala_g.rect.x, bala_g.rect.y)]
            i=0
            while (i<len(recorrido)):
                pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(recorrido[i]),5)
                i+=1
        
        #Skins
        DISPLAYSURF.blit(skin1, (tanque1.rect.x-10,tanque1.rect.y-5))
        DISPLAYSURF.blit(skin2, (tanque2.rect.x-10,tanque2.rect.y-5))
        
        #Game over
        if (tanque1.vida <= 0 or tanque2.vida <= 0):
            while True:
                interfaz.text_game_over = "GAME OVER"
                interfaz.text_surface_game_over = interfaz.vGlobales.font.render(interfaz.text_game_over, True, interfaz.vGlobales.rojo_oscuro)
                interfaz.text_surface_game_over_rect = interfaz.text_surface_game_over.get_rect(center = ((interfaz.vGlobales.WIDTH/2) + 140,(interfaz.vGlobales.HEIGHT/2) - 30))
                interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_game_over, interfaz.text_surface_game_over_rect)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        sys.exit()
                        
        #Inicio de interfaz
        interfaz.print_interfaz()
        interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_altura_maxima, interfaz.text_surface_altura_maxima_rect)
        pygame.display.flip()
        RELOJ.tick(vGlobales.FPS)
menu_principal()
#Fin de creacion de metodos del menu


#CAMBIOS REALIZADOS
#1.- SE AGREGARON METODOS NUEVOS PARA HACER EL MENU
#2.- SE IMPORTO LA CLASE boton en la linea 3
#3.- Se agregaron dos tipos de fonts a globales
