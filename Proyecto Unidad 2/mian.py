import pygame, sys, globales, tanque, bala, random, interfaz
from pygame.locals import *
from boton import Button
from pygame import mixer   

#DECLARACIONES
pygame.init()
interfaz = interfaz.Interfazz()

#MUSICA DE FONDO
mixer.music.load("Proyecto Unidad 2/sonidos_musica/background.mp3")
mixer.music.play(-1)

#VARIABLES GLOBALES
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()

#PANTALLA
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanques Lovers Juego")
#Creacion de variable de imagen de fondo
IMAGEN_DE_FONDO = pygame.image.load("Proyecto unidad 2/imagenes/BG_MAIN_MENU.png")

#FUNCIONES GENERALES
def get_font(tamaño): #Obtiene la fuente a usar en el juego
    return pygame.font.Font("Proyecto unidad 2/font/Pixellari.ttf",tamaño) 

def genera_terreno_pixel(pantalla, matriz): #Retorna una copia del terreno para el pixel_array
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

def mostrar_distancias(tanque1, tanque2, bala, superfice, pixel_array, lista_tanques, num_jugadores): 
        superfice = bala.update(tanque1,tanque2, superfice, pixel_array, lista_tanques, num_jugadores)
        #Altura bala
        interfaz.text_altura_maxima = str(bala.altaura_max) + " metros"
        interfaz.text_surface_altura_maxima = interfaz.vGlobales.font.render(interfaz.text_altura_maxima, True, interfaz.vGlobales.NEGRO)
        interfaz.text_surface_altura_maxima_rect = interfaz.text_surface_altura_maxima.get_rect(center = (bala.coordenadas_altura_max))
        #Distancia bala
        interfaz.text_distancia_maxima = str(bala.distancia_max) + "metros"
        interfaz.text_surface_distancia_maxima = interfaz.vGlobales.font.render(interfaz.text_distancia_maxima, True, interfaz.vGlobales.NEGRO)
        interfaz.text_surface_distancia_maxima_rect = interfaz.text_surface_distancia_maxima.get_rect(center = (bala.coordenadas_distancia))
        return superfice

def calcular_recorrido(bala, reco): #Retorna el reccorido de la bala
        if (bala.contador_recorrido % 5) == 0 and bala.caida == True :
            reco = reco + [(bala.rect.x, bala.rect.y)]
        return reco

def mostrar_recorrido(reco):
    i=0
    while (i<len(reco)):
        pygame.draw.circle(DISPLAYSURF, vGlobales.NEGRO,(reco[i]),5)
        i+=1

def descuento_balas_tanque(bala,turno_pasado, turno_jugador,tanque):
    if bala.tipo == vGlobales.bala_chica and turno_pasado == 0:
        tanque.unidades_c -= 1
    if bala.tipo == vGlobales.bala_mediana and turno_pasado == 0:
        tanque.unidades_m -= 1
    if bala.tipo == vGlobales.bala_grande and turno_pasado == 0:
        tanque.unidades_g -= 1
    #turno_pasado == 0
        
def animacion_explosion(radio_bala, bala):
    i = 0
    while i < radio_bala:
        pygame.draw.circle(DISPLAYSURF,'black',(bala.rect.center),i/2)
        i+=0.5
        pygame.display.flip()

#Inicia el proceso para disparar la bala
def disparar_bala(event, bala, turno_pasado, turno_jugador, tanque, recorrido):
    turno_pasado = interfaz.click_mouse(event, bala, tanque, turno_pasado) #Permite pasar al siguiente turno
    descuento_balas_tanque(bala, turno_pasado, turno_jugador, tanque)
    #limpia recorrido de la bala si no esta en mivimiento
    if (bala.caida == False):
        recorrido.clear()
    return turno_pasado

#Animacion del soldado de la pantalla de inicio
def soldado_durmiendo_anim(current_sprite,pos_x,pos_y):
    sprite_set = []
    sprite_set.append(pygame.image.load("Proyecto Unidad 2/imagenes/Sleeping_soldier_1.png"))
    sprite_set.append(pygame.image.load("Proyecto Unidad 2/imagenes/Sleeping_soldier_2.png"))
    sprite_set.append(pygame.image.load("Proyecto Unidad 2/imagenes/Sleeping_soldier_3.png"))
    sprite_set.append(pygame.image.load("Proyecto Unidad 2/imagenes/Sleeping_soldier_4.png"))
    sprite_set.append(pygame.image.load("Proyecto Unidad 2/imagenes/Sleeping_soldier_5.png"))
    current_sprite = current_sprite + 0.04
    if current_sprite < 5:
        DISPLAYSURF.blit(sprite_set[int(current_sprite)], (pos_x,pos_y))
    else:
        DISPLAYSURF.blit(sprite_set[0], (pos_x,pos_y))
    if current_sprite >= 12:
        return 0
    else:
        return current_sprite
    
#Easter egg jiji
def fatality(fatality_check):
    if fatality_check == 0:
        mixer.music.load("Proyecto Unidad 2/sonidos_musica/fatality_bgm_1.mp3")
        mixer.music.play()
        mixer.music.queue("Proyecto Unidad 2/sonidos_musica/man_burning.mp3")
        fatality_check = 1
    if fatality_check == 1 and mixer.music.get_busy() == False:
        mixer.music.load("Proyecto Unidad 2/sonidos_musica/fatality_bgm_2.mp3")
        mixer.music.play(loops=0)
        burning_sound = mixer.Sound("Proyecto Unidad 2/sonidos_musica/burning_effect.mp3")
        burning_sound.play()
        fatality_check = 2
    elif fatality_check == 2:
        if mixer.music.get_pos() >= 500:
            fatality_sound = mixer.Sound("Proyecto Unidad 2/sonidos_musica/fatality_sfx.mp3")
            fatality_sound.play()
            fatality_check = 3
    if fatality_check == 3:
        fatality = pygame.image.load("Proyecto Unidad 2/imagenes/fatality.png")
        DISPLAYSURF.blit(fatality, (620,170))
    if fatality_check == 3 and mixer.music.get_busy() == False:
        pygame.quit()
        sys.exit()
    return fatality_check

#FUNCIONES PRINCIPALES
#Pantalla de opciones
def opciones(contador_soldado_anim):
    pygame.display.set_caption("Opciones")
    while True:
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        TEXTO_OPCIONES = vGlobales.font3.render("OPCIONES", True, vGlobales.BLANCO)
        TEXTO_DESCRIPCION = vGlobales.font2.render("De momento no tenemos las opciones listas xd", True, vGlobales.BLANCO)
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(640, 100))
        DESCRIPCION_RECT = TEXTO_DESCRIPCION.get_rect(center=(640,400))

        #Creacion de botones
        BOTON_VOLVER = Button(image=None, pos=(640,550), text_input="VOLVER", font=get_font(75), base_color=vGlobales.verde_oscuro, hovering_color=vGlobales.BLANCO)
        
        contador_soldado_anim = soldado_durmiendo_anim(contador_soldado_anim,850,430)
        DISPLAYSURF.blit(TEXTO_OPCIONES, OPCIONES_RECT)
        DISPLAYSURF.blit(TEXTO_DESCRIPCION, DESCRIPCION_RECT)
        
        for boton in [BOTON_VOLVER]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN: #Volver al menu principal
                if BOTON_VOLVER.checkForInput(MENU_MOUSE_POS):
                    menu_principal()

        pygame.display.update()
        
#Pantalla de menu principal
def menu_principal():
    contador_soldado_anim = 0
    pygame.display.set_caption("Menu")
    while True:
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        TEXTO_MENU = vGlobales.font3.render("TANK LOVER'S GAME", True, vGlobales.BLANCO)
        MENU_RECT = TEXTO_MENU.get_rect(center=(640, 100))
        contador_soldado_anim = soldado_durmiendo_anim(contador_soldado_anim,850,430)
        #Creacion de botones
        BOTON_JUGAR = Button(image=None, pos=(400,290), text_input="JUGAR", font=get_font(75), base_color=vGlobales.verde_oscuro, hovering_color=vGlobales.BLANCO)
        BOTON_OPCIONES = Button(image=None, pos=(400,415),text_input="OPCIONES", font=get_font(75), base_color=vGlobales.verde_oscuro, hovering_color=vGlobales.BLANCO)
        BOTON_SALIR = Button(image= None, pos=(400,540),text_input="SALIR", font=get_font(75), base_color=vGlobales.verde_oscuro,hovering_color=vGlobales.BLANCO)

        DISPLAYSURF.blit(TEXTO_MENU, MENU_RECT)
        
        for boton in [BOTON_JUGAR, BOTON_OPCIONES,BOTON_SALIR]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #click mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS): #ir a opciones
                    opciones(contador_soldado_anim)

                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS): #Salir del juego
                    pygame.quit()
                    sys.exit()

                if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):#Pantalla con instrucciones
                    pre_game() 

        pygame.display.update()

#Pantalla de instrucciones
def pre_game():
    pre_game_img = pygame.image.load("Proyecto Unidad 2/imagenes/pre_game_bg.png")
    mixer.music.load("Proyecto Unidad 2/sonidos_musica/pre_game_bgm.mp3")
    mixer.music.play(-1)
    
    while True:
        DISPLAYSURF.blit(pre_game_img,(0,0))
        for event in pygame.event.get():#Comenzar el juego
            if event.type == pygame.MOUSEBUTTONDOWN:
                partida()
        pygame.display.flip()

#Pantalla del juego
def partida():
    pygame.display.set_caption("Partida")
    #Musica de la partida
    mixer.music.load("Proyecto Unidad 2/sonidos_musica/init_game.mp3")
    mixer.music.play(-1)
    
    #Cargar imagenes
    vGlobales.seleccion_terreno = 0
    icono = pygame.image.load("Proyecto Unidad 2/imagenes/tanque.png")
    pygame.display.set_icon(icono)
    fondo = pygame.image.load("Proyecto Unidad 2/imagenes/fondo.png")
    DISPLAYSURF.blit(fondo, (0,0))

    #Skines
    skins_tanque = []
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin1.png"))
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin2.png"))
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin3.png"))
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin4.png"))
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin5.png"))
    skins_tanque.append(pygame.image.load("Proyecto Unidad 2/imagenes/skin6.png"))
    skin1_tanque = pygame.image.load("Proyecto Unidad 2/imagenes/skin1.png")
    skin2_tanque = pygame.image.load("Proyecto Unidad 2/imagenes/skin2.png")
    skin_bala_c = pygame.image.load("Proyecto Unidad 2/imagenes/bala_c_img.png")
    skin_bala_m = pygame.image.load("Proyecto Unidad 2/imagenes/bala_m_img.png")
    skin_bala_g = pygame.image.load("Proyecto Unidad 2/imagenes/bala_g_img.png")
    


    #Test cantidad de tanques
    num_jugadores = 6
    lista_tanques_OG = []
    lista_tanques = []
    lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint(vGlobales.ancho_gris + 10, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + vGlobales.ancho_gris - 100)))
    for i in range (num_jugadores-1):
        lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint((vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + lista_tanques_OG[i].rect.x, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores * (i+2) + vGlobales.ancho_gris - 30)))

    
    #Objetos en pantalla
    sprites = pygame.sprite.Group()
    tanque1 = tanque.Tankes(vGlobales.AZUL,random.randint(vGlobales.ancho_gris + 10,(vGlobales.WIDTH - vGlobales.ancho_gris)/2 + vGlobales.ancho_gris ))
    tanque2 = tanque.Tankes(vGlobales.ROJO,random.randint((vGlobales.WIDTH- vGlobales.ancho_gris)/2 + tanque1.rect.x, vGlobales.WIDTH - 10))    
    lista_tanques = [tanque1, tanque2]
    bala_g = bala.Balas(vGlobales.bala_grande, vGlobales.daño_bala_g, vGlobales.unidades_cyg)
    bala_m = bala.Balas(vGlobales.bala_mediana, vGlobales.daño_bala_m, vGlobales.unidades_m)
    bala_c = bala.Balas(vGlobales.bala_chica, vGlobales.daño_bala_c, vGlobales.unidades_cyg)
    sprites.add(lista_tanques[0]), sprites.add(lista_tanques[1]), sprites.add(lista_tanques_OG[0])
    for i in range (num_jugadores):
        sprites.add(lista_tanques_OG[i])
    sprites.add(bala_g)
    sprites.add(bala_m)
    sprites.add(bala_c)
    recorrido = []

    #Creacion de variables en main
    turno_jugador = 2
    turno_pasado = 0 

    #generacion del terreno
    vGlobales.generar_terreno()
    pantalla_juego = pygame.Surface((vGlobales.WIDTH-vGlobales.ancho_gris,vGlobales.HEIGHT),pygame.SRCALPHA)
    pixel_array = pygame.PixelArray(pantalla_juego)
    pixel_array = genera_terreno_pixel(DISPLAYSURF,pixel_array)
    nueva_superficie = pixel_array.make_surface()

    #Easter egg jiji
    fatality_count = 0
    
    #Variable para generar la nueva partida
    nueva_partida = False

    while True:

        #Dibujo de la pantalla
        DISPLAYSURF.blit(fondo,(0,0))
        
        #Dibuja el terreno
        DISPLAYSURF.blit(nueva_superficie,(vGlobales.ancho_gris,0))
        
        #Interfaz
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(0,0,vGlobales.ancho_gris,vGlobales.HEIGHT))
        interfaz.interfaz()
        
        #proceso de cambio de turno 
        if turno_pasado == 0:
            turno_jugador = random.randint(1,6)
            turno_pasado = 1
            interfaz.text_jugador1 = "Jugador " + str(turno_jugador)
            interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.ROJO)

        #bucle de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:#click mouse
                #bloquea el inventario mientras se ejectua el disparo
                if bala_c.caida == False and bala_m.caida == False and bala_g.caida == False:
                    interfaz.click_mouse_inventario(event.pos)
                #click en "Nueva Partida"
                if interfaz.boton_abrir_minimenu_active == True:
                    if interfaz.boton_nueva_partida_rect.collidepoint(event.pos):
                        nueva_partida = True
                    if interfaz.boton_salir_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                #disparo de bala
                if interfaz.minibox_bala1_active == True and lista_tanques_OG[turno_jugador-1].unidades_c > 0:
                    turno_pasado = disparar_bala(event.pos, bala_c, turno_pasado, turno_jugador, lista_tanques_OG[turno_jugador-1], recorrido)
                if interfaz.minibox_bala2_active == True and lista_tanques_OG[turno_jugador-1].unidades_m > 0:
                    turno_pasado = disparar_bala(event.pos, bala_m, turno_pasado, turno_jugador, lista_tanques_OG[turno_jugador-1], recorrido)
                if interfaz.minibox_bala3_active == True and lista_tanques_OG[turno_jugador-1].unidades_g> 0:
                    turno_pasado = disparar_bala(event.pos, bala_g, turno_pasado, turno_jugador, lista_tanques_OG[turno_jugador-1], recorrido)

            if event.type == pygame.KEYDOWN:
                interfaz.escribir(event)
                
        #Movimiento de tanques
        lista_tanques[0].update()
        lista_tanques[1].update()
        for i in range (num_jugadores):
            lista_tanques_OG[i].update()
        #Evento al seleccionar la municion
        if interfaz.minibox_bala1_active == True:
            nueva_superficie= mostrar_distancias(lista_tanques_OG[turno_jugador-1], lista_tanques[0], bala_c, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores)
            recorrido = calcular_recorrido(bala_c, recorrido)
            DISPLAYSURF.blit(skin_bala_c, (bala_c.rect.x-17,bala_c.rect.y-17))

        if interfaz.minibox_bala2_active == True:
            nueva_superficie=mostrar_distancias(lista_tanques_OG[turno_jugador-1], lista_tanques[0], bala_m, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores)
            recorrido = calcular_recorrido(bala_m, recorrido)
            DISPLAYSURF.blit(skin_bala_m, (bala_m.rect.x-17,bala_m.rect.y-17))
        
        if interfaz.minibox_bala3_active == True:
            nueva_superficie= mostrar_distancias(lista_tanques_OG[turno_jugador-1], lista_tanques[0], bala_g, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores)
            recorrido = calcular_recorrido(bala_g, recorrido)
            DISPLAYSURF.blit(skin_bala_g, (bala_g.rect.x-17,bala_g.rect.y-17))
        
        sprites.draw(DISPLAYSURF)
        mostrar_recorrido(recorrido)

        #Dibujo de skins
        for i in range (num_jugadores):
            if i % 2 == 0:
                DISPLAYSURF.blit(skins_tanque[i], (lista_tanques_OG[i].rect.x-10,lista_tanques_OG[i].rect.y-5))
            else:
                DISPLAYSURF.blit(pygame.transform.flip(skins_tanque[i],True,False), (lista_tanques_OG[i].rect.x-10,lista_tanques_OG[i].rect.y-5))
        DISPLAYSURF.blit(skin1_tanque, (lista_tanques[0].rect.x-10,lista_tanques[0].rect.y-5))
        DISPLAYSURF.blit(skin2_tanque, (lista_tanques[1].rect.x-10,lista_tanques[1].rect.y-5))
        
        #Easter Egg jiji
        if lista_tanques[0].rect.y >= 720:
            fatality_count = fatality(fatality_count)
            
        #Game over
        if (lista_tanques[0].vida <= 0 or lista_tanques[1].vida <= 0):
            while True:
                interfaz.text_game_over = "GAME OVER"
                interfaz.text_surface_game_over = interfaz.vGlobales.font.render(interfaz.text_game_over, True, interfaz.vGlobales.rojo_oscuro)
                interfaz.text_surface_game_over_rect = interfaz.text_surface_game_over.get_rect(center = ((interfaz.vGlobales.WIDTH/2) + 140,(interfaz.vGlobales.HEIGHT/2) - 30))
                interfaz.interfaz()
                if turno_jugador == 1:
                    interfaz.print_interfaz(bala_c.unidades_tanque1,bala_m.unidades_tanque1,bala_g.unidades_tanque1,lista_tanques[0],lista_tanques[1],lista_tanques_OG,num_jugadores)
                else:
                    interfaz.print_interfaz(bala_c.unidades_tanque2,bala_m.unidades_tanque2,bala_g.unidades_tanque2,lista_tanques[0],lista_tanques[1],lista_tanques_OG,num_jugadores)
                interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_game_over, interfaz.text_surface_game_over_rect)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        sys.exit()
                        
        #Inicio de interfaz
        if turno_jugador == 1:
            interfaz.print_interfaz(bala_c.unidades_tanque1,bala_m.unidades_tanque1,bala_g.unidades_tanque1, lista_tanques[0], lista_tanques[1],lista_tanques_OG,num_jugadores)
        else:
            interfaz.print_interfaz(bala_c.unidades_tanque2,bala_m.unidades_tanque2,bala_g.unidades_tanque2, lista_tanques[0], lista_tanques[1],lista_tanques_OG,num_jugadores)
        interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_altura_maxima, interfaz.text_surface_altura_maxima_rect)
        interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_distancia_maxima, interfaz.text_surface_distancia_maxima_rect)

        #Animacion de explosion de las balas
        if bala_c.explosion == 1:
            animacion_explosion(vGlobales.bala_chica, bala_c)
        elif bala_m.explosion == 1:
            animacion_explosion(vGlobales.bala_mediana, bala_m)
        elif bala_g.explosion == 1:
            animacion_explosion(vGlobales.bala_grande,bala_g)
            
        #Creacion de condicional para ver si se debe crear una nueva partida o no
        if nueva_partida == True:
            partida()
        pygame.display.flip()
        RELOJ.tick(vGlobales.FPS)

#EJECUCION
menu_principal()