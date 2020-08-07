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
direccion = "DERECHA"
score = 0

serpiente = [(cabezaX,cabezaY)]

#Funcion para ir moviendo la serpiente
def moverSerpiente(direccion, serpiente):
    global vel
    global score

    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]
    

    if direccion == "ARRIBA":
        nuevaCabezaY -= vel
    elif direccion == "ABAJO":
        nuevaCabezaY += vel
    elif direccion == "DERECHA":
        nuevaCabezaX += vel
    elif direccion == "IZQUIERDA":
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))  

#Funcion para generar la comida de la serpiente
def food_serpiente():
    food_pos = [random.randint(0, 49)*10, random.randint(0, 49)*10]
    return food_pos

#Funcion para determinar la dirección de la serpiente y cumplir solo tenga una cabeza
def Direccion():
    global direccion

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and direccion != "IZQUIERDA":
        direccion = "DERECHA"
    elif keys[pygame.K_LEFT] and direccion != "DERECHA":
        direccion = "IZQUIERDA"
    elif keys[pygame.K_UP] and direccion != "ABAJO":
        direccion = "ARRIBA"
    elif keys[pygame.K_DOWN] and direccion != "ARRIBA":
        direccion = "ABAJO"
    elif keys[pygame.K_p]:    #Seleccion para la Pausa
        pausa()

#Funcion para llamar las colisiones
def colisiones(serpiente):
    global score
    global running
    
    if serpiente[0][0] >= 500 or serpiente[0][0] <= 0:
        print(f"Game Over   Score: {score}")
        running = False

    if serpiente[0][1] >= 500 or serpiente[0][1] <= 0:
        print(f"Game Over   Score: {score}")
        running = False

    if len(serpiente) > 1:
        if serpiente[0] in serpiente [1:]:
            print(f"Game Over Score: {score}")
            running = False

#Funcion para realizar la pausa del juego.
def pausa():
    global running
    
    Juego_pausado = True
    while Juego_pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    Juego_pausado = False

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
    global score

    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption("SnakeGame")

    '''Ciclo de vida del juego'''

    #Llamado de la funcion para la comida de la serpiente
    pos_food = food_serpiente()

    while running: 
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        Direccion()
        win.fill((0,0,0))
        #Llamado de funcion para el movimiento de la serpiente
        moverSerpiente(direccion,serpiente)

        if serpiente[0][0] == pos_food[0] and serpiente[0][1] == pos_food[1]:
            pos_food = food_serpiente()
            score += 1
        else:
            serpiente.pop()

        for pixel in serpiente:
            pygame.draw.rect(win, (255,0,0), (pixel[0],pixel[1],anchoDePixel,altoDePixel))
    
        pygame.draw.rect(win, (255,160,60), (pos_food[0],pos_food[1],anchoDePixel,altoDePixel))
        pygame.display.update()
        #Llamado de funcion de colisiones
        colisiones(serpiente)
       


pygame.quit()
'''Ejecutar el juego'''
main()