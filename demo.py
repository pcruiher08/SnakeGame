import pygame
import random

SCREENSIZE = 500
running = True

dimensionPixel = 20
vel = 20
jugador = (200, 480)

enemigos = []

enemigosTick = 2
currentTick = 0

def actualizarEnemigos():
    global enemigos

    enemigos.append([random.randint(1, 24) * 20, 0])

    removeIndices = []
    
    for i, enemigo in enumerate(enemigos):
        enemigo[1] = enemigo[1] + vel
        if enemigo[1] > SCREENSIZE:
            removeIndices.append(i)

    for index in removeIndices:
        enemigos.pop(index)

def checarColision():
    global jugador
    global enemigos
    global running

    for enemigo in enemigos:
        if enemigo[0] == jugador[0] and enemigo[1] == jugador[1]:
            running = False


def manejarTeclado():
    global jugador
    global dimensionPixel
    keys = pygame.key.get_pressed()

    nuevaPosX = jugador[0]

    if keys[pygame.K_RIGHT]:
        nuevaPosX += vel
    elif keys[pygame.K_LEFT]:
        nuevaPosX -= vel

    if nuevaPosX > SCREENSIZE - dimensionPixel:
        nuevaPosX = SCREENSIZE - dimensionPixel
    if nuevaPosX < 0:
        nuevaPosX = 0

    jugador = (nuevaPosX, jugador[1])

def dibujar(win):
    global jugador
    global enemigos

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (jugador[0], jugador[1], dimensionPixel, dimensionPixel))

    for enemigo in enemigos:
        pygame.draw.rect(win, (255,0,0), (enemigo[0], enemigo[1], dimensionPixel, dimensionPixel))

    pygame.display.update()

def main():
    global SCREENSIZE
    global running
    global dimensionPixel
    global currentTick
    global enemigosTick
    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
    pygame.display.set_caption("Demo")

    while running: 
        currentTick += 1
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        manejarTeclado()  
        if currentTick > enemigosTick:
            actualizarEnemigos() 
            currentTick = 0  
        
        checarColision()

        dibujar(win)

    pygame.quit()

main()