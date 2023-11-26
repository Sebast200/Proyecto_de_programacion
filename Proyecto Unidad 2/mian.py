import pygame, sys, globales, tanque, bala, random, interfaz,math
from particulas import Particulas
from pygame.locals import *
from boton import Button
from pygame import mixer 

#DECLARACIONES
pygame.init()
interfaz = interfaz.Interfazz()

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
            if (pantalla.get_at((i,j)) == vGlobales.grisclaro):
                matriz[i-vGlobales.ancho_gris][j] = (vGlobales.grisclaro)
            else:
                matriz[i-vGlobales.ancho_gris][j] = (0,0,0,0)
            j+=1
        i+=1

    return matriz

def mostrar_distancias(bala, superfice, pixel_array, lista_tanques, num_jugadores, turno_jugador): 
        superfice = bala.update(superfice, pixel_array, lista_tanques, num_jugadores, turno_jugador)
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

def descuento_balas_tanque(bala,turno_pasado,tanque):
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
def disparar_bala(event, bala, turno_pasado, tanque, recorrido, viento):
    turno_pasado = interfaz.click_mouse(event, bala, tanque, turno_pasado, viento) #Permite pasar al siguiente turno
    descuento_balas_tanque(bala, turno_pasado, tanque)
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

def validar_balas(lista_tanques, num_jugadores):
    #Hay que arreglar esto ya que si un tanque muere CON balas, nunca habra empate
    todos_sin_balas = False
    sin_bala = 0
    for i in range (num_jugadores):
        if lista_tanques[i].unidades_c == 0 and lista_tanques[i].unidades_m == 0 and lista_tanques[i].unidades_g == 0:
            sin_bala += 1
        #Si se hace esto no deberia de ocurrir este error
        elif lista_tanques[i].vida<=0:
            sin_bala += 1
    if sin_bala == num_jugadores:
        todos_sin_balas = True
    else: todos_sin_balas = False
    return todos_sin_balas

def disparo_bot(tanque, turno_pasado, bala_c, bala_m, bala_g, gravedad,viento, recorrido):
    #seleccion de bala
    if turno_pasado == 1:
        balas = [bala_c, bala_m, bala_g]
        condition = True
        if tanque.unidades_c == 0 and tanque.unidades_m == 0 and tanque.unidades_g == 0:
            return 0
        while condition == True:      
            i = random.randint(0,2)
            if i == 0:
                if tanque.unidades_c > 0:
                    interfaz.minibox_bala1_active = True
                    interfaz.minibox_bala2_active = False
                    interfaz.minibox_bala3_active = False
                    interfaz.minibox_bala1_color = vGlobales.ROJO
                    interfaz.minibox_bala2_color = vGlobales.NEGRO
                    interfaz.minibox_bala3_color = vGlobales.NEGRO
                    condition = False
            if i == 1:
                if tanque.unidades_m > 0:
                    interfaz.minibox_bala1_active = False
                    interfaz.minibox_bala2_active = True
                    interfaz.minibox_bala3_active = False
                    interfaz.minibox_bala1_color = vGlobales.NEGRO
                    interfaz.minibox_bala2_color = vGlobales.ROJO
                    interfaz.minibox_bala3_color = vGlobales.NEGRO
                    condition = False
            if i == 2:
                if tanque.unidades_g > 0:
                    interfaz.minibox_bala1_active = False
                    interfaz.minibox_bala2_active = False
                    interfaz.minibox_bala3_active = True
                    interfaz.minibox_bala1_color = vGlobales.NEGRO
                    interfaz.minibox_bala2_color = vGlobales.NEGRO
                    interfaz.minibox_bala3_color = vGlobales.ROJO
                    condition = False
        angulo = random.randint(40,140)
        velocidad = random.randint(50,150)
        balas[i].disparar(angulo, math.pi/180 * (angulo + 90),velocidad,tanque,viento)
        turno_pasado = 0
        Tank_shoot = mixer.Sound("Proyecto Unidad 2/sonidos_musica/tank_shooting.mp3")
        Tank_shoot.play()
        descuento_balas_tanque(balas[i],turno_pasado,tanque)
        if balas[i].caida == False:
            recorrido.clear()
        return turno_pasado

#FUNCIONES PRINCIPALES
#Pantalla de preparacion
def preparacion(num_rondas, num_jugadores, num_bots, contador_soldado_anim):
    #Aqui se dara la opcion a modificar cuantas rondas se quiere jugar asi como cuantos jugadores se quiere que haya en la partida
    pygame.display.set_caption("Preparacion")
    #variable para contar la cantidad de rondas y mostrarlas en la pantalla
    ronda_actual = 1
    gravedad = 5
    viento_active = False
    while True:
        suma_jugadores = num_bots + num_jugadores
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #Creacion de textos
        TEXTO_PREPARACION = vGlobales.font3.render("PREPARACION", True, vGlobales.verde_oscuro)
        PREPARACION_RECT = TEXTO_PREPARACION.get_rect(center=(400, 100))
        TEXTO_CUANTOS_JUGADORES = vGlobales.font2.render("Nro. de jugadores:", True, vGlobales.NEGRO)
        TEXTO_CUANTOS_JUGADORES_RECT = TEXTO_CUANTOS_JUGADORES.get_rect(center=(280,200))
        #Creacion de texto que dira el numero de jugadores
        TEXTO_NUM_JUGADORES = vGlobales.font2.render(str(num_jugadores), True, vGlobales.NEGRO)
        TEXTO_NUM_JUGADORES_RECT = TEXTO_NUM_JUGADORES.get_rect(center=(570,207))
        TEXTO_CUANTOS_BOTS = vGlobales.font2.render("Nro. de bots:", True, vGlobales.NEGRO)
        TEXTO_CUANTOS_BOTS_RECT = TEXTO_CUANTOS_BOTS.get_rect(center=(217,270))
        #Creacion de texto que dira el numero de bots
        TEXTO_NUM_BOTS = vGlobales.font2.render(str(num_bots), True, vGlobales.NEGRO)
        TEXTO_NUM_BOTS_RECT = TEXTO_NUM_BOTS.get_rect(center=(450,277))
        #Creacion de texto que preguntara el numero de rondas
        TEXTO_CUANTAS_RONDAS = vGlobales.font2.render("Nro. de rondas:", True, vGlobales.NEGRO)
        TEXTO_CUANTAS_RONDAS_RECT = TEXTO_CUANTAS_RONDAS.get_rect(center=(247,340))
        #Creacion de texto que dira el numero de rondas
        TEXTO_NUM_RONDAS = vGlobales.font2.render(str(num_rondas), True, vGlobales.NEGRO)
        TEXTO_NUM_RONDAS_RECT = TEXTO_NUM_JUGADORES.get_rect(center=(505,345))
        #Creacion de texto que dira Gravedad
        TEXTO_GRAVEDAD = vGlobales.font2.render("Gravedad:",True, vGlobales.NEGRO)
        TEXTO_GRAVEDAD_RECT = TEXTO_GRAVEDAD.get_rect(center=(185,410))
        #Creacion de texto que dira el numero de la gravedad
        TEXTO_NUM_GRAVEDAD = vGlobales.font2.render(str(gravedad), True, vGlobales.NEGRO)
        TEXTO_NUM_GRAVEDAD_RECT = TEXTO_NUM_GRAVEDAD.get_rect(center=(400,415))
        #Creacion de texto que dira Viento
        TEXTO_VIENTO = vGlobales.font2.render("Viento:",True, vGlobales.NEGRO)
        TEXTO_VIENTO_RECT = TEXTO_VIENTO.get_rect(center=(149,480))
        #Creacion de botones
        #Boton para volver
        BOTON_VOLVER = Button(image=None, pos=(240,650), text_input="VOLVER", font=get_font(75), base_color=vGlobales.verde_oscuro, hovering_color=vGlobales.BLANCO)
        #Boton para jugar
        BOTON_JUGAR = Button(image=None, pos=(1040,650), text_input="JUGAR", font=get_font(75), base_color=vGlobales.verde_oscuro, hovering_color=vGlobales.BLANCO)
        #Boton para restar en num_jugadores
        BOTON_MENOS1 = Button(image=None,pos=(520,207), text_input="-", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para sumar en num_jugadores
        BOTON_MAS1 = Button(image=None,pos=(620,207), text_input="+", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para restar en num_bots
        BOTON_MENOS4 = Button(image=None,pos=(400,277), text_input="-", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para sumar en num_bots
        BOTON_MAS4 = Button(image=None,pos=(500,277), text_input="+", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para restar en rondas
        BOTON_MENOS2 = Button(image=None,pos=(455,345), text_input="-", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para sumar en rondas
        BOTON_MAS2 = Button(image=None,pos=(585,345), text_input="+", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para restar gravedad
        BOTON_MENOS3 = Button(image=None,pos=(335,415), text_input="-", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para sumar gravedad
        BOTON_MAS3 = Button(image=None,pos=(465,415), text_input="+", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para activar viento
        BOTON_ACTIVAR_VIENTO = Button(image=None,pos=(265,485), text_input="Si", font=vGlobales.font2, base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        #Boton para desactivar viento
        BOTON_DESACTIVAR_VIENTO = Button(image=None,pos=(340,485), text_input="No", font=vGlobales.font2, base_color=vGlobales.NEGRO, hovering_color=vGlobales.gris)
        
        contador_soldado_anim = soldado_durmiendo_anim(contador_soldado_anim,850,430)
        #IMPRESION DE RECTANGULOS PARA BOTONES
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(495,175,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(545,175,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(595,175,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(375,245,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(425,245,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(475,245,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(430,315,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(480,315,80,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(560,315,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(310,385,50,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(360,385,80,50))
        pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(440,385,50,50))
        
        if viento_active == False:
            pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(235,455,70,60))
            pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(305,455,70,60))
        else:
            pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(235,455,70,60))
            pygame.draw.rect(DISPLAYSURF,vGlobales.gris_oscuro,(305,455,70,60))

        #IMPRESION DE TEXTOS
        DISPLAYSURF.blit(TEXTO_PREPARACION, PREPARACION_RECT)
        DISPLAYSURF.blit(TEXTO_CUANTOS_JUGADORES, TEXTO_CUANTOS_JUGADORES_RECT)
        DISPLAYSURF.blit(TEXTO_NUM_JUGADORES, TEXTO_NUM_JUGADORES_RECT)
        DISPLAYSURF.blit(TEXTO_CUANTOS_BOTS, TEXTO_CUANTOS_BOTS_RECT)
        DISPLAYSURF.blit(TEXTO_NUM_BOTS, TEXTO_NUM_BOTS_RECT)
        DISPLAYSURF.blit(TEXTO_CUANTAS_RONDAS, TEXTO_CUANTAS_RONDAS_RECT)
        DISPLAYSURF.blit(TEXTO_NUM_RONDAS, TEXTO_NUM_RONDAS_RECT)
        DISPLAYSURF.blit(TEXTO_GRAVEDAD, TEXTO_GRAVEDAD_RECT)
        DISPLAYSURF.blit(TEXTO_NUM_GRAVEDAD, TEXTO_NUM_GRAVEDAD_RECT)
        DISPLAYSURF.blit(TEXTO_VIENTO, TEXTO_VIENTO_RECT)
        
        for boton in [BOTON_VOLVER, BOTON_JUGAR, BOTON_MENOS1, BOTON_MAS1, BOTON_MAS2, BOTON_MENOS2, BOTON_MENOS3, BOTON_MAS3, BOTON_MENOS4, BOTON_MAS4, BOTON_ACTIVAR_VIENTO, BOTON_DESACTIVAR_VIENTO]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN: #Volver al menu principal
                print(suma_jugadores)
                if BOTON_VOLVER.checkForInput(MENU_MOUSE_POS):
                    menu_principal()
                if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                    print(suma_jugadores)
                    pre_game(num_rondas,num_jugadores, ronda_actual, gravedad+5, num_bots,viento_active)
                #Creacion de condicionales para los botones de suma y resta de numero de jugadores
                if BOTON_MENOS1.checkForInput(MENU_MOUSE_POS):
                    if num_jugadores > 0 and suma_jugadores > 2:
                        num_jugadores -= 1
                        print(suma_jugadores)
                if BOTON_MAS1.checkForInput(MENU_MOUSE_POS):
                    if num_jugadores < 6 and suma_jugadores < 6:
                        num_jugadores += 1
                        print(suma_jugadores)
                #Creacion de condicionales para los botones de suma y resta de numero de bots
                if BOTON_MENOS4.checkForInput(MENU_MOUSE_POS):
                    if num_bots > 0 and suma_jugadores > 2:
                        num_bots -=1
                        print(suma_jugadores)
                if BOTON_MAS4.checkForInput(MENU_MOUSE_POS):
                    if num_bots < 6 and suma_jugadores < 6:
                        num_bots += 1
                        print(suma_jugadores)
                #Creacion de condicionales para los botones de suma y resta de numero de rondas
                if BOTON_MENOS2.checkForInput(MENU_MOUSE_POS):
                    if num_rondas > 1:
                        num_rondas -= 1
                if BOTON_MAS2.checkForInput(MENU_MOUSE_POS):
                    if num_rondas < 20  :
                        num_rondas += 1
                #Creacion de botones para aumentar y disminuir la gravedad
                if BOTON_MENOS3.checkForInput(MENU_MOUSE_POS):
                    if gravedad > 1:
                        gravedad -= 1
                if BOTON_MAS3.checkForInput(MENU_MOUSE_POS):
                    if gravedad < 10:
                        gravedad += 1
                #Creacion de condicionales para los botones para activar o desactivar viento
                if BOTON_ACTIVAR_VIENTO.checkForInput(MENU_MOUSE_POS):
                    viento_active = True
                if BOTON_DESACTIVAR_VIENTO.checkForInput(MENU_MOUSE_POS):
                    viento_active = False

        pygame.display.update()

#Pantalla de opciones
def opciones(contador_soldado_anim):
    pygame.display.set_caption("Opciones")
    while True:
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        TEXTO_OPCIONES = vGlobales.font3.render("OPCIONES", True, vGlobales.NEGRO)
        TEXTO_DESCRIPCION = vGlobales.font2.render("De momento no tenemos las opciones listas xd", True, vGlobales.NEGRO)
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
    #MUSICA DE FONDO
    mixer.music.load("Proyecto Unidad 2/sonidos_musica/background.mp3")
    #mixer.music.play(-1)
    contador_soldado_anim = 0
    num_rondas = 2
    num_jugadores = 2
    num_bots = 1
    pygame.display.set_caption("Menu")
    while True:
        DISPLAYSURF.blit(IMAGEN_DE_FONDO,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        TEXTO_MENU = vGlobales.font3.render("TANK LOVER'S GAME", True, vGlobales.verde_oscuro)
        MENU_RECT = TEXTO_MENU.get_rect(center=(640, 100))
        contador_soldado_anim = soldado_durmiendo_anim(contador_soldado_anim,850,430)
        #Creacion de botones
        BOTON_JUGAR = Button(image=None, pos=(400,290), text_input="JUGAR", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.BLANCO)
        BOTON_OPCIONES = Button(image=None, pos=(400,415),text_input="OPCIONES", font=get_font(75), base_color=vGlobales.NEGRO, hovering_color=vGlobales.BLANCO)
        BOTON_SALIR = Button(image= None, pos=(400,540),text_input="SALIR", font=get_font(75), base_color=vGlobales.NEGRO,hovering_color=vGlobales.BLANCO)

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
                    preparacion(num_rondas,num_jugadores,num_bots,contador_soldado_anim)
                    # pre_game(num_rondas, num_jugadores) 

        pygame.display.update()

#Pantalla de instrucciones
def pre_game(num_rondas, num_personas, ronda_actual, gravedad, num_bots, viento_active):
    pre_game_img = pygame.image.load("Proyecto Unidad 2/imagenes/pre_game_bg.png")
    mixer.music.load("Proyecto Unidad 2/sonidos_musica/pre_game_bgm.mp3")
    #mixer.music.play(-1)
    num_jugadores = num_personas + num_bots
    print("num_jugadores = ",num_jugadores)
    lista_tanques_OG = []
    if num_personas == 0: 
        lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint(vGlobales.ancho_gris + 10, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + vGlobales.ancho_gris - 100), gravedad, True))
        lista_tanques_OG[0].id = 1
    else: 
        lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint(vGlobales.ancho_gris + 10, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + vGlobales.ancho_gris - 100), gravedad, False))
        lista_tanques_OG[0].id = 1
    for i in range (num_jugadores-1):
        if i < num_bots:
            lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint((vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + lista_tanques_OG[i].rect.x, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores * (i+2) + vGlobales.ancho_gris - 30), gravedad, True))
            lista_tanques_OG[i+1].id = i+2
        else:
            lista_tanques_OG.append(tanque.Tankes(vGlobales.gris,random.randint((vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + lista_tanques_OG[i].rect.x, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores * (i+2) + vGlobales.ancho_gris - 30), gravedad, False))
            lista_tanques_OG[i+1].id = i+2
    print("Cantidad de Jugadores: ",len(lista_tanques_OG))
    while True:
        DISPLAYSURF.blit(pre_game_img,(0,0))
        for event in pygame.event.get():#Comenzar el juego
            if event.type == pygame.MOUSEBUTTONDOWN:
                partida(num_rondas, num_jugadores, ronda_actual, lista_tanques_OG, viento_active, gravedad)
        pygame.display.flip()

#Pantalla del juego
def partida(num_rondas, num_jugadores, ronda_actual, lista_tanques_OG, viento_active, gravedad):
    if num_rondas > 0:
        #RECOLECCION E IMPRESION DE RONDA
        DISPLAYSURF.fill((0,0,0), (0,0,vGlobales.WIDTH,vGlobales.HEIGHT))
        text_ronda = vGlobales.font3.render("Ronda n°" + str(ronda_actual), True, vGlobales.BLANCO)
        text_ronda_rect = text_ronda.get_rect(center=(vGlobales.WIDTH/2, vGlobales.HEIGHT/2))
        DISPLAYSURF.blit(text_ronda, text_ronda_rect)
        pygame.display.flip()
        pygame.time.delay(600)
        print("Ronda n° ",num_rondas)
        pygame.display.set_caption("Partida")
        #Musica de la partida
        mixer.music.load("Proyecto Unidad 2/sonidos_musica/init_game.mp3")
        #mixer.music.play(-1)

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
        skin_bala_c = pygame.image.load("Proyecto Unidad 2/imagenes/bala_c_img.png")
        skin_bala_m = pygame.image.load("Proyecto Unidad 2/imagenes/bala_m_img.png")
        skin_bala_g = pygame.image.load("Proyecto Unidad 2/imagenes/bala_g_img.png")

        #Objetos en pantalla
        sprites = pygame.sprite.Group()
        bala_g = bala.Balas(vGlobales.bala_grande, vGlobales.daño_bala_g, gravedad)
        bala_m = bala.Balas(vGlobales.bala_mediana, vGlobales.daño_bala_m, gravedad)
        bala_c = bala.Balas(vGlobales.bala_chica, vGlobales.daño_bala_c, gravedad)
        for i in range (num_jugadores-1):
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

        #Variable para verificar si se le hizo click a pasar turno al final del codigo (si se verifica antes no funciona asi que por ahora se hara de este modo que es un poco feo :c )
        pasar_turno = False
        #Arreglo de turnos por ronda
        ronda = []
        viento = -1
        jugadores_muertos = num_jugadores

        #Variable que controla las particulas
        particula = Particulas()
        
        #Variable booleana que define si los jugadores tienen balas o no
        todos_sin_balas = False
        
        #Variable booleana que definira si se debe mostrar la tienda o no
        compraron_todos = False

        #Variable timer del bot
        timer_disparo_bot = 0

        tanques_suelo = False
        
        turno_anterior = 0
        while True:
            #Dibujo de la pantalla
            DISPLAYSURF.blit(fondo,(0,0))

            #Particulas
            particula.update(viento)
            for particulas in particula.particulas:
                pygame.draw.circle(DISPLAYSURF, vGlobales.BLANCO, (int(particulas['x']), int(particulas['y'])), 2)
            
            #Dibuja el terreno
            DISPLAYSURF.blit(nueva_superficie,(vGlobales.ancho_gris,0))
            
            #Interfaz
            pygame.draw.rect(DISPLAYSURF,vGlobales.grisclaro,(0,0,vGlobales.ancho_gris,vGlobales.HEIGHT))
            interfaz.interfaz()

            #proceso de cambio de turno
            tanques_suelo = False
            for i in range (num_jugadores):
                lista_tanques_OG[i].update()
                if lista_tanques_OG[i].caida == True:
                    tanques_suelo = True
            if turno_pasado == 0 and not bala_c.caida and not bala_m.caida and not bala_g.caida and not tanques_suelo:
                turno_anterior = turno_jugador
                if viento_active == True:
                    viento = random.randint(-10,10)/10
                else:
                    viento = 0
                jugadores_muertos = num_jugadores
                for i in range (len(lista_tanques_OG)):
                    if lista_tanques_OG[i].vida >= 0:
                        jugadores_muertos -= 1
                print(jugadores_muertos)
                if len(ronda) >= num_jugadores - jugadores_muertos:
                    ronda = []
                turno_jugador = random.randint(1,num_jugadores)
                condition = True
                while condition:
                    print("condicion")
                    if lista_tanques_OG[turno_jugador-1].vida <= 0:
                        turno_jugador = random.randint(1,num_jugadores)
                        print("vivo")
                    else:
                        condition = False
                while turno_jugador in ronda:
                    turno_jugador = random.randint(1,num_jugadores)
                    print("vivo2")
                ronda.append(turno_jugador)
                turno_pasado = 1
                interfaz.text_jugador1 = "Jugador " + str(turno_jugador)
                print("Jugador ", turno_jugador,"Es Bot?: ",lista_tanques_OG[turno_jugador-1].bot)
                if turno_jugador == 1:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.AZUL)
                if turno_jugador == 2:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.ROJO)
                if turno_jugador == 3:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.amarillo)
                if turno_jugador == 4:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.celeste)
                if turno_jugador == 5:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.morado)
                if turno_jugador == 6:
                    interfaz.text_surface_jugador1 = interfaz.vGlobales.font.render(interfaz.text_jugador1, True, interfaz.vGlobales.naranjo)
                disparo_unico_bot = True
            
            
            #Proceso nuevo de kills 
            for i in range (len(lista_tanques_OG)):
                if lista_tanques_OG[i].vida <= 0 and lista_tanques_OG[i].vivo == True: 
                    lista_tanques_OG[i].vivo = False
                    print(lista_tanques_OG[i].id)
                    print(turno_anterior)
                    print("Muerte")
                    if turno_anterior == lista_tanques_OG[i].id:
                        lista_tanques_OG[i].cantidad_suicidios += 1
                        print("entro suicidio")
                    else:
                        lista_tanques_OG[turno_anterior-1].kills+=1
                        print("entro kill")
            
            #Saltar el turno de los jugadores muertos
            if lista_tanques_OG[turno_jugador-1].vida <= 0:
                pasar_turno = True
            
            #Saltar el turno de los jugadores sin balas
            if lista_tanques_OG[turno_jugador-1].unidades_c == 0 and lista_tanques_OG[turno_jugador-1].unidades_m == 0 and lista_tanques_OG[turno_jugador-1].unidades_g == 0:
                pasar_turno = True

            #Muerte por caida
            for i in range (num_jugadores):
                if lista_tanques_OG[i].vida <= lista_tanques_OG[i].distancia_caida*gravedad/10 and not lista_tanques_OG[i].muerte_caida:
                    if lista_tanques_OG[i] == lista_tanques_OG[turno_anterior-1] and lista_tanques_OG[i].suicidio == False:
                        lista_tanques_OG[i].suicidio = True
                    elif lista_tanques_OG[i].muerte_caida == False:
                        lista_tanques_OG[turno_anterior-1].kills +=1
                        lista_tanques_OG[i].muerte_caida = True
                    #jugadores_muertos += 1 
            
            #bucle de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:#click mouse
                    #bloquea el inventario mientras se ejectua el disparo
                    if bala_c.caida == False and bala_m.caida == False and bala_g.caida == False:
                        interfaz.click_mouse_inventario(event.pos)
                    #click en "Pasar Turno"
                    if interfaz.boton_abrir_minimenu_active == True:
                        if interfaz.boton_pasar_turno_rect.collidepoint(event.pos):
                            pasar_turno = True
                            # nueva_partida = True
                        if interfaz.boton_salir_rect.collidepoint(event.pos):
                            menu_principal()
                    #disparo de bala
                    #if interfaz.minibox_bala1_active == True and lista_tanques_OG[turno_jugador-1].unidades_c > 0 and lista_tanques_OG[turno_jugador-1].vida > 0
                    if interfaz.minibox_bala1_active == True and lista_tanques_OG[turno_jugador-1].bot == False:
                        turno_pasado = disparar_bala(event.pos, bala_c, turno_pasado, lista_tanques_OG[turno_jugador-1], recorrido, viento)
                    if interfaz.minibox_bala2_active == True and lista_tanques_OG[turno_jugador-1].bot == False:
                        turno_pasado = disparar_bala(event.pos, bala_m, turno_pasado, lista_tanques_OG[turno_jugador-1], recorrido, viento)
                    if interfaz.minibox_bala3_active == True and lista_tanques_OG[turno_jugador-1].bot == False:
                        turno_pasado = disparar_bala(event.pos, bala_g, turno_pasado, lista_tanques_OG[turno_jugador-1], recorrido, viento)

                if event.type == pygame.KEYDOWN:
                    interfaz.escribir(event)

            
            
            #Evento al seleccionar la municion
            if interfaz.minibox_bala1_active == True:
                nueva_superficie= mostrar_distancias(bala_c, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores, turno_jugador-1)
                recorrido = calcular_recorrido(bala_c, recorrido)
                DISPLAYSURF.blit(skin_bala_c, (bala_c.rect.x-17,bala_c.rect.y-17))
            if interfaz.minibox_bala2_active == True:
                nueva_superficie=mostrar_distancias(bala_m, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores, turno_jugador-1)
                recorrido = calcular_recorrido(bala_m, recorrido)
                DISPLAYSURF.blit(skin_bala_m, (bala_m.rect.x-17,bala_m.rect.y-17))
            if interfaz.minibox_bala3_active == True:
                nueva_superficie= mostrar_distancias(bala_g, nueva_superficie, pixel_array, lista_tanques_OG, num_jugadores, turno_jugador-1)
                recorrido = calcular_recorrido(bala_g, recorrido)
                DISPLAYSURF.blit(skin_bala_g, (bala_g.rect.x-17,bala_g.rect.y-17))
            sprites.draw(DISPLAYSURF)
            mostrar_recorrido(recorrido)

            #Movimiento de tanques
            '''for i in range (num_jugadores):
                lista_tanques_OG[i].update()'''
            
            #Dibujo de skins
            for i in range (num_jugadores):
                if i % 2 == 0:
                    DISPLAYSURF.blit(skins_tanque[i], (lista_tanques_OG[i].rect.x-10,lista_tanques_OG[i].rect.y-5))
                else:
                    DISPLAYSURF.blit(pygame.transform.flip(skins_tanque[i],True,False), (lista_tanques_OG[i].rect.x-10,lista_tanques_OG[i].rect.y-5))
            
            #Easter Egg jiji
            for i in range (num_jugadores):
                if lista_tanques_OG[i].rect.y >= 720:
                    fatality_count = fatality(fatality_count)
            
            #Inicio de interfaz
            i = 0
            while i<len(lista_tanques_OG):
                if i==turno_jugador-1:
                    interfaz.print_interfaz(lista_tanques_OG[i].unidades_c,lista_tanques_OG[i].unidades_m,lista_tanques_OG[i].unidades_g,lista_tanques_OG,num_jugadores)
                i+=1
            #Proceso de impresion de tienda
            while compraron_todos == False:
                compraron_todos = interfaz.print_tienda(lista_tanques_OG,compraron_todos,num_jugadores,bala_c,bala_m,bala_g)
            #undo
            interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_altura_maxima, interfaz.text_surface_altura_maxima_rect)
            interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_distancia_maxima, interfaz.text_surface_distancia_maxima_rect)
            
            # de explosion de las balas
            if bala_c.explosion == 1:
                animacion_explosion(vGlobales.bala_chica, bala_c)
            elif bala_m.explosion == 1:
                animacion_explosion(vGlobales.bala_mediana, bala_m)
            elif bala_g.explosion == 1:
                animacion_explosion(vGlobales.bala_grande,bala_g)
            #Validacion cantidad de balas de cada jugador
            if bala_c.caida == False and bala_m.caida == False and bala_g.caida == False:
                todos_sin_balas = validar_balas(lista_tanques_OG, num_jugadores)
            #Creacion de condicional para ver si se debe crear una nueva parAnimaciontida o no
            if nueva_partida == True:
                partida(num_rondas, num_jugadores, ronda_actual, lista_tanques_OG)
            #Creacion de condicional para ver si se debe pasar el turno o no
            if pasar_turno == True:
                turno_pasado = 0
                pasar_turno = False
            pygame.display.flip()

                #Disparo jugadores bot
            if lista_tanques_OG[turno_jugador-1].bot == True and lista_tanques_OG[turno_jugador-1].caida == False and turno_pasado == 1:
                #disparo_bot(lista_tanques_OG[turno_jugador-1],turno_pasado,bala_c,bala_m,bala_g,gravedad,viento,recorrido)
                timer_disparo_bot +=1
                if disparo_unico_bot == True and timer_disparo_bot == 75:
                    recorrido = []
                    turno_pasado = disparo_bot(lista_tanques_OG[turno_jugador-1],turno_pasado,bala_c,bala_m,bala_g,gravedad,viento,recorrido)
                    disparo_unico_bot = False
                    timer_disparo_bot = 0


            #Game over o Empate
            if (jugadores_muertos+1) == num_jugadores or todos_sin_balas == True:
                num_rondas = num_rondas - 1
                ronda_actual += 1
                print("rondas restantes: ", num_rondas)
                for i in range(num_jugadores):
                    lista_tanques_OG[i].saldo = lista_tanques_OG[i].saldo + 10000
                    if lista_tanques_OG[i].kills > 0:
                        lista_tanques_OG[i].saldo = lista_tanques_OG[i].saldo + (5000 * lista_tanques_OG[i].kills)
                        lista_tanques_OG[i].total_kills += lista_tanques_OG[i].kills
                        lista_tanques_OG[i].kills = 0
                        print("Saldo Jugador ", i+1," = ",lista_tanques_OG[i].saldo)

                    if lista_tanques_OG[i].suicidio == True: 
                        lista_tanques_OG[i].saldo = lista_tanques_OG[i].saldo - 5000
                        lista_tanques_OG[i].cantidad_suicidios =+ 1
                        lista_tanques_OG[i].suicidio = False

                    if lista_tanques_OG[i].saldo < 0:
                        lista_tanques_OG[i].saldo = 0
                while True:
                    #La idea es que se actualicen los datos de los tanques antes de mostrar la pantalla de resultados. voy a hacer unos cambios
                    '''
                    interfaz.text_game_over = "GAME OVER"
                    interfaz.text_surface_game_over = interfaz.vGlobales.font.render(interfaz.text_game_over, True, interfaz.vGlobales.verde_oscuro)
                    interfaz.text_surface_game_over_rect = interfaz.text_surface_game_over.get_rect(center = ((interfaz.vGlobales.WIDTH/2) + 140,(interfaz.vGlobales.HEIGHT/2) - 30))
                    interfaz.interfaz()
                    interfaz.vGlobales.PANTALLA.blit(interfaz.text_surface_game_printover, interfaz.text_surface_game_over_rect)
                    '''
                    interfaz.print_resultados(lista_tanques_OG,i,num_jugadores)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if num_rondas > 0:
                                lista_tanques_OG[0].rect.center=(random.randint(vGlobales.ancho_gris + 10, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + vGlobales.ancho_gris - 100), 100)
                                for i in range(num_jugadores-1): 
                                    lista_tanques_OG[i+1].rect.center=(random.randint((vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores + lista_tanques_OG[i].rect.x, (vGlobales.WIDTH-vGlobales.ancho_gris)/num_jugadores * (i+2) + vGlobales.ancho_gris - 30), 100)
                                for i in range(num_jugadores):
                                    #lista_tanques_OG[i].kills = 0
                                    lista_tanques_OG[i].suicidio = False
                                    lista_tanques_OG[i].vida = 100
                                    lista_tanques_OG[i].inmune = True
                                partida(num_rondas, num_jugadores, ronda_actual, lista_tanques_OG, viento, gravedad)
                                print("otra ronda")
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if num_rondas == 0:
                                menu_principal()
                                print("partida finalizada")
            RELOJ.tick(vGlobales.FPS)
    else:
        menu_principal()

#EJECUCION
menu_principal()

#NUEVOS CAMBIOS (FRANCO ARENAS) 29-10-2023
#1.- SE AGREGARON LOS COLORES EN GLOBALES Y EN MIAN
#2.- linea 308 se cambio el sistema de turno y ahora es funcional (creo)
#NUEVOS CAMBIOS (FRANCO ARENAS) 14-11-2023
#1.- Linea 505 a 510 se cambiaron las condicionales que estaban antes, ya que estas a pesar de que funcionaban, a la hora de que se acabara la municion de la bala anteriormente seleccionada habia que elegir SI O SI otra con municion, de otra forma el jugador no va a poder hacer nada