# INSTRUCCIONES: Presiona la tecla 'P' para poner pausa,
#                en pausa, presionar 'P' de nuevo para continuar
#                y presionar 'q' para salir del juego.
#                Presionar 'r' durante el juego para reiniciar.

import pygame, random

def moverSerpiente(direccion, serpiente):
    global vel
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]
    serpiente.pop()

    if direccion == 'ARRIBA':
        nuevaCabezaY -= vel
    elif direccion == 'ABAJO':
        nuevaCabezaY += vel
    elif direccion == 'DERECHA':
        nuevaCabezaX += vel
    elif direccion == 'IZQUIERDA':
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX, nuevaCabezaY))

def dibujar(surface, serpiente, anchoPixel):
    surface.fill((35, 35, 35))      # Not quite black
    for pixel in serpiente:
        pygame.draw.rect(surface, (255,0,0), (pixel[0],pixel[1],anchoPixel,anchoPixel))
    pygame.display.update()

def exitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Límites de la ventana de 500 x 500 para la colisión serpiente-borde
    if serpiente[0][0] >= 500 or serpiente[0][0] <= -25 or serpiente[0][1] >= 500 or serpiente[0][1] <= -25:
        pygame.quit()
        quit()
    # Colisión serpiente-serpiente
    if serpiente[0] in serpiente[2:]:
        pygame.quit()
        quit()

def dibujarComida(surface, comidaX, comidaY, anchoPixel): 
    pygame.draw.rect(surface, (0,255,0), (comidaX,comidaY,anchoPixel,anchoPixel))
    pygame.display.update()

def comer():
    global comidaX, comidaY
    # Detectar colisión serpiente-comida y cambiar posición de comida
    if serpiente[0][0] == comidaX and serpiente[0][1] == comidaY:
        serpiente.insert(0,(comidaX, comidaY))
        '''La pantalla es de 500x500 y el ancho de los pixeles es 25,
           por lo que la comida debe aparecer en una posición que sea múltiplo de 25.
           El rango aleatorio 1-18 se eligió para que la comida no apareza pegada
           a los bordes de la pantalla o fuera de esta.'''
        comidaX = random.randint(1,18) * 25
        comidaY = random.randint(1,18) * 25
        while (comidaX,comidaY) in serpiente:
            comidaX = random.randint(1,18) * 25
            comidaY = random.randint(1,18) * 25        

def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
                # elif event.key == pygame.K_r:
                #     print('r')
                    # cabezaX = 50
                    # cabezaY = 50
                    # direccion = 'DERECHA'
                    # comidaX = random.randint(1,18) * 25
                    # comidaY = random.randint(1,18) * 25
                    # serpiente = [(cabezaX,cabezaY)]

def score(surface):
    global serpiente
    score = len(serpiente) - 1
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Score: {score}', True, (255,255,255))
    surface.blit(img, (10, 10))
    pygame.display.update()

screenSize = 500
cabezaX = 50
cabezaY = 50
anchoPixel = 25
vel = 25
direccion = 'DERECHA'
comidaX = random.randint(1,18) * 25
comidaY = random.randint(1,18) * 25

serpiente = [(cabezaX,cabezaY)]

def main():
    global screenSize, cabezaX, cabezaY, anchoDePixel, altoDePixel, vel, serpiente, direccion, comidaX, comidaY
    pygame.init()
    win = pygame.display.set_mode((screenSize, screenSize))
    pygame.display.set_caption('Snake Game')

    while 1:
        pygame.time.delay(100)
        exitGame()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and direccion != 'IZQUIERDA':
            direccion = 'DERECHA'
        elif keys[pygame.K_LEFT]and direccion != 'DERECHA':
            direccion = 'IZQUIERDA'
        elif keys[pygame.K_UP]and direccion != 'ABAJO':
            direccion = 'ARRIBA'
        elif keys[pygame.K_DOWN] and direccion != 'ARRIBA':
            direccion = 'ABAJO'
        elif keys[pygame.K_p]:
            pause()
        elif keys[pygame.K_r]:          # Presionar 'r' para pausar.
            cabezaX = 50
            cabezaY = 50
            direccion = 'DERECHA'
            comidaX = random.randint(1,18) * 25
            comidaY = random.randint(1,18) * 25
            serpiente = [(cabezaX,cabezaY)]

        moverSerpiente(direccion, serpiente)
        dibujar(win, serpiente, anchoPixel)
        comer()
        dibujarComida(win, comidaX, comidaY, anchoPixel)
        score(win)

main()