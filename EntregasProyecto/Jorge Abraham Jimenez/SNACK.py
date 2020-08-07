# PYGAME

#soluciones
#hooked on swing xd

#formula gral para cuadratica
#import math as m -> al inicio para acortar math en funciones posicion[1] variables de libreria
#format posicion[1] .2f para dejar dos decimales despues del punto
#ejemplo: print(format(lado*0.86,'.2f'))
#sen60 * lado para la altura

#import platform -> para return platform.system()
#->nos da 'Windows'

#from matplotlib import pyplot as plt -> para histogrma
#import numpy as np
#numpy.array -> para el array
#pyplot.hist,pyplot.title para letra (variable del array) posicion[1] array (divisiones de datos), posicion[1] para nombre
#pyplot.show() -> al final
#abre otra ventana con el histograma


#PYGAME

#INSTALAR PIP
#programa para descargar librerias de internet
#
#
#
#
#

#INSTALAR PYGAME
#pip install pygame xd
#
#
#
#
#


#PROGRAMA PYGAME
#ventana -> (+)
#        |
#        v  
#        (+)
#
#main() -> se declara esta funcion para incluir funcionalidad principal del juego
#
#pygame.init() -> para iniciar el juego se llama esta funcion la cual despliega todos los modulos
#pygame.display -> controla la ventana, se crea posicion[1] se modifica
#pygame.display.set_mode((ancho,altura))
#pygame.event -> eventos dentro del juego (cuando el usuario da click o teclea)
#


import pygame
import pygame.freetype
import time
import random

#colorines
rojo=(255,125,0)
blanco=(255,255,255)
negro=(0,0,0)
azul=(0,0,255)
verde=(0,255,0)
gris=(100,100,100)
sky=(0,125,255)
colorend=(255,0,160)

screensize=500 #tamaño de pantalla
margen=20      #margen de pantalla para imagenes posicion[1] titulo
tamaño_imagen=[50,50]   #tamaño de imagenes
tamaño_titulo=[300,100] #tamaño de imagen de titulo de juego

def main():

    corriendo4=True

    while corriendo4:
        
        #ctes para posicion de imagenes
        posicion=[screensize/2,screensize/2]
        pos_imagen=[(((screensize/2))-(tamaño_titulo[0]/2))+10,margen+10]
        pos_fire1=[margen,screensize-margen-tamaño_imagen[1]]
        pos_fire2=[screensize-margen-tamaño_imagen[0],screensize-margen-tamaño_imagen[1]]
        pos_skull1=[margen,screensize-margen-(tamaño_imagen[1]*2)]
        pos_skull2=[screensize-20-50,screensize-margen-(tamaño_imagen[1]*2)]
        pos_fire1black=[margen,screensize-margen-tamaño_imagen[1]]
        pos_fire2black=[screensize-margen-tamaño_imagen[0],screensize-margen-tamaño_imagen[1]]
        pos_fire1blackup=[margen,margen]
        pos_fire2blackup=[screensize-margen-tamaño_imagen[0],margen]

        velocidad=3
        sizesnake=10
        loops=-1 #infinte loop music

        xchange=3
        ychange=0
        lastkey='right'

        food=[round(random.randrange(0,screensize-sizesnake-sizesnake)),round(random.randrange(0,screensize-sizesnake-sizesnake))]


        sumapuntaje=0

        pygame.init()
        pygame.display.set_caption('snek: of the underworld pt.1')
        pantalla=pygame.display.set_mode((screensize,screensize))

        def our_snake(sizesnake,snake_list):
            for w in snake_list:
                pygame.draw.rect(pantalla,blanco,[round(w[0]),round(w[1]),sizesnake,sizesnake])
                


        GAME_FONT = pygame.freetype.Font("8-Bit Madness.ttf", 48)
        PUNTAJE = pygame.freetype.Font("8-Bit Madness.ttf", 24)
        Image = pygame.image.load("snek.png").convert()
        fireuno = pygame.image.load("fire1.png").convert()
        firedos = pygame.image.load("fire2.png").convert()
        firetres = pygame.image.load("fire3.png").convert()
        fires=[fireuno,firedos,firetres]
        skulls=[pygame.image.load("skull1.png",).convert(),pygame.image.load("skull2.png").convert(),pygame.image.load("skull3.png").convert(),pygame.image.load("skull4.png").convert()]
        fireunoblack = pygame.image.load("fire1black.png").convert()
        firedosblack = pygame.image.load("fire2black.png").convert()
        firetresblack = pygame.image.load("fire3black.png").convert()
        firesblack=[fireunoblack,firedosblack,firetresblack]

        def paused():
            pause=True
            while pause:
                pygame.time.delay(20)
                GAME_FONT.render_to(pantalla, (180, 200), "paused",sky)
                GAME_FONT.render_to(pantalla, (60, 300), "press y to continue",sky)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()

                teclas=pygame.key.get_pressed() #teclas es una lista del teclado
                if teclas[pygame.K_y]:
                    pause=False

        pygame.mixer.init()
        pygame.mixer.music.load('ACIDDANCE.wav')
        pygame.mixer.music.play(loops)

        effect = pygame.mixer.Sound('points!.wav')
        effect2=pygame.mixer.Sound('points3.wav')

        corriendo1=True #para menu posicion[1] para juego
        corriendo2=True
        corriendo3=True
        i=0
        time=0
        current=0
        time2=0
        current2=0
        j=0
        snake_list=[]
        lengthofsnake=1
        timeover=0
        timegame=0
        currentgame=0
        m=0
        r=0
       

        while corriendo1:
            pygame.time.delay(20)
            time+=20
            time2+=20
            for event in pygame.event.get():
                if event.type==pygame.QUIT: 
                    pygame.quit()
                    quit()
                                    
            teclas=pygame.key.get_pressed() 
            if teclas[pygame.K_y]:
                corriendo1=False
                corriendo2=True

            if teclas[pygame.K_n]:
                pygame.quit()
                quit()

            pantalla.fill((255,255,255))

            pantalla.blit(Image, ( round(pos_imagen[0]),round(pos_imagen[1]))) # paint to screen


            pantalla.blit(fires[i], ( pos_fire1[0],pos_fire1[1])) # paint to screen
            pantalla.blit(fires[i], ( pos_fire2[0],pos_fire2[1])) # paint to screen
            if (time-current) >= 250:
                i+=1
                current=time
            if i==3:
                i=0

            pantalla.blit(skulls[j], ( pos_skull1[0],pos_skull1[1])) # paint to screen
            pantalla.blit(skulls[j], ( pos_skull2[0],pos_skull2[1])) 
            if (time2-current2) >= 400:
                j+=1
                current2=time2
            if j==4:
                j=0          

            GAME_FONT.render_to(pantalla, (120, 200), "start game = y",sky)
            GAME_FONT.render_to(pantalla, (120, 250), "quit game = n",negro)

            pygame.display.flip()


        while corriendo2:
            pygame.time.delay(20)
            timegame+=20

            for event in pygame.event.get():
                if event.type==pygame.QUIT: #tipos de eventos!
                    corriendo2=False
                    corriendo3=False
                    corriendo4=False
                                    #R  G  B posicion,ancho,altura
            
            teclas=pygame.key.get_pressed() #teclas es una lista del teclado
            if teclas[pygame.K_LEFT] and lastkey!='right':
                xchange=-velocidad
                ychange=0
                lastkey='left'
            if teclas[pygame.K_RIGHT] and lastkey!='left':
                xchange=velocidad
                ychange=0
                lastkey='right'
            if teclas[pygame.K_UP] and lastkey!='down':
                ychange=-velocidad
                xchange=0
                lastkey='up'
            if teclas[pygame.K_DOWN] and lastkey!='up':
                ychange=velocidad
                xchange=0
                lastkey='down'

            if teclas[pygame.K_ESCAPE]:
                corriendo2=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    paused()

            if posicion[0] >= (screensize-sizesnake) or posicion[0] < 0 or posicion[1] >= (screensize-sizesnake) or posicion[1] < 0:
                corriendo2=False

            posicion[0]+=xchange
            posicion[1]+=ychange

            pantalla.fill(negro)
            pantalla.blit(firesblack[m], ( pos_fire1black[0],pos_fire1black[1])) # paint to screen
            pantalla.blit(firesblack[m], ( pos_fire2black[0],pos_fire2black[1])) # paint to screen
            pantalla.blit(firesblack[m], ( pos_fire1blackup[0],pos_fire1blackup[1])) # paint to screen
            pantalla.blit(firesblack[m], ( pos_fire2blackup[0],pos_fire2blackup[1])) # paint to screen
            if (timegame-currentgame) >= 250:
                m+=1
                currentgame=timegame
            if m==3:
                m=0
            pygame.draw.rect(pantalla,sky,(food[0],food[1],sizesnake,sizesnake))
            
            """pygame.draw.rect(pantalla,(0,0,0),(posicion[0],posicion[1],sizesnake,sizesnake))"""
            #hacer fuegos para game, cabeza snake, png para end

            snake_head=[]
            snake_head.append(posicion[0])
            snake_head.append(posicion[1])
            snake_list.append(snake_head)
            if len(snake_list) > lengthofsnake:
                del snake_list[0]

            for w in snake_list[:-1]: 
                if w == snake_head:
                    corriendo2:False 

            our_snake(sizesnake,snake_list)

            pygame.display.update()

            if (posicion[0]+(sizesnake/2))>=(food[0]-5) and (posicion[0]+(sizesnake/2))<=(food[0]+sizesnake+5) and  (posicion[1]+(sizesnake/2))>=(food[1]-5) and (posicion[1]+(sizesnake/2))<=(food[1]+sizesnake+5):
                
                food=[round(random.randrange(0,screensize-sizesnake-sizesnake)),round(random.randrange(0,screensize-sizesnake-sizesnake))]

                velocidad+=(1/5)
                lengthofsnake+=1
                sumapuntaje+=1
                effect.play()
                effect2.play()

            PUNTAJE.render_to(pantalla, (10, 10), str(sumapuntaje), rojo)
            PUNTAJE.render_to(pantalla, (screensize-210, 10),'p = pause, esc = quit', gris)
            pygame.display.flip()

        while corriendo3:

            pygame.time.delay(20)
            timeover+=20

            for event in pygame.event.get():
                if event.type==pygame.QUIT: #tipos de eventos!
                    corriendo3=False   
                    corriendo4=False     

            if (timeover)<999:
                pantalla.fill(negro)
                GAME_FONT.render_to(pantalla, (110, 160), "GAME__OVER_", blanco)
                GAME_FONT.render_to(pantalla, (90, 290), "return 2 menu = n", sky)
                GAME_FONT.render_to(pantalla, (120, 330), "quit game = y", blanco)
                pygame.display.flip()
            elif (timeover)>999 and timeover<2000:
                pantalla.fill(blanco)
                GAME_FONT.render_to(pantalla, (110, 160), "GAME__OVER_", negro)
                GAME_FONT.render_to(pantalla, (90, 290), "return 2 menu = n", sky)
                GAME_FONT.render_to(pantalla, (120, 330), "quit game = y", negro)
                pygame.display.flip()
            elif (timeover)==2000:
                timeover=0

            GAME_FONT.render_to(pantalla, (margen, r), 'ur score = '+ str(sumapuntaje), colorend)
            pygame.display.flip()
            if r<(screensize):
                r+=2
            else:
                r=0

            teclas=pygame.key.get_pressed() #teclas es una lista del teclado
            if teclas[pygame.K_y]:
                corriendo3=False
                corriendo4=False

            if teclas[pygame.K_n]:
                corriendo3=False
                corriendo4=True

main()












