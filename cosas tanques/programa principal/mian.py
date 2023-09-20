import math, pygame, sys, globales, tanque, bala, random
from pygame.locals import *

#DECLARACIONES
pygame.init()
#variables globales
vGlobales = globales.Globaless()
RELOJ = pygame.time.Clock()
#pantalla
DISPLAYSURF = vGlobales.PANTALLA 
pygame.display.set_caption("Tanque Volador")
print("a")
#icono
icono = pygame.image.load("cosas tanques/programa principal/imagenes/tanque.png")
pygame.display.set_icon(icono)
#fondo
fondo = pygame.image.load("cosas tanques/programa principal/imagenes/fondo.png")
DISPLAYSURF.blit(fondo, (0,0))

#jugador 1
skin1 = pygame.image.load("cosas tanques/programa principal/imagenes/skin1.png")
rect1 = skin1.get_rect()
skin2 = pygame.image.load("cosas tanques/programa principal/imagenes/skin2.png")
#objetos en pantalla
sprites = pygame.sprite.Group()
tanque1 = tanque.Tankes(vGlobales.ROJO,300)
tanque2 = tanque.Tankes(vGlobales.AZUL,400)
bala1 = bala.Balas()
sprites.add(tanque1)
sprites.add(tanque2)
sprites.add(bala1)


#CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
textbox_angulo = ""
#Rectangulo de la caja de texto
textbox_angulo_rect = pygame.Rect(150,180,80,40)
#Esta variable cambiara de false a true una vez que el jugador le haga click al rectangulo para escribir
textbox_angulo_active = False

textbox_velocidad_inicial = ""
#Rectangulo de la caja de texto
textbox_velocidad_inicial_rect = pygame.Rect(150,355,80,40)
#Esta variable cambiara de false a true una vez que el jugador le haga click al rectangulo para escribir
textbox_velocidad_inicial_active = False
#FIN DE CREACION DE VARIABLES PARA LAS CAJAS DE TEXTO
#Ahora que lo pienso, quizas tambien tenga que crear en el main el rectangulo que va a decir disparar, ya que asi puedo colocar las condiciones aqui de una forma mas sencilla
#Voy a probar a crear el rectangulo aqui, ya que la idea es que el usuario pueda hacerle click al rectangulo en vez de apretar enter
text_boton_jugador = "Dispara"
text_boton_jugador_rect = pygame.Rect(20,600,220,80)
text_boton_jugador_color = vGlobales.verde
#Voy a crear 

while True:
    #pygame.display - posibilidad de no ser necesario

    #bucle para cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Creacion de condiciones para la caja de texto y boton
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Condicion de click para el cuadro de angulo
            if textbox_angulo_rect.collidepoint(event.pos):
                print("Click")
                textbox_angulo_active = True
            else:
                textbox_angulo_active = False
            #Condicion de click para el cuadro de velocidad inicial
            if textbox_velocidad_inicial_rect.collidepoint(event.pos):
                print("Click2")
                textbox_velocidad_inicial_active = True
            else:
                textbox_velocidad_inicial_active = False
            #Condicion de click para el cuadro de boton de disparo
            if text_boton_jugador_rect.collidepoint(event.pos):
                print("Click3")
                print("Comprobacion de que los datos puestos sean validos y esten listos para el disparo")
                try:
                    numero_angulo = int(textbox_angulo)
                    numero_velocidad_inicial = int(textbox_velocidad_inicial)
                    #Por ahora la unica condicion sera que el numero del angulo no supere los 360 grados
                    if numero_angulo>360:
                        print("El numero del angulo supera los limites :(")
                        textbox_angulo = ""
                    else:
                        print("Los numeros ingresados son validos :3")
                        print("el numero de angulo es: ", numero_angulo)
                        print("el numero de velocidad inicial es: ", numero_velocidad_inicial)
                        #Voy a colocar por ahora aqui el metodo disparo para simular que el boton cause el disparo y que por ende tambien cambie de color
                        bala1.disparar(math.pi/180 * (numero_angulo + 90), numero_velocidad_inicial,tanque1.rect.midtop)
                        text_boton_jugador = "Recarga"
                        text_boton_jugador_color = vGlobales.ROJO
                        pygame.draw.rect(DISPLAYSURF,text_boton_jugador_color,text_boton_jugador_rect)
                        text_boton_jugador_surface = vGlobales.font.render(text_boton_jugador,True,vGlobales.BLANCO)

                except ValueError:
                    print("Hay algo mal aqui")
                    textbox_angulo = ""
                    textbox_velocidad_inicial = ""

        if event.type == pygame.KEYDOWN:
            #Seccion de codigo de caja de texto de angulo
            if textbox_angulo_active == True:
                if event.key == pygame.K_BACKSPACE:
                    textbox_angulo = textbox_angulo[:-1]
                if event.key == pygame.K_RETURN:
                    #Verificacion de que el numero puesto sea valido y todo eso
                    try:
                        numero_angulo = int(textbox_angulo)
                        print("Numero ingresado: ",textbox_angulo)
                        if numero_angulo>360 or numero_angulo<0:
                            print("El numero ingresado supera los limites")
                            textbox_angulo = ""
                        else:
                            print("El numero es valido y no supera los limites :)")
                    except ValueError:
                        print("No es un numero valido")
                        textbox_angulo = ""
                if event.unicode.isnumeric():
                    #Voy a ver si hay una forma de limitar a que solo hayan tres numeros ingresados
                    if len(textbox_angulo)<3:
                        textbox_angulo += event.unicode
                    print(event.unicode)
            #Seccion de codigo de caja de texto de velocidad inicial
            if textbox_velocidad_inicial_active == True:
                if event.key == pygame.K_BACKSPACE:
                    textbox_velocidad_inicial = textbox_velocidad_inicial[:-1]
                if event.key == pygame.K_RETURN:
                    #Verificacion de que el numero puesto sea valido y todo eso
                    try:
                        numero_velocidad_inicial = int(textbox_velocidad_inicial)
                        print("Numero ingresado: ",textbox_velocidad_inicial)
                        if numero_velocidad_inicial>999:
                            print("El numero ingresado supera los limites")
                            textbox_velocidad_inicial = ""
                        else:
                            print("El numero es valido y no supera los limites :)")
                    except ValueError:
                        print("No es un numero valido")
                        textbox_velocidad_inicial = ""
                if event.unicode.isnumeric():
                    if len(textbox_velocidad_inicial)<3:
                        textbox_velocidad_inicial += event.unicode
                    print(event.unicode)
    #pygame.display.update() - posibilidad de no ser necesario
    

    #dibujo de la pantalla
    DISPLAYSURF.blit(fondo,(0,0))
    vGlobales.terreno()
    #Aqui se dibuja la interfaz despues de que se dibuje el terreno
    vGlobales.interfaz()
   
    #SPRITES
    sprites.update()
    #bala1.colision_Tanke((tanque1, tanque2))
    sprites.draw(DISPLAYSURF)

    #Skins
    DISPLAYSURF.blit(skin1, (tanque1.rect.x-15,tanque1.rect.y-15))
    if tanque2.rect.x + tanque2.largo > bala1.rect.x and \
       tanque2.rect.x < bala1.rect.x + 5 and \
       tanque2.rect.y + tanque2.alto > bala1.rect.y and \
       tanque2.rect.y < bala1.rect.y + 5:
        print("toco tanque")
        bala1.caida = False
    DISPLAYSURF.blit(skin2, (tanque2.rect.x-25,tanque2.rect.y-15))

    '''
    if event.type == pygame.MOUSEBUTTONUP:
        bala1.disparar(math.pi/180 * 130, 70,tanque1.rect.midtop)
    '''
    
    
    #AQUI SE DIBUJARA Y SE ACTUALIZARA LAS CAJAS DE TEXTO Y EL BOTON DE DISPARO
    pygame.draw.rect(DISPLAYSURF,vGlobales.gris,textbox_angulo_rect)
    textbox_angulo_surface = vGlobales.font.render(textbox_angulo,True,vGlobales.NEGRO)

    pygame.draw.rect(DISPLAYSURF,vGlobales.gris,textbox_velocidad_inicial_rect)
    textbox_velocidad_inicial_surface = vGlobales.font.render(textbox_velocidad_inicial,True,vGlobales.NEGRO)

    pygame.draw.rect(DISPLAYSURF,text_boton_jugador_color,text_boton_jugador_rect)
    text_boton_jugador_surface = vGlobales.font.render(text_boton_jugador,True,vGlobales.NEGRO)

    DISPLAYSURF.blit(textbox_angulo_surface,(textbox_angulo_rect.x + 15, textbox_angulo_rect.y + 10))
    DISPLAYSURF.blit(textbox_velocidad_inicial_surface,(textbox_velocidad_inicial_rect.x + 15, textbox_velocidad_inicial_rect.y + 10))
    DISPLAYSURF.blit(text_boton_jugador_surface,(text_boton_jugador_rect.x + 65, text_boton_jugador_rect.y + 25))

    pygame.display.flip()
    #FIN DE CAMBIOS
    RELOJ.tick(vGlobales.FPS)
