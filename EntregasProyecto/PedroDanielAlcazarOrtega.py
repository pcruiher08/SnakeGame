'Importación de librerias'
import pygame
import random

'Configuracion de la pantalla'
pygame.init()
pantalla = pygame.display.set_mode((500,500))
pygame.display.update ()
pygame.display.set_caption('SnakeGame')

'Configuracion del juego'
pixel = 10 #Es la medida de los pixeles que usaremos en el juego (Manzana, cuerpo de serpiente)
Pantalla = 500
cabezaX = round(random.randint(10,200)/10) *10 #Es la localizacion
cabezaY = round(random.randint(10,450)/10) *10 #Es la localizacion
x_cambio = 10 # Variable que cambiará para que se mueva en el eje x
y_cambio = 0  # Variable que cambiará para que se mueva en el eje y
manzanaX = round(random.randint(10,430)/10)*10
manzanaY = round(random.randint(10,430)/10)*10
Serpiente = []
Long_serpiente = 1
texto = pygame.font.SysFont("arial", 22)
pausa = False


' Funcion para el SCORE '
def Puntos(score):
    if score < 20:
        puntos = texto.render("Puntos:", True, (255,255,0))
        pantalla.blit(puntos, [0,475])

    if score >= 20:
        puntos = texto.render("Puntos: " + str(score), True, (255,255,0))
        pantalla.blit(puntos, [0,475])

' funcion para agranddar serpiente'
def main_serpiente (pixel, Serpiente):
    for x in Serpiente:
        pygame.draw.rect(pantalla, (57,255,20), [x[0], x[1], pixel,pixel])

'Loop del Juego'
Game_over=False
clock = pygame.time.Clock()


def GameLoop ():
    global Game_over
    global cabezaX
    global cabezaY
    global x_cambio
    global y_cambio
    global manzanaX
    global manzanaY
    global Serpiente
    global Long_serpiente
    global texto
    global pausa


    while not Game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x_cambio <= 0 and pausa is False:
                        x_cambio=-pixel
                        y_cambio=0
                if event.key == pygame.K_RIGHT:
                    if x_cambio >= 0  and pausa is False:
                        x_cambio= pixel
                        y_cambio=0

                if event.key == pygame.K_UP:
                    if y_cambio <= 0  and pausa is False:
                        x_cambio=0
                        y_cambio=-pixel

                if event.key == pygame.K_DOWN:
                    if y_cambio >= 0  and pausa is False:
                        x_cambio= 0
                        y_cambio= pixel
                if event.key == pygame.K_p:
                    if pausa is False:
                        pausa= True
                    else:
                        pausa = False   

        if pausa is False:
            cabezaX += x_cambio
            cabezaY += y_cambio
            pantalla.fill((0,0,0))
        # AREA DE BOTON DE REINICIO  #
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 400+100 > mouse [0] > 400 and 480+25 > mouse [1] > 480:
                pygame.draw.rect(pantalla,(0,0,255), (400,480,100,25))
                if click [0] == 1:
                    Serpiente =[]
                    cabezaX = round(random.randint(10,200)/10) *10 #Es la localizacion
                    cabezaY = round(random.randint(10,440)/10) *10 #Es la localizacion
                    x_cambio = 10 # Variable que cambiará para que se mueva en el eje x
                    y_cambio = 0  # Variable que cambiará para que se mueva en el eje y
                    manzanaX = round(random.randint(10,430)/10)*10
                    manzanaY = round(random.randint(10,430)/10)*10
                    Long_serpiente = 1
                    
            else:
                pygame.draw.rect(pantalla,(173,216,230), (400,480,100,25))

            font3 = pygame.font.Font(None, 20)
            text3 = font3.render("REINICIAR", True, (0,0,0))
            text_rect2 = text3.get_rect(center=(450,490))
            pantalla.blit(text3, text_rect2)
            pygame.display.update()

            # TERMINA AREA DE BOTON #
            # AREA DE CRECIMIENTO DE SERPIENTE

            pygame.draw.rect(pantalla,(57,255,20), (cabezaX,cabezaY, pixel, pixel)) #Serpiente
            pygame.draw.rect(pantalla,(255,40,0), (manzanaX,manzanaY, pixel, pixel)) #Manzanas
            pygame.draw.rect(pantalla,(227,0,82), (0, 460, 500,10)) # Pared Inferior
            
            cabeza = []
            cabeza.append (cabezaX)
            cabeza.append (cabezaY)
            Serpiente.append(cabeza)

            if len(Serpiente) > Long_serpiente :
                del Serpiente [0]
            
            for x in Serpiente [:-1]:
                if x == cabeza:
                    Game_over = True

            main_serpiente (pixel, Serpiente)
            Puntos (len(Serpiente * 10))
            
            pygame.display.update()

            if cabezaX == manzanaX and cabezaY == manzanaY:
                manzanaX = round(random.randint(10,450)/10)*10
                manzanaY = round(random.randint(10,450)/10)*10
                Long_serpiente += 1


            'Colision Serpiente pared'
            if cabezaX >= 500 or cabezaX < 0 or cabezaY >= 460 or cabezaY < 0:
                Game_over = True

            clock.tick(20)
        




GameLoop()

# AREA DE GAME OVER #
while Game_over:
    pantalla.fill((244,244,244))
    font = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text = font.render("GAME OVER !", True, (0,0,0))
    text_rect = text.get_rect(center=(250,250))
    pantalla.blit(text, text_rect)
    text2 = font2.render("Presiona R para reiniciar", True, (0,143,57))
    text_rect = text.get_rect(center=(250,490))
    pantalla.blit(text2, text_rect)
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Game_over = False
                Serpiente =[]
                cabezaX = round(random.randint(10,200)/10) *10 #Es la localizacion
                cabezaY = round(random.randint(10,440)/10) *10 #Es la localizacion
                x_cambio = 10 # Variable que cambiará para que se mueva en el eje x
                y_cambio = 0  # Variable que cambiará para que se mueva en el eje y
                manzanaX = round(random.randint(10,430)/10)*10
                manzanaY = round(random.randint(10,430)/10)*10
                Long_serpiente = 1
                GameLoop()
