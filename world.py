import pygame
import random

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("SnakeGame")

x = 50
y = 50
width = 5
height = 5
vel = 5

#arreglo de coordenadas para dibujar la serpiente
serpiente = [(x,y)]
snakeSize = len(serpiente)

pellet = (0,0)

direccion = "RIGHT"

pellets = 0
flagComi = False
ticks = 0

run = True

def generarCoordenadaRandom():
    newX = random.randint(0, 100) * 5
    newY = random.randint(0, 100) * 5
    return (newX, newY)

def spawnPellet():
    global pellet
    newPellet = generarCoordenadaRandom()
    valida = True

    while not valida:
        valida = True
        for point in serpiente:
            if point[0] == newPellet[0] and point[1] == newPellet[1]:
                valida = False
                break

        if not valida:
            newPellet = generarCoordenadaRandom()
    
    pellet = newPellet

def gameOver():
    global run
    #mostrar score en grande
    print("perdiste")
    run = False
    return

def checarColisiones():
    global flagComi
    global serpiente
    global x, y
    #hay que checar si chocamos con paredes
    #hay que checar si chocamos con nosotros
    #hay que checar si chocamos con pellets

    if(x<=0 or x>=500 or y<=0 or y>=500):
        #chocamos con pared
        print("me sali de la pantalla")
        gameOver()
    
    choqueConmigo = False

    for pixel in serpiente:
        if serpiente.count(pixel)>1:
            choqueConmigo = True
            break

    if choqueConmigo:
        print("choque conmigo")
        gameOver()

    if serpiente[snakeSize - 1] == pellet:
        flagComi = True
        print("munch munch")
    

def checarTeclado():
    global x
    global y
    global direccion

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        direccion = "LEFT"
    if keys[pygame.K_RIGHT]:
        x += vel
        direccion = "RIGHT"
    if keys[pygame.K_UP]:
        y -= vel
        direccion = "UP"
    if keys[pygame.K_DOWN]:
        y += vel
        direccion = "DOWN"

def actualizarSerpiente():
    global direccion
    global serpiente
    #la cola se debe poner enfrente de la cabeza en la direccion a la que se está moviendo
    if direccion == "LEFT":
        serpiente.append((x-vel,y))
    if direccion == "RIGHT":
        serpiente.append((x+vel,y)) 
    if direccion == "UP":
        serpiente.append((x,y-vel))
    if direccion == "DOWN":
        serpiente.append((x,y+vel))
    
    print(serpiente)

    if not flagComi:
        #despues hay que checar si comio, para borrar la cola para que la serpiente no crezca 
        serpiente.pop(0)

    #luego hay que checar si comio pellet o no, pero como no hay pellets aun, eso no se hace aun
    #pero ya tenemos pellets asi que hay que implementar el crecimiento

def dibujarElementos():
    global window
    global serpiente
    window.fill((0,0,0))

    # Dibujar serpiente
    for pixel in serpiente:
        pygame.draw.rect(window, (255,0,0), (pixel[0],pixel[1],width, height))

    # Dibujar pellet
    pygame.draw.rect(window, (0, 255, 0), (pellet[0], pellet[1],width, height))

    pygame.display.update()


def main():
    global ticks
    global run
    global pellets
    global flagComi
    global serpiente

    spawnPellet()

    while run: 
        ticks += 1

        if ticks%10 == 0:
            pellets += 1
            flagComi = True

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        checarTeclado()
        checarColisiones()
        actualizarSerpiente()
        dibujarElementos()

        flagComi = False

    pygame.quit()

main()