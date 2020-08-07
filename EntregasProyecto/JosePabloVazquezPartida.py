import pygame
import random

SCREENSIZE = 500 
running = True
cabezaX = 50
cabezaY= 50
anchoDePixel = 10
altoDePixel = 10
vel = 10
direccion = "DERECHA"
negro = (0,0,0)
verde = (0,255,0)
rojo = (255,0,0)
blanco = (255, 255, 255)
x = random.randrange(0,49) * 10
y = random.randrange(0,49) * 10

serpiente = [(cabezaX,cabezaY)]

comida = [(x, y)]


def moverSerpiente(direccion,serpiente):
    global vel
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]

    serpiente.pop()

    if direccion == "ARRIBA":
        nuevaCabezaY -= vel
    elif direccion == "ABAJO":
        nuevaCabezaY += vel
    elif direccion == "DERECHA":
        nuevaCabezaX += vel
    elif direccion == "IZQUIERDA":
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))

def dibujar(win, serpiente):
    global anchoDePixel
    global altoDePixel

    win.fill((negro))

    for pixel in serpiente:
        pygame.draw.rect(win, (verde), (pixel[0],pixel[1], anchoDePixel,altoDePixel))
    pygame.display.update()

def dibujarComida(win, comida):
    global anchoDePixel
    global altoDePixel

    pygame.display.flip()

    for pixel in comida:
        pygame.draw.rect(win, (rojo), (pixel[0], pixel[1], anchoDePixel,altoDePixel))
    
    pygame.display.update()

def crecer(serpiente, comida):
    if serpiente[0] == comida[0]:
        if direccion == "DERECHA":
            colaX = cabezaX - 10
            colaY = cabezaY
            serpiente.append((colaX, colaY))
        elif direccion == "IZQUIERDA":
            colaX = cabezaX + 10
            colaY = cabezaY
            serpiente.append((colaX, colaY))
        elif direccion == "ARRIBA":
            colaX = cabezaX 
            colaY = cabezaY - 10
            serpiente.append((colaX, colaY))
        elif direccion == "ABAJO":
            colaX = cabezaX + 10
            colaY = cabezaY
            serpiente.append((colaX, colaY))

def teleportComida(serpiente,comida):
    if comida[0] == serpiente[0]:
        comida.pop()
        x = random.randrange(0, 49)* 10
        y = random.randrange(0, 49)* 10
        comida.append((x,y))
        pygame.display.update()

def colisionBordes(cabezaX, cabezaY):
    global running
    (cabezaX,cabezaY) = serpiente[0]
    if cabezaX <= 0 or cabezaX >= 500:
        running = False
    elif cabezaY <= 0 or cabezaY >= 500:
        running = False

def colisionSerpiente(serpiente):
    global running
    cuenta = serpiente.count(serpiente[0])
    serpiente.count(serpiente[0])
    if cuenta > 1:
        running = False

def main():
    global SCREENSIZE
    global running
    global cabezaX
    global cabezaY
    global anchoDePixel
    global altoDePixel
    global serpiente
    global vel
    global direccion

    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
    pygame.display.set_caption("SnakeGame")

    while running:
        clock = pygame.time.Clock()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if direccion != "IZQUIERDA":
                direccion = "DERECHA"
        elif keys[pygame.K_LEFT]:
            if direccion != "DERECHA":
                direccion = "IZQUIERDA"
        elif keys[pygame.K_UP]:
            if direccion != "ABAJO":
                direccion = "ARRIBA"
        elif keys[pygame.K_DOWN]:
            if direccion != "Arriba":
                direccion = "ABAJO"

        moverSerpiente(direccion,serpiente)

        dibujar(win,serpiente)

        dibujarComida(win, comida)

        crecer(serpiente, comida)

        teleportComida(serpiente, comida)

        colisionBordes(cabezaX, cabezaY)

        colisionSerpiente(serpiente)

    pygame.quit()


main()