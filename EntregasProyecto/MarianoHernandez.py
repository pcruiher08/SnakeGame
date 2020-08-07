'''Importación de librerías'''
import pygame
import random

'''Configuración del juego'''
SCREENSIZE = 500
running = True
cabezaX = random.randint(50,450)
cabezaY = random.randint(50,450)
anchoDePixel = 10
altoDePixel = 10
vel = 10
direccion = "DERECHA"

serpiente = [(cabezaX,cabezaY)]


comidax=random.randint(1,490)
comiday=random.randint(1,490)

comidan=[(comidax,comiday)]

game_over=False



def derrotas():
    global game_over
    global serpiente
    longitud=len(serpiente)
    
    "Colision serpiente-serpiente"
    
    for i in range(1,longitud):
        if (serpiente[0])==(serpiente[i]):
            print("Derrota")
            game_over=True
    


    "Colision serpiente-pared"
    if (serpiente[0][0]<0) or (serpiente[0][0]>500):
        game_over=True
    if (serpiente[0][1]<0) or (serpiente[0][1]>500):
        game_over=True
    




def comer():
    global comidax
    global comiday
    global serpiente
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    global direccion
    aumentoserpiente=0


    difx=serpiente[0][0]-comidax
    dify=serpiente[0][1]-comiday
    if  (difx>-9 and difx<9)and(dify>-9 and dify<9):
        aumentoserpiente+=10
        comidax=random.randint(10,490)
        comiday=random.randint(10,490)
        pygame.draw.rect(win,(0,255,0),(comidax,comiday,anchoDePixel,altoDePixel))
        pygame.display.update()
        #print(dify, difx)
        if direccion=="DERECHA":
            serpiente.append((cabezaX-aumentoserpiente,cabezaY))
        if direccion=="IZQUIERDA":
            serpiente.append((cabezaX+aumentoserpiente,cabezaY))
        if direccion=="ARRIBA":
            serpiente.append((cabezaX,cabezaY-aumentoserpiente))
        if direccion=="ABAJO":
            serpiente.append((cabezaX,cabezaY+aumentoserpiente))
        
    
    

def moverSerpiente(direccion, serpiente):
    global vel
    global comidax
    global cabezaY
    
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
    global comidax
    global comiday

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
            if direccion!="IZQUIERDA":
                direccion = "DERECHA"
                cabezaX += vel
        elif keys[pygame.K_LEFT]:
            if direccion!="DERECHA":
                direccion = "IZQUIERDA"
                cabezaX -= vel
        elif keys[pygame.K_UP]:
            if direccion!="ABAJO":
                direccion = "ARRIBA"
                cabezaY -= vel
        elif keys[pygame.K_DOWN]:
            if direccion!="ARRIBA":
                direccion = "ABAJO"
                cabezaY += vel

        win.fill((0,0,0))
      

        

        moverSerpiente(direccion,serpiente)
        comer()
        

        for pixel in serpiente:
            pygame.draw.rect(win, (255,0,0), (pixel[0],pixel[1],anchoDePixel,altoDePixel))
            
    
            
        pygame.display.update()

        pygame.draw.rect(win,(0,255,0),(comidax,comiday,anchoDePixel,altoDePixel))
        pygame.display.update()

        derrotas()

        if game_over:
            #pygame.draw.rect(win,(255,255,255),(250,250,50,50))
            #pygame.display.update()
            running=False

    



        

    pygame.quit()
'''Ejecutar el juego'''

main()