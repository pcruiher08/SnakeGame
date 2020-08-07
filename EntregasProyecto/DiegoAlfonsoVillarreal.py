'''Importación de librerías'''
import pygame
from random import randrange
'''Configuración del juego'''
SCREENSIZE = 500
running = True
cabezaX = 50
cabezaY = 50
anchoDePixel = 10
altoDePixel = 10
vel = 10
direccion = "RIGHT"
lose = False
x = 200
xp = x
y = 300
yp = y
fruitpos = (x,y)
crecer = 0
a = 0
b = -8
aaa = (a,a,a)
bbb = (b,b,b)
win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
serpiente = [(cabezaX,cabezaY)]
respawn = False
time = 0
points = 0
point = "0"
paused = False

def RESTART():
    global cabezaX
    global cabezaX
    global cabezaY
    global serpiente
    global direccion
    global lose
    global a
    global x
    global xp
    global y
    global yp
    global fruitpos
    global crecer
    global aaa
    global bbb
    global b
    global font
    global win
    global respawn
    global time
    global points
    global paused
    global point
    cabezaX = 50
    cabezaY = 50
    direccion = "RIGHT"
    lose = False
    x = 200
    xp = x
    y = 300
    yp = y
    fruitpos = (x,y)
    crecer = 0
    a = 0
    b = -8
    aaa = (a,a,a)
    bbb = (b,b,b)
    serpiente = [(cabezaX,cabezaY)]
    respawn = True
    time = 0
    points = 0
    point = str(points)
    paused = False

def animacionchida():
    global a
    global b
    global aaa
    global bbb
    global win
    global deathmsg 
    global font
    pygame.time.delay(80)
    if a <= 10:
        a += 1
        aaa = (a,a,a)
    pygame.draw.rect(win, aaa, (0, 169, 500, 160))
    if b <= 192:
        b += 8
        bbb = (b, 0, 0)
    deathmsg = font.render("YOU DIED", True, bbb)


def fruitgen(serpiente):
    global xp
    global yp
    global x
    global y
    global fruitpos
    global anchoDePixel
    global altoDePixel
    global points
    global point

    while ((xp, yp) in serpiente):
        xp = 10 * (randrange(0 , 49))
        yp = 10 * (randrange(0 , 49))

    x = xp
    y = yp
    fruitpos = (x,y)
    points += 1
    point = str(points)


def moverserpiente(direccion, serpiente):
    global vel
    global lose
    global fruitpos
    global crecer
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]

    if serpiente[0] == fruitpos:
        fruitgen(serpiente)
        crecer += 1

    if crecer == 0:
        serpiente.pop()
    else:
        crecer -= 1

    if direccion == "UP":
        nuevaCabezaY -= vel
    elif direccion == "DOWN":
        nuevaCabezaY += vel
    elif direccion == "LEFT":
        nuevaCabezaX -= vel
    elif direccion == "RIGHT":
        nuevaCabezaX += vel
    
    if (nuevaCabezaX,nuevaCabezaY) in serpiente:
        lose = True
    elif (nuevaCabezaX < 0 or nuevaCabezaX >= 500 or nuevaCabezaY < 0 or nuevaCabezaY >= 500):
        lose = True
    else:
        serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))
    

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
    global lose
    global a
    global b
    global font
    global win
    global time
    global respawn
    global point
    global paused
    pygame.init()
    pygame.display.set_caption("SnakeGame")
    font = pygame.font.SysFont("cambriacambriamath", 80)
    font2 = pygame.font.SysFont("cambriacambriamath", 16)
    '''Ciclo de vida del juego'''
    
    while running:

        while lose == False: 
            pygame.time.delay(50)

            # El conteo de cuando le picamos a restart
            if respawn == True:

                win.fill((0,0,0))

                for pixel in serpiente:
                    pygame.draw.rect(win, (255,0,0), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

                pygame.draw.rect(win, (255,233,0), (x, y, anchoDePixel, altoDePixel))

                if time < 60:
                    if time < 20:
                        num = font.render("3", True, (255,255,255))
                        win.blit(num, (249, 75))
                        time += 1
                    elif time < 40:
                        num = font.render("2", True, (255,255,255))
                        win.blit(num, (249, 75))
                        time += 1
                    else:
                        num = font.render("1", True, (255,255,255))
                        win.blit(num, (249, 75))
                        time += 1 
                else:
                    respawn = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        lose = True
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (m1, m2) = pygame.mouse.get_pos()
                        if m1 > 425 and m2 < 22:
                            RESTART()

                pygame.display.update()
            
            # Lo que pasa cuando jugamos normalmente
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        lose = True
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (m1, m2) = pygame.mouse.get_pos()
                        if m1 > 425 and m2 < 22:
                            RESTART()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            if paused == False:
                                paused = True
                            else:
                                paused = False
        
                keys = pygame.key.get_pressed()
                if paused == False:
                    if keys[pygame.K_RIGHT]:
                        if direccion != "LEFT":
                            direccion = "RIGHT"
                            cabezaX += vel
                    elif keys[pygame.K_LEFT]:
                        if direccion != "RIGHT":
                            direccion = "LEFT"
                            cabezaX -= vel
                    elif keys[pygame.K_UP]:
                        if direccion != "DOWN":
                            direccion = "UP"
                            cabezaY -= vel
                    elif keys[pygame.K_DOWN]:
                        if direccion != "UP":
                            direccion = "DOWN"
                            cabezaY += vel

                # Dibujamos los cambios

                win.fill((0,0,0))

                for pixel in serpiente:
                    pygame.draw.rect(win, (255,0,0), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

                pygame.draw.rect(win, (255,233,0), (x, y, anchoDePixel, altoDePixel))

                restart = font2.render("RESTART", True, (255,255,255))
                win.blit(restart, (425, 0))
                ptstext = font2.render("SCORE   " + point, True, (255,255,255))
                win.blit(ptstext, (385, 20))               

                if paused == False:
                    moverserpiente(direccion,serpiente)

                pygame.display.update()

        #Esto es lo que pasa cuando pierdes
        animacionchida()
        win.blit(deathmsg, (78,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    (m1, m2) = pygame.mouse.get_pos()
                    if m1 > 425 and m2 < 22:
                        RESTART()


    pygame.quit()

'''Ejecutar el juego'''
main()