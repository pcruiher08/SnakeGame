'''Importación de librerías'''
import pygame
import random

'''Configuración del juego'''
SCREENSIZE = 500
running = True
cabezaX = 50
cabezaY = 50
anchoDePixel = 10
altoDePixel = 10
vel = 10

foodX = 200
foodY = 200

direccion = "DERECHA"

serpiente = [(cabezaX,cabezaY)]

def moverSerpiente(direccion, serpiente):
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

def spawnFood():
    global foodX
    global foodY
    foodX = random.randint(1, 49) * 10
    foodY = random.randint(1, 49) * 10
    print((foodX,foodY))

def draw(win, serpiente):
    global anchoDePixel
    global altoDePixel
    global foodX
    global foodY

    win.fill((0,0,0))

    #draw food
    pygame.draw.rect(win, (0,255,255), (foodX,foodY,anchoDePixel,altoDePixel))

    #draw snake
    for pixel in serpiente:
        pygame.draw.rect(win, (255,0,0), (pixel[0],pixel[1],anchoDePixel,altoDePixel))
    
    pygame.display.update()

def gameOver():
    global running
    #mostrar score en grande
    print("perdiste")
    running = False
    return

def serpienteCome(serpiente):
    spawnFood()
    serpiente.append(serpiente[len(serpiente) - 1]) 

def revisaColisiones(serpiente):
    #revisar colision serpiente-serpiente
    for i in range(1,len(serpiente)):
        if serpiente[0] == serpiente[i]:
            #se acaba el juego porque la cabeza choco con el cuerpo
            gameOver()
    
    #revisar colision serpiente-pared
    if serpiente[0][0] < 0 or serpiente[0][0] > 500 or serpiente[0][1] < 0 or serpiente[0][1] > 500:
        #chocamos con pared
        gameOver()
    
    #revisar colision serpiente-comida
    if serpiente[0] == (foodX, foodY):
        #la serpiente está comiendo
        serpienteCome(serpiente)
        


'''Definición de la función principal del juego'''
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
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption("SnakeGame")
    '''Ciclo de vida del juego'''
    while running: 
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            direccion = "DERECHA"
            cabezaX += vel
        elif keys[pygame.K_LEFT]:
            direccion = "IZQUIERDA"
            cabezaX -= vel
        elif keys[pygame.K_UP]:
            direccion = "ARRIBA"
            cabezaY -= vel
        elif keys[pygame.K_DOWN]:
            direccion = "ABAJO"
            cabezaY += vel

        revisaColisiones(serpiente)
        moverSerpiente(direccion,serpiente)
        draw(win, serpiente)

    pygame.quit()
'''Ejecutar el juego'''
main()