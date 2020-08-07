import pygame
import pygame.freetype 
import random
pantalla = 500
activo = True #juego
echele = True #pause
actividad =  True #main
file = r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\cancion.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

def main(activo,pantalla,echele,actividad):

    menu = pygame.image.load(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\menu.jpg")
    menu = pygame.transform.scale(menu, (500,500))
    pygame.init()
    screen = pygame.display.set_mode((pantalla,pantalla))
    pygame.display.set_caption("Snake")
    inst = pygame.freetype.Font(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\PlayMeGames-Demo.otf ", 20)
    text_surface, rect = inst.render("Presiona P para pausar el juego", (0, 0, 0))


    while actividad:
        pygame.time.delay(100)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actividad = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 143 and pos[0] < 431 and pos[1] > 318 and pos[1] < 431:
                    juego(activo, pantalla, screen, echele, actividad)
            
        screen.blit(menu, (0,0))
        screen.blit(text_surface, (60, 470))
        pygame.display.update()
        

def paus(screen):

    paused = True

    while paused:
        GAME_FONT = pygame.freetype.Font(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\PlayMeGames-Demo.otf ", 40)
        GAME_FONT1 = pygame.freetype.Font(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\PlayMeGames-Demo.otf ", 25)
        text_surface, rect = GAME_FONT.render("P A U S A", (0, 0, 0))
        text_surface1, rect = GAME_FONT1.render("Presiona C para continuar", (0, 0, 0))
        screen.blit(text_surface, (140, 140))
        screen.blit(text_surface1, (60, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    paused = False

def gameover(screen):

    over = True
    while over:
        GAME_FONT = pygame.freetype.Font(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\PlayMeGames-Demo.otf ", 30)
        GAME_FONT1 = pygame.freetype.Font(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\PlayMeGames-Demo.otf ", 25)
        text_surface, rect = GAME_FONT.render("G A M E O V E R", (255, 0, 0))
        text_surface1, rect = GAME_FONT1.render("Presiona ESPACIO para salir", (255, 0, 0))
        screen.blit(text_surface, (120, 140))
        screen.blit(text_surface1, (50, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    over = False

def juego(activo,pantalla,screen, echele, actividad):

    cabezaX = 20
    cabezaY = 20
    desplaz = 20
    snake=[(cabezaX, cabezaY)]
    cuersnake=snake[1:]
    indi=3
    check=False
    check1=False
    manzX=random.randint(15,pantalla-20)
    manzY=random.randint(15,pantalla-20)
    manzana=(manzX, manzY)
    marcador = 0 
    
    

    screen = pygame.display.set_mode((pantalla,pantalla))
    pygame.display.set_caption("Snake")
    img = pygame.image.load(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\tierra.png")
    comida = pygame.image.load(r"C:\Users\damol\OneDrive\Imágenes\Escritorio\Verano2020\Progra\Prgrma_Hub\Desarrollo de juego\manzana.jpg.png")
    comida = pygame.transform.scale(comida, (30,30))
    letra = pygame.font.Font('freesansbold.ttf', 32)
    texto = letra.render("Puntuación : " + str(marcador), True ,(0,0,0), (255,0,0))

    while activo:
        pygame.time.delay(100)

        if echele == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    activo = False
                elif event.type == pygame.K_p:
                    pause()

            while manzX % 20 != 0 or manzY % 20 != 0:
                if manzX%20 != 0:
                    manzX += 1
                if manzY%20 != 0:
                    manzY += 1
                manzana=(manzX, manzY)
        
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_UP]:
                cabezaY -= desplaz
                indi=1
            elif keys[pygame.K_DOWN]:
                cabezaY += desplaz
                indi=2
            elif keys[pygame.K_RIGHT]:
                cabezaX += desplaz
                indi=3
            elif keys[pygame.K_LEFT]:
                cabezaX -= desplaz
                indi=4
            elif keys[pygame.K_p]:
                paus(screen)
                
                      
        
            

            cuersnake= snake[1:]
    
            if snake[0][0]== pantalla or snake[0][0] == 0 or snake[0][1]== pantalla or snake[0][1]==0 :
                gameover(screen)
                actividad =False
                activo=False

            if snake[0] in cuersnake:
                gameover(screen)
                activo=False
                actividad=False
        

            movim(snake,desplaz,indi)
            screen.blit(comida, (40,40))
            screen.fill((0,0,0))
            screen.blit(img, (0,0))
            screen.blit(texto, (0,0)) 
            pygame.draw.rect(screen, (255,0,0),(manzX+7, manzY+3,10,10))
            screen.blit(comida, manzana)

            if snake[0] == manzana:
                pygame.time.delay(100)
                marcador += 1
                manzX=random.randint(1,pantalla-15)
                manzY=random.randint(1,pantalla-15)
                snake.append((cabezaX,cabezaY))
                letra = pygame.font.Font('freesansbold.ttf', 32) 
                texto = letra.render("Puntuación : " + str(marcador), True ,(0,0,0), (255,0,0))

            for pix in snake:
                pygame.draw.rect(screen,(0,255,0),(pix[0],pix[1],20,20))
            pygame.display.update()

            

    
        pygame.display.update()



def movim(snake, desplaz,indi):
    ncabx= snake[0][0]
    ncaby= snake[0][1]
    snake.pop()
    if indi==1:
        ncaby -= desplaz
    elif indi==2:
        ncaby += desplaz
    elif indi==3:
        ncabx += desplaz
    elif indi==4:
        ncabx -= desplaz
    snake.insert(0,(ncabx,ncaby))



    
main(activo,pantalla,echele,actividad)