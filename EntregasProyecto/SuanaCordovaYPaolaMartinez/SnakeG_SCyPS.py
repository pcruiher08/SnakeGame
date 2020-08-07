#IMPORTACIÓN DE LIBRERÍAS
import pygame
import random
import sys
from pygame.locals import *
from pygame import mixer 

#CONFIGURACIÓN DEL JUEGO
SCREENSIZE = 500
running = True
cabezaX = 50
cabezaY = 50
anchoDePixel = 10
altoDePixel = 10
vel = 10
direccion = "DERECHA"
comidaX = 0
comidaY = 0
crece = 0
findepausa = True
file = 'despacitovidg.wav'
soundGO = 'wahwahwah.wav'
cuantaComida = 0

serpiente = [(cabezaX, cabezaY), (60, 50), (70,50), (80,50), (90,50)]

letreroGO1 = '11101110100010111000111010001011101111'
letreroGO2 = '10001010110110100000101010001010001001'
letreroGO3 = '11101110101010110000101001010011001111'
letreroGO4 = '10101010100010100000101001010010001010'
letreroGO5 = '11101010100010111000111000100011101001'

letreroP = '1001'

#display de la pantalla y nombre del juego
pygame.init()
win = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
pygame.display.set_caption("Shakey-Snakey")


#Inicializar Musica
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


#Función para aparecer comida
def apareceComida():
    global comidaX
    global comidaY

    comidaX = 10*random.randint(1,49)
    comidaY = 10*random.randint(1,49)


#Función para checar colisión con comida
def colisionComida():
    global comidaX
    global comidaY
    global cuantaComida
    colision = serpiente[0][0] == comidaX and serpiente[0][1] == comidaY
  
    if colision: 
        cuantaComida = cuantaComida + 1
    return colision

#Función para checar colisión con pared
def colisionPared():
    return (serpiente[0][0] == 500 or serpiente[0][0] == -10) or (serpiente[0][1] == 500 or serpiente[0][1] == -10)


#Función para checar colisión consigo misma
def colisionSerpiente():
    largo = len(serpiente)
    if largo > 5:   
        for i in range(5,largo):
            if serpiente[0] == serpiente[i]:
                serpiente.pop()
                return True
        return False 


#Función para letrero "Game Over"
def letreroGameOver():
    for i in range(0,38):
        x= 10*i + 60
        if letreroGO1[i] == '1':
            pygame.draw.rect(win, (153,0,76), (x,200,anchoDePixel,altoDePixel))
        if letreroGO2[i] == '1':
            pygame.draw.rect(win, (153,0,76), (x,210,anchoDePixel,altoDePixel))
        if letreroGO3[i] == '1':
            pygame.draw.rect(win, (153,0,76), (x,220,anchoDePixel,altoDePixel))
        if letreroGO4[i] == '1':
            pygame.draw.rect(win, (153,0,76), (x,230,anchoDePixel,altoDePixel))
        if letreroGO5[i] == '1':
            pygame.draw.rect(win, (153,0,76), (x,240,anchoDePixel,altoDePixel))
    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(soundGO)
    pygame.mixer.music.play()
    pygame.time.delay(5000)


#Función para agradecimientos
def agradecimientos():
    fondo = cargar_imagen('suypa.png')
    win.blit(fondo, (0,0))
    pygame.display.flip()


#Función para bienvenida
def bienvenido():
    fondo = cargar_imagen('bienvenido.png')
    win.blit(fondo, (0,0))
    pygame.display.flip()


#Función para letrero Pausa [II]
def pausa():
    for i in range(0,4):
        x = 10*i + 230
        if letreroP[i] == '1':
            pygame.draw.rect(win, (102,0,102), (x,200,anchoDePixel,altoDePixel))
            pygame.draw.rect(win, (102,0,102), (x,210,anchoDePixel,altoDePixel))
            pygame.draw.rect(win, (102,0,102), (x,220,anchoDePixel,altoDePixel))
            pygame.draw.rect(win, (102,0,102), (x,230,anchoDePixel,altoDePixel))
            pygame.draw.rect(win, (102,0,102), (x,240,anchoDePixel,altoDePixel))
    pygame.mixer.music.pause()      
    pygame.display.update()


#Función para el movimiento de la serpiente
def moverSerpiente(direccion, serpiente):
    global vel
    global crece
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]

    if crece > 0:
        crece = crece - 1
    else:
        serpiente.pop()

    if direccion == "ARRIBA":
        nuevaCabezaY -= vel
    elif direccion == "ABAJO":
        nuevaCabezaY += vel
    elif direccion == "DERECHA":
        nuevaCabezaX += vel
    elif direccion == "IZQUIERDA":
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX, nuevaCabezaY))

#Funcion para cargar fondo
def cargar_imagen(nombre,transparente=False):
    imagen = pygame.image.load(nombre)
    imagen = pygame.transform.scale(imagen, (500,500))
    return imagen

#Función parala pantalla con todos sus contenidos
# win: ventana del juego
# serpiente: arreglo de tuplas que contiene la serpiente

def dibujar(win, serpiente):
    global anchoDePixel
    global altoDePixel
    global cuantaComida
    
    fondo = cargar_imagen('fondocespedtextura.jpg')
    win.blit(fondo, (0,0))

    Fpuntaje = pygame.font.SysFont('Rockwell', 15)
    textPuntaje = Fpuntaje.render("Puntaje: "+str(cuantaComida*5), True, (255,255,255), (0,128,0))
    win.blit(textPuntaje, (4,0))
    pygame.display.flip()

    for pixel in serpiente:
        pygame.draw.rect(win, (255,128,0), (pixel[0],pixel[1],anchoDePixel,altoDePixel))
   
    pygame.draw.rect(win, (200,0,0), (comidaX,comidaY,anchoDePixel,altoDePixel))
    pygame.display.update()


#DEFINICIÓN DE FUNCIÓN PRINCIPAL DEL JUEGO
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
    global crece
    global comidaX
    global comidaY
    global findepausa

    #CICLO DE LA VIDA DEL JUEGO
    bienvenido()
    pygame.time.delay(5000)
    apareceComida()
    while running:
        pygame.time.delay(80)
        moverSerpiente(direccion,serpiente)
        dibujar(win,serpiente)

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
            if direccion != "ARRIBA":
                direccion = "ABAJO"
        elif keys[pygame.K_p]:
            pausa()
            findepausa = False
            while not findepausa:
                for e in pygame.event.get():
                    k = pygame.key.get_pressed()
                    findepausa = k[pygame.K_p]
            pygame.mixer.music.unpause()

        if colisionComida():
            crece = crece + 3         
            apareceComida()
        elif colisionSerpiente() or colisionPared():
            letreroGameOver()
            agradecimientos()
            pygame.time.delay(2000)
            pygame.quit()

    agradecimientos()
    pygame.time.delay(2000)     
    pygame.quit()


#EJECUTAR EL JUEGO
main()

'''
Autoras: Susy Córdova y Paola Martínez
Música: Vinheteiro en YouTube
¡Gracias Monterrey Programming Hub!
'''