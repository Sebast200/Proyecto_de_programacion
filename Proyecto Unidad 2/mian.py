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

def genera_terreno_pixel(pantalla, matriz):
    i = vGlobales.ancho_gris
    while (i < vGlobales.WIDTH):
        j = 0
        while (j < vGlobales.HEIGHT):
            if (pantalla.get_at((i,j)) == vGlobales.verde):
                matriz[i-vGlobales.ancho_gris][j] = (vGlobales.verde)
            else:
                matriz[i-vGlobales.ancho_gris][j] = (0,0,0,0)
            j+=1
        i+=1

    return matriz
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
    #Cargar imagenes
    icono = pygame.image.load("Proyecto Unidad 2/imagenes/tanque.png")
    pygame.display.set_icon(icono)
    fondo = pygame.image.load("Proyecto Unidad 2/imagenes/fondo.png")
    DISPLAYSURF.blit(fondo, (0,0))
    #Skin jugadores
    skin1 = pygame.image.load("Proyecto Unidad 2/imagenes/skin1.png")
    skin2 = pygame.image.load("Proyecto Unidad 2/imagenes/skin2.png")

    #Objetos en pantalla
    sprites = pygame.sprite.Group()
    tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.ancho_gris + 10,(vGlobales.WIDTH - vGlobales.ancho_gris)/2 + vGlobales.ancho_gris ))
    tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint((vGlobales.WIDTH- vGlobales.ancho_gris)/2 + tanque1.rect.x, vGlobales.WIDTH - 10))    
    bala_g = bala.Balas(vGlobales.bala_grande, vGlobales.daño_bala_g, vGlobales.unidades_cyg)
    bala_m = bala.Balas(vGlobales.bala_mediana, vGlobales.daño_bala_m, vGlobales.unidades_m)
    bala_c = bala.Balas(vGlobales.bala_chica, vGlobales.daño_bala_c, vGlobales.unidades_cyg)
    sprites.add(tanque1), sprites.add(tanque2)
    sprites.add(bala_g)
    sprites.add(bala_m)
    sprites.add(bala_c)
    recorrido = []

    #Creacion de variables en main (por ahora)
    turno_jugador = 2
    turno_pasado = 0 

    #generacion del terreno
    vGlobales.generar_terreno()
    pantalla_juego = pygame.Surface((vGlobales.WIDTH-vGlobales.ancho_gris,vGlobales.HEIGHT),pygame.SRCALPHA)
    pixel_array = pygame.PixelArray(pantalla_juego)
    pixel_array = genera_terreno_pixel(DISPLAYSURF,pixel_array)
    nueva_superficie = pixel_array.make_surface()

    def mostrar_distancias(tanque1, tanque2, bala):
        bala.update(tanque1,tanque2)
        #Altura bala
        interfaz.text_altura_maxima = str(bala.altaura_max) + " metros"
        interfaz.text_surface_altura_maxima = interfaz.vGlobales.font.render(interfaz.text_altura_maxima, True, interfaz.vGlobales.NEGRO)
        interfaz.text_surface_altura_maxima_rect = interfaz.text_surface_altura_maxima.get_rect(center = (bala.coordenadas_altura_max))
        #Distancia bala
        interfaz.text_distancia_maxima = str(bala.distancia_max) + "metros"
        interfaz.text_surface_distancia_maxima = interfaz.vGlobales.font.render(interfaz.text_distancia_maxima, True, interfaz.vGlobales.NEGRO)
        interfaz.text_surface_distancia_maxima_rect = interfaz.text_surface_distancia_maxima.get_rect(center = (bala.coordenadas_distancia))

    def calcular_recorrido(bala, reco):
        if (bala.contador_recorrido % 5) == 0 and bala.caida == True :
            reco = reco + [(bala.rect.x, bala.rect.y)]
        return reco
    
    def mostrar_recorrido(reco):
        i=0
        while (i<len(reco)):
            pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(reco[i]),5)
            i+=1

    def descuento_balas_tanque1(bala):
        if turno_pasado == 0:
            bala.unidades_tanque1 -= 1
            print("balas tanque 1: ", bala.unidades_tanque1)
    def descuento_balas_tanque2(bala):
        if turno_pasado == 0:
            bala.unidades_tanque2 -= 1
            print("balas tanque 2: ", bala.unidades_tanque2)
            
    def destruccion_terreno(bala, pixel_array, nueva_superficie):
        pixel_array = bala.rompe_terreno(pixel_array,bala.tipo/2,bala.rect.center)
        nueva_superficie = pixel_array.make_surface()
        bala.explosion=0
        return nueva_superficie
    
    def animacion_explosion(radio_bala, bala):
        i = 0
        while i < radio_bala:
            pygame.draw.circle(DISPLAYSURF,'black',(bala.rect.center),i/2)
            i+=0.5
            pygame.display.flip()

    while True:
        #Dibujo de la pantalla
        DISPLAYSURF.blit(fondo,(0,0))

        #Dibuja el terreno
        DISPLAYSURF.blit(nueva_superficie,(vGlobales.ancho_gris,0))
        if (bala_c.explosion == 1 and bala_c.caida == False):
                nueva_superficie = destruccion_terreno(bala_c, pixel_array, nueva_superficie)
        elif (bala_m.explosion == 1 and bala_m.caida == False):
            nueva_superficie = destruccion_terreno(bala_m, pixel_array, nueva_superficie)
        elif (bala_g.explosion == 1 and bala_g.caida == False):
            nueva_superficie = destruccion_terreno(bala_g, pixel_array, nueva_superficie)
        #Interfaz
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(0,0,vGlobales.ancho_gris,vGlobales.HEIGHT))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                interfaz.click_mouse_inventario(event.pos)
                if turno_jugador == 1:
                    if interfaz.minibox_bala1_active == True and bala_c.unidades_tanque1 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_c,tanque1, turno_pasado, turno_jugador)
                        descuento_balas_tanque1(bala_c)
                        recorrido.clear()
                    if interfaz.minibox_bala2_active == True and bala_m.unidades_tanque1 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_m,tanque1, turno_pasado, turno_jugador)
                        descuento_balas_tanque1(bala_m)
                        recorrido.clear()   
                    if interfaz.minibox_bala3_active == True and bala_g.unidades_tanque1 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_g,tanque1, turno_pasado, turno_jugador)
                        descuento_balas_tanque1(bala_g)
                        recorrido.clear()      
                else:
                    if interfaz.minibox_bala1_active == True and bala_c.unidades_tanque2 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_c,tanque2, turno_pasado, turno_jugador)
                        descuento_balas_tanque2(bala_c)
                        recorrido.clear()                    
                    if interfaz.minibox_bala2_active == True and bala_m.unidades_tanque2 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_m,tanque2, turno_pasado, turno_jugador)
                        descuento_balas_tanque2(bala_m)
                        recorrido.clear()
                    if interfaz.minibox_bala3_active == True and bala_g.unidades_tanque2 > 0:
                        turno_pasado = interfaz.click_mouse(event.pos,bala_g,tanque2, turno_pasado, turno_jugador)
                        descuento_balas_tanque2(bala_g)
                        recorrido.clear()
            if event.type == pygame.KEYDOWN:
                interfaz.escribir(event)
        #SPRITES
        tanque1.update()
        tanque2.update()
        #Distancia del disparo
        if turno_jugador == 1:
            if interfaz.minibox_bala1_active == True:
                mostrar_distancias(tanque2, tanque1, bala_c)
            if interfaz.minibox_bala2_active == True:
                mostrar_distancias(tanque2, tanque1, bala_m)
            if interfaz.minibox_bala3_active == True:
                mostrar_distancias(tanque2, tanque1, bala_g)
        elif turno_jugador == 2:
            if interfaz.minibox_bala1_active == True:
                mostrar_distancias(tanque1, tanque2, bala_c)
            if interfaz.minibox_bala2_active == True:
                mostrar_distancias(tanque1, tanque2, bala_m)
            if interfaz.minibox_bala3_active == True:
                mostrar_distancias(tanque1, tanque2, bala_g)     
        sprites.draw(DISPLAYSURF)
        
        #Recorrido de la bala
        if interfaz.minibox_bala1_active == True:
            recorrido = calcular_recorrido(bala_c, recorrido)
            mostrar_recorrido(recorrido)
        if interfaz.minibox_bala2_active == True:
            recorrido = calcular_recorrido(bala_m, recorrido)
            mostrar_recorrido(recorrido)
        if interfaz.minibox_bala3_active == True:
            recorrido = calcular_recorrido(bala_g, recorrido)
            mostrar_recorrido(recorrido)
        
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
        if turno_jugador == 1:
            interfaz.print_interfaz(bala_c.unidades_tanque1,bala_m.unidades_tanque1,bala_g.unidades_tanque1)
        else:
            interfaz.print_interfaz(bala_c.unidades_tanque2,bala_m.unidades_tanque2,bala_g.unidades_tanque2)
        interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_altura_maxima, interfaz.text_surface_altura_maxima_rect)
        interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_distancia_maxima, interfaz.text_surface_distancia_maxima_rect)
        ####
        if bala_c.explosion == 1:
            animacion_explosion(vGlobales.bala_chica, bala_c)
        elif bala_m.explosion == 1:
            animacion_explosion(vGlobales.bala_mediana, bala_m)
        elif bala_g.explosion == 1:
            animacion_explosion(vGlobales.bala_grande,bala_g)
        pygame.display.flip()
        RELOJ.tick(vGlobales.FPS)
menu_principal()
#Fin de creacion de metodos del menu

#CAMBIOS REALIZADOS
#1.- SE AGREGARON METODOS NUEVOS PARA HACER EL MENU
#2.- SE IMPORTO LA CLASE boton en la linea 3
#3.- Se agregaron dos tipos de fonts a globales

#NUEVOS CAMBIOS
#1.- SE CAMBIARON LAS CONDICIONES DE LA LINEA 171 HASTA LA 212, de todas formas deje en # las condicionales anteriores por si llega a pasar algo malo
#2.- SE CAMBIARON LAS CONDICIONES DE LA LINEA 227 HASTA LA 274, de todas formas deje en # las condicionales anteriores por si llega a pasar algo malo
#NUEVOS CAMBIOS (FRANCO ARENAS) 11-10-2023
#1.- Voy a hacer que print interfaz pida los datos del tanque para poder imprimir la cantidad de balas que les queda a cada uno
#2.- Linea 325 aprox (ahora es la linea 277), voy a crear una condicional que preguntara que turno es para ver QUE dato debe de imprimir con respecto al inventario