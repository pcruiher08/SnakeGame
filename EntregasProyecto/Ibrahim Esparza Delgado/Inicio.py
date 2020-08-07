#Hacer una ventana 

import pygame
import random

Puntos = 0

ScreenSize = 500
Running = True
cabezax = round(random.randrange(0, ScreenSize - 10) / 10) * 10
cabezay = round(random.randrange(0, ScreenSize - 10) / 10) * 10
anchoDePixel = 10
altoDePixel = 10
velocidad = 10
direccion = ""

#Comida de la serpiente 
comidaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
comidaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10

vesente = [ (cabezax, cabezay) ]

# Que la serpeinte se mueva sola 
def moverSerpiente(direccion, serpeinte):

    nuevaCabezaX = serpeinte [0] [0]
    nuevaCabezaY = serpeinte [0] [1]
    serpeinte.pop()

    if direccion == "ARRIBA" and direccion != "ABAJO":
        nuevaCabezaY -= velocidad
    elif direccion == "ABAJO" and direccion != "ARRIBA":
        nuevaCabezaY += velocidad
    elif direccion == "DERECHA" and direccion != "IZQUIERDA":
        nuevaCabezaX += velocidad
    elif direccion == "IZQUIERDA" and direccion != "DERECHA":
        nuevaCabezaX -= velocidad
    
    serpeinte.insert(0, (nuevaCabezaX, nuevaCabezaY) )

# Dibujar la sepriente y acutlaizar la pantalla
def dibujar(win, serpeinte, x, y):
    global anchoDePixel
    global altoDePixel
    global Puntos
    #Puntos
    FuenteTexto = pygame.font.SysFont("Arial", 20)
    Texto = FuenteTexto.render("Puntos:" +str(Puntos), 0, (255, 255, 255) )

    #Instrucciones para saber que botones usar para poner pausa y reiniciar
    TextoPausa = FuenteTexto.render("Presiona P para poner pausa", 0, (255, 255, 255) )
    TextoReinicio = FuenteTexto.render("Presiona R para reiniciar el juego", 0, (255, 255, 255) )

    win.fill( (0, 0, 0) )

    for pixel in serpeinte:
        pygame.draw.rect(win, (0, 255, 0), (pixel[0], pixel[1], anchoDePixel, altoDePixel) )

    #Dibujar la comida
    pygame.draw.rect(win, (14, 28, 222), (x, y, 10, 10))

    #Dibujar el limite inferior 
    pygame.draw.rect(win, (255, 255, 255), (0, 501, 500, 1))

    #Puntos
    win.blit(Texto, (10, 540) )
    win.blit(TextoPausa, (230, 520) )
    win.blit(TextoReinicio, (230, 550) )

# Las colisiones con las paredes y comida... por ahora
def Colisones(win, serpeinte):
    global ScreenSize
    global Running
    global comidaX
    global comidaY
    global Puntos

    #Sonidos
    Muerte = pygame.mixer.Sound("darksouls_youdied.ogg")
    Comiendo = pygame.mixer.Sound("ComiendoSonido.ogg")

    #Pantalla de Muerte
    PantallaMuerte = pygame.image.load("Died.png")

    #Texto de muerte
    FuenteTexto = pygame.font.SysFont("Bold", 25)
    Texto = FuenteTexto.render("Presiona Q para intentar de nuevo", 0, (255, 255, 255) )

    nuevaCabezaX = serpeinte [0] [0]
    nuevaCabezaY = serpeinte [0] [1]

    # Fin del juego por si toca las paredes
    if nuevaCabezaX >= ScreenSize or nuevaCabezaX < 0 or nuevaCabezaY >= ScreenSize or nuevaCabezaY < 0:
        Muerte.play()
        win.fill( (0, 0, 0) )
        win.blit(PantallaMuerte, (0,130) )
        win.blit(Texto, (120, 325) )
        pygame.display.update()
        Muerto(win, serpeinte)

    #Fin del juego por si toca su mismo cuerpo
    for pixel in serpeinte[1: ]:
        if nuevaCabezaX == pixel[0] and nuevaCabezaY == pixel[1]:
            Muerte.play()
            win.fill( (0, 0, 0) )
            win.blit(PantallaMuerte, (0,130) )
            win.blit(Texto, (120, 325) )
            pygame.display.update()
            Muerto(win, serpeinte)

    #Cuando come, hacer aparecer la comida en otro lado y agregar un nuevo elemento a la cola
    if nuevaCabezaX == comidaX and nuevaCabezaY == comidaY:

        win.fill( (0, 0, 0) )
        comidaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
        comidaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10
        Comiendo.play()
        pygame.time.delay(50)
        serpeinte.append( (nuevaCabezaX, nuevaCabezaY) )
        Puntos += 1

def Pausa(win, Sonido):
    Pausado = True

    FuenteTexto1 = pygame.font.SysFont("Arial", 30)
    FuenteTexto2 = pygame.font.SysFont("Arial", 20)
    Texto = FuenteTexto1.render("Pausa", 0, (255, 255, 255) )
    Texto2 = FuenteTexto2.render("Presiona L para continuar", 0, (255, 255, 255) )

    while Pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    Sonido.play()
                    pygame.time.delay(100)
                    Pausado = False

        #Instrucciones mientras estas en pausa
        win.fill( (0, 0, 0) )
        win.blit(Texto, (200, 240) )
        win.blit(Texto2, (150, 275) )
        pygame.display.update()

def Muerto(win, serpiente):
    global comidaX
    global comidaY
    global Puntos
    global direccion
    global ScreenSize
    Muerto = True

    while Muerto:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Muerto = False
                    Puntos = 0
                    nuevaCabezaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
                    nuevaCabezaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10
                    direccion = ""

                    #Comida de la serpiente 
                    comidaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
                    comidaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10

                    serpiente.clear()
                    serpiente.append( (nuevaCabezaX, nuevaCabezaY) )
                    
def reinicio(serpiente):
    global comidaX
    global comidaY
    global Puntos
    global direccion
    global ScreenSize

    Puntos = 0
    nuevaCabezaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
    nuevaCabezaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10
    direccion = ""

    #Comida de la serpiente 
    comidaX = round(random.randrange(0, ScreenSize - 10) / 10) * 10
    comidaY = round(random.randrange(0, ScreenSize - 10) / 10) * 10

    serpiente.clear()
    serpiente.append( (nuevaCabezaX, nuevaCabezaY) )



def main():
    # Tomar variables que estan fuera de la funcion
    global ScreenSize
    global Running
    global cabezax 
    global cabezay 
    global anchoDePixel 
    global altoDePixel
    global vesente
    global velocidad
    global direccion
    global comidaX
    global comidaY
    global Puntos

    pygame.init()

    win = pygame.display.set_mode( (ScreenSize, 600) )
    pygame.display.set_caption("Snake")

    #Sonidos
    Seleccion = pygame.mixer.Sound("Persona 5 Seleccion.ogg")
    PausaSonido = pygame.mixer.Sound("Persona 5 Pausa.ogg")

    while Running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and direccion != "IZQUIERDA":
            direccion = "DERECHA"
        elif keys[pygame.K_LEFT] and direccion != "DERECHA":
            direccion = "IZQUIERDA"
        elif keys[pygame.K_DOWN] and direccion != "ARRIBA":
            direccion = "ABAJO"
        elif keys[pygame.K_UP] and direccion != "ABAJO":
            direccion = "ARRIBA"
        #Boton Pausa
        elif keys[pygame.K_p]:
            PausaSonido.play()
            pygame.time.delay(100)
            Pausa(win, Seleccion)
        #Boton Reiniciar
        elif keys[pygame.K_r]:
            Seleccion.play()
            pygame.time.delay(100)
            reinicio(vesente)

        moverSerpiente(direccion, vesente)

        dibujar(win, vesente, comidaX, comidaY)

        Colisones(win, vesente)

        pygame.display.update()
        


main()