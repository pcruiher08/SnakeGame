import pygame
import random

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("SnakeGame")

x = 50
y = 50
width = 10
height = 10
vel = 10

black = (0,0,0)
#arreglo de coordenadas para dibujar la serpiente
serpiente = [(x,y)]
snakeSize = len(serpiente)

pellet = (0,0)

direccion = "RIGHT"

pellets = 0
flagComi = False
ticks = 0

run = True

def drawMatrix():
    for i in range(50):
        pygame.draw.line(window, (255,255,255), (0, i * 10), (500, i * 10), 1)
        pygame.draw.line(window, (255,255,255), (i * 10, 0), (i * 10, 500), 1)


def generarCoordenadaRandom():
    newX = random.randint(0, 50) * 10
    newY = random.randint(0, 50) * 10
    return (newX, newY)

def showScore(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((500/2),(500/2))
    window.blit(TextSurf, TextRect)

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

    #serpiente[0][0] es x
    #serpiente[0][1] es y

    if(serpiente[0][0]<0 or serpiente[0][0]>500 or serpiente[0][1]<0 or serpiente[0][1]>500):
        #chocamos con pared
        
        print("me sali de la pantalla")
        gameOver()
        return
    
    choqueConmigo = False

    for pixel in serpiente:
        if serpiente.count(pixel)>1:
            choqueConmigo = True
            break

    if choqueConmigo:
        print("choque conmigo")
        gameOver()
        return

    if serpiente[snakeSize - 1] == pellet:
        flagComi = True
        print("munch munch")
        spawnPellet()
    

def checarTeclado():
    global x
    global y
    global direccion
    global vel 

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
    global flagComi
    #la cola se debe poner enfrente de la cabeza en la direccion a la que se está moviendo
    print("serpiente Antes: ", serpiente)
    print(direccion)
    if direccion == "LEFT":
        serpiente.append((serpiente[snakeSize-1][0]-vel,serpiente[snakeSize-1][1]))
    if direccion == "RIGHT":
        serpiente.append((serpiente[snakeSize-1][0]+vel,serpiente[snakeSize-1][1])) 
    if direccion == "UP":
        serpiente.append((serpiente[snakeSize-1][0],serpiente[snakeSize-1][1]-vel))
    if direccion == "DOWN":
        serpiente.append((serpiente[snakeSize-1][0],serpiente[snakeSize-1][1]+vel))
    

    if not flagComi:
        #despues hay que checar si comio, para borrar la cola para que la serpiente no crezca 
        serpiente.pop(0)
    print("serpiente Despues: ", serpiente)
    
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def dibujarElementos():
    global window
    global serpiente
    drawMatrix()
    window.fill((128,128,128))

    # Dibujar serpiente
    for pixel in serpiente:
        pygame.draw.rect(window, (255,0,0), (pixel[0],pixel[1],width, height))

    # Dibujar pellet
    pygame.draw.rect(window, (0, 255, 0), (pellet[0], pellet[1],width, height))
    drawMatrix()
    showScore(str(serpiente[0]))
    pygame.display.update()


def main():
    global ticks
    global run
    global pellets
    global flagComi
    global serpiente

    spawnPellet()

    while run: 
        print(serpiente)

        ticks += 1
        '''
        if ticks%10 == 0:
            pellets += 1
            flagComi = True
        '''

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