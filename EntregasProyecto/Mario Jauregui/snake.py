#Importación de librerias
import pygame
import random
import time
#Tamaño de la pantalla
SCREENSIZE = 500
#Dejar que el juego este corriendo
running = False
# posición de la fruta
n1 = random.randint(11,479)
n2 = random.randint(11,479) 
#posición inicial de la cabeza
cabezaX = 50
cabezaY = 50
#tamaño de las cosas
anchoDelPixel = 10
altoDelPixel = 10
#velocidad de la serpiente
velocidad = 10
#dirección inicial de serpiente
direccion = "DERECHA"
#valores para el cuerpo
colaX = 0
colaY = 0
#lista de la serpiente
serpienteOriginal = [(cabezaX,cabezaY)]
serpiente = serpienteOriginal
#tamaño de cuerpo y de frutas comidas
longitud = len(serpiente)
#para el movimiento
nuevaCabezaX = serpiente[0][0]
nuevaCabezaY = serpiente[0][1]
#Para el menu del comienzo
Start = True
#Para el la cantidad necesaria para ganar
cantidad_Frutas = 0
#Para las que lleva la serpiente comidas
FrutasComidas = 0
over = False
#Para poder hacer el game over
win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
#las teclas 
keys = pygame.key.get_pressed()
#COLORES
negro = (0,0,0)
blanco = (255,255,255)
#Funcion para mover serpiente
#direccion: dirrecion en la que se mueve la serpiente
#serpiente : arreglo de tuplas
def moverSerpiente(direccion,serpiente):
    global longitud
    global nuevaCabezaX
    global nuevaCabezaY
 

    serpiente.pop()
    
#movimiento de la serpiente
    if direccion == "ARRIBA":
        nuevaCabezaY -= velocidad
    elif direccion == "ABAJO":
        nuevaCabezaY += velocidad
    elif direccion == "DERECHA":
        nuevaCabezaX += velocidad
    elif direccion == "IZQUIERDA":
        nuevaCabezaX -= velocidad

#nueva cabeza
    serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))
  
    
    
    

#Dibuja todos los objetos
def dibujar(win):
    global anchoDelPixel
    global altoDelPixel
    global FrutasComidas
    
    #pone el fondo de color azul
    win.fill((0,0,255))     
    #te enseña el puntaje
    score = FrutasComidas * 100
    text(380,10,"Puntos: "+ str(score),18)  
#Nuestro jugador
    
    #Muro izquierdo
    pygame.draw.rect(win,(241,119,170),(0,0,10,500))
    #muro derecho
    pygame.draw.rect(win,(241,119,170),(490,0,10,500))
    #muro arriba
    pygame.draw.rect(win,(241,119,170),(0,0,500,10))
    #muro abajo
    pygame.draw.rect(win,(241,119,170),(0,490,500,10))



    pygame.display.update()




   
#Funcion que elimina la fruta
def EliminFrutas(win):
    global cabezaX
    global cabezaY
    global n1
    global n2
    global longitud
    global colaY
    global colaX
    global nuevaCabezaX
    global nuevaCabezaY
    global FrutasComidas
    
    #si la serpiente come frutas
    if serpiente[0][0] <= n1 + 8 and n1-8 <= serpiente[0][0] and serpiente[0][1] >= n2 -8 and n2 + 10 >= serpiente[0][1] :
        #mueve de lugar a la fruta
        
        n1 = random.randint(11,479)
        n2 = random.randint(11,479)
        if n1 in serpiente or n2 in serpiente:
            #para que no aparezca adentro de la serpiente
            n1 = random.randint(11,479)
            n2 = random.randint(11,479)
        
        #añade al cuerpo de manera correcta
        #revisar para arreglar
        if direccion == "ARRIBA":
           colaY -= velocidad
           serpiente.insert (longitud, (nuevaCabezaX,colaY))
        
        elif direccion == "ABAJO":
            colaY -= velocidad
            serpiente.insert (longitud, (nuevaCabezaX,colaY))
           
        elif direccion == "DERECHA":
            colaX -= velocidad
            serpiente.insert (longitud, (colaX,nuevaCabezaY))
            
        elif direccion == "IZQUIERDA":
            colaX -= velocidad
            serpiente.insert (longitud, (colaX,nuevaCabezaY))

        FrutasComidas +=1
        
        
        
    pygame.display.update()
# checa si choca contra algo
def Hitbox (serpiente):
    global running
    global longitud
    global win
    

    golpeIzq = serpiente [0][0] >= 0 and serpiente[0][0] <=10 

    golpeDer = serpiente [0][0] >= 480 and serpiente[0][0] <=500 

    golpeUp = serpiente [0][1] >= 0 and serpiente[0][1] <=10 

    golpeDown = serpiente [0][1] >= 480 and serpiente[0][1] <=500 
    #choque contra cualquier pared
    if  golpeIzq or golpeDer or golpeUp or golpeDown:
        GameOver(win)
    #golpe con el cuerpo
    if serpiente.count(serpiente[0])> 1:
        GameOver(win)
        


#ES LA PANTALLA DE PERDER
def GameOver(win):
    global running
    global keys
    global over
    imagen = pygame.image.load(r"D:\programacion\SnakeGame\EntregasProyecto\Mario Jauregui\GAME OVER.jpg")
    win.fill((0,0,0)) 
    
    win.blit(imagen,(100,150))
    
    pygame.display.update()
    
    running = False
    over = True

#pantalla de victoria
def Victoria(win):
    global running
    global over
    imagen = pygame.image.load(r"D:\programacion\SnakeGame\EntregasProyecto\Mario Jauregui\Victory.jpg")
    win.fill((47,65,85))
    win.blit (imagen,(0,100))
    pygame.display.update()

    over = True
    running = False
    
#necesario para generar textos

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
# textos

def text(positionX,positionY,texto,tamaño):
    global negro
    smallText = pygame.font.Font("freesansbold.ttf",tamaño)
    textSurf, textRect = text_objects(texto, smallText,negro)
    textRect.center = ( (positionX+(100/2)), (positionY+(50/2)) )
    win.blit(textSurf, textRect)
#menu del principio


def startMenu(win):
    global cantidad_Frutas
    global running
    global Start
    global FrutasComidas
    global serpiente
    
    
    
    FrutasComidas = 0
    

    #Título
    smallText = pygame.font.Font("freesansbold.ttf",50)
    textSurf, textRect = text_objects("Snake game", smallText,negro)
    textRect.center = ( (250), (50) )
    win.blit(textSurf, textRect)

    #instrucciones
    smallText = pygame.font.Font("freesansbold.ttf",25)
    textSurf, textRect = text_objects("Seleccione la cantidad de frutas", smallText,negro)
    textRect.center = ( (250), (170) )
    win.blit(textSurf, textRect)
#                                  """LISTA DE CUADROS PARA EL MENÚ"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #cuadro verde
    pygame.draw.rect(win,(0,255,0),(50,250,100,50))
    text(50,250,"5 Frutas",18)
    # if posicionX + largo ... posicion X and posicion Y + alto ... posicion Y
    if 50 + 100 > mouse [0]> 50 and 250 +50 > mouse [1]>250 and click[0] == 1:
        cantidad_Frutas = 5
        Start = False
        running = True  
    #cuadro amarillo
    pygame.draw.rect(win,(255,255,0),(350,250,100,50))
    text(350,250,"10 Frutas",18)
    if 350 + 100 > mouse [0]> 350 and 250 +50 > mouse [1]>250 and click[0] == 1:
        cantidad_Frutas = 10
        Start = False
        running = True 
    #cuadro naranja
    pygame.draw.rect(win,(255,128,0),(50,350,100,50))
    text(50,350,"20 Frutas",18)
    if 50 + 100 > mouse [0]> 50 and 350 +50 > mouse [1]>350 and click[0] == 1:
        cantidad_Frutas = 20
        Start = False
        running = True 
    #cuadro rojo
    pygame.draw.rect(win,(255,0,0),(350,350,100,50))
    text(350,350,"40 Frutas",18)
    if 350 + 100 > mouse [0]> 350 and 350 +50 > mouse [1]>350 and click[0] == 1:
        cantidad_Frutas = 40
        Start = False
        running = True 
    #cuadro azul clarito
    pygame.draw.rect(win,(0,255,255),(200,300,100,50))
    text(200,300,"Limitless",18)
    if 200 + 100 > mouse [0]> 200 and 300 +50 > mouse [1]>300 and click[0] == 1:
        cantidad_Frutas = 10000000
        Start = False
        running = True 

#corre el juego
def main():
    #Deja que las variables sean usadas dentro del programa
    global SCREENSIZE
    global running
    global cabezaX
    global cabezaY
    global anchoDelPixel
    global altoDelPixel
    global serpiente
    global velocidad
    global direccion
    global n1
    global n2
    global longitud
    global Start
    global cantidad_Frutas
    global FrutasComidas
    global over
    global blanco
    global nuevaCabezaX
    global nuevaCabezaY
    
    #Con lo que se empieza el juego
    pygame.init()
    #Con lo que se ve la ventana
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption("Snake Game")
    while Start:
        pygame.time.delay(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Start = False
        win.fill((255,255,255))
        nuevaCabezaX = 50
        nuevaCabezaY = 50
        direccion = "DERECHA"
        serpiente = [(nuevaCabezaX,nuevaCabezaY)]
        startMenu(win)
        pygame.display.update()
        
    #Ciclo de vida del juego
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
       
        
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_RIGHT]:
            if direccion != "IZQUIERDA" or len(serpiente)<=1:
                direccion = "DERECHA"
                
        elif keys[pygame.K_LEFT]:
             if direccion != "DERECHA"or len(serpiente)<=1:
                direccion = "IZQUIERDA"
        elif keys[pygame.K_UP]:
             if direccion != "ABAJO" or len(serpiente)<=1:
                direccion = "ARRIBA"
        elif keys[pygame.K_DOWN]:
             if direccion != "ARRIBA"or len(serpiente)<=1:
                direccion = "ABAJO"
        if keys[pygame.K_p]:
            over = True
            running = False
        
           

        
        
        #mueve la serpiente
        moverSerpiente(direccion,serpiente,)
        #dibuja los objetos
        dibujar(win)
        for pixel in serpiente:

            pygame.draw.rect(win, (255,255,0), (pixel[0],pixel[1], anchoDelPixel,altoDelPixel))
        #dibuja a las frutas
        frutaHitbox = (n1+1,n2+1,anchoDelPixel,altoDelPixel)
        pygame.draw.rect (win, (255,0,0), frutaHitbox)
        #cambia de posicion las frutas y alarga a la serpiente
        EliminFrutas(win)
        #lee si choca la serpiente contra si misma o las paredes
        Hitbox(serpiente)
        if len(serpiente) > cantidad_Frutas :
           Victoria(win)
    
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        score = FrutasComidas * 100
        #PUNTOS FINALES
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurf, textRect = text_objects("Puntaje: " + str(score)  , smallText,blanco)
        textRect.center = ((250), (100))
        win.blit(textSurf, textRect)
        #MENU
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurf, textRect = text_objects("MENU", smallText,blanco)
        textRect.center = ( (250), (350) )
        win.blit(textSurf, textRect)
        #QUIT
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurf, textRect = text_objects("QUIT", smallText,blanco)
        textRect.center = ( (250), (410) )
        win.blit(textSurf, textRect)
        if keys[pygame.K_p]:
            #continue
            smallText = pygame.font.Font("freesansbold.ttf",25)
            textSurf, textRect = text_objects("CONTINUE", smallText,blanco)
            textRect.center = ( (250), (230) )
            win.blit(textSurf, textRect)
        if click[0] == 1 and 200+100>mouse[0]>200 and 200+50 >mouse[1] >200:
            running = True
            over = False
            main()
            print("unpause")
       
        if click[0] == 1 and 200+100>mouse[0]>200 and 320+50 >mouse[1] >320 :
            Start = True
            over = False
            main()
        elif click [0] == 1 and 200+100>mouse[0]>200 and 380+50 >mouse[1] >380:
            over = False
        
        pygame.display.update()
          

  

    pygame.quit()

#Ejecuta el juego
main()