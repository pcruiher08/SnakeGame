'''Importación de librerías'''
import pygame
import time
import random

pygame.init()

'''Configuración del juego'''
SCREENSIZE = 500

bloque = 10


direccion = "DERECHA" #con esta variable se controla que la serpiente no se mueva a la derecha
velocidad = 7

win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE)) #se crea la pantalla
pygame.display.set_caption("Viborita")
clock = pygame.time.Clock() #controla la rapidez del juego usando la variable velocidad
estilo_fuente = pygame.font.SysFont("bahnschrift", 25)

# Paleta de Colores

blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

#Funcion para mensajes 
def mensaje(msg, color, pos):
    mesg = estilo_fuente.render(msg, True, color)
    win.blit(mesg, [SCREENSIZE / 6, (SCREENSIZE / 4)*pos])
 
#Funcion para pausar el juego
def jpausado():
    global pausa                    
    
    while pausa:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausa = False
                    
            
    
    
                    

    

'''Definición de la función principal del juego'''
def main():

    global mensaje
    global SCREENSIZE
    
 
 
   

    global direccion
    limite = 1

    #coordenadas aleatorias de la comida
    comidax= round(random.randrange(0, SCREENSIZE - bloque) / 10.0) * 10 
    comiday= round(random.randrange(0, SCREENSIZE - bloque) / 10.0) * 10
   
    '''Ciclo de vida del juego'''
    #coordenadas de inicio
    x1 = SCREENSIZE/2
    y1 = SCREENSIZE/2
    cambioX = 10 #para que empiece moviendose
    
    cambioY = 0
    #lista del cuerpo principal de la serpiente
    serpiente = []
    
    global pausa 
    pausa = False
    cerrarjuego = False
    gameover = False
    while not gameover: 
        global direccion
       
        while cerrarjuego == True:
            #menu principal al acabar el juego
            win.fill(negro)
            mensaje("GAME OVER!", rojo,1)
            mensaje("Presiona R para jugar de nuevo", verde , 2)
            mensaje("Presiona S para salir del juego", verde , 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameover = True
                        cerrarjuego = False
                    if event.key == pygame.K_r:
                        main()
                  
                             
                
                elif event.type == pygame.QUIT:
                    gameover = True
                    cerrarjuego = False
        #manipulación de la dirección de la serpiente mediante las teclas de dirección    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direccion != "DERECHA":
                    cambioX = -bloque
                    cambioY = 0
                    direccion = "IZQUIERDA"
                elif event.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                    cambioX = bloque
                    cambioY = 0
                    direccion = "DERECHA"
                elif event.key == pygame.K_UP and direccion != "ABAJO":
                    cambioY = -bloque
                    cambioX = 0
                    direccion = "ARRIBA"
                elif event.key == pygame.K_DOWN and direccion != "ARRIBA":
                    cambioY = bloque
                    cambioX = 0
                    direccion = "ABAJO"
                elif event.key == pygame.K_p:  #pausa cuando se oprime la tecla p y llama a la función de pausa
                    pausa = True
                    win.fill(negro)
                    mensaje("JUEGO PAUSADO!", amarillo,1)
                    mensaje("Presiona P de nuevo para seguir jugando", verde , 2)
                    mensaje("Presiona S para salir del juego", rojo , 3) 
                    pygame.display.update()
                    jpausado()
                    
                  
                    
        # colisión contra paredes 
        if x1 >= SCREENSIZE or x1 < 0 or y1 >= SCREENSIZE or y1 < 0:  
            cerrarjuego = True

        #coordenadas de cambio de dirección
        x1 += cambioX
        y1 += cambioY
         
        win.fill(negro)
        #dibuja el primer cuadro de comida
        pygame.draw.rect(win, verde, [comidax, comiday, bloque, bloque]) 
        
       
        #cabeza de serpiente 
        cabeza = []
        cabeza.append(x1)
        cabeza.append(y1)
        #se añade cabeza al cuerpo
        serpiente.append(cabeza)
   
   
        #borra el rastro que deja la serpiente al irse moviendo, y de esta manera regula el crecimiento de la serpiente
        if len(serpiente) > limite:
            del serpiente[0]
        
        # colisión contra si misma, aqui me quede con duda acerca de una serpiente muy grande que se enrolle sobre si misma 
        for x in serpiente[:-1]: 
            if x == cabeza:
                cerrarjuego = True

               
       
        #Aqui se dibuja la serpiente
        for pixel in serpiente:
            pygame.draw.rect(win, rojo, (pixel[0],pixel[1], bloque,bloque))
        pygame.display.update()
        #Si las coordenadas de la cabeza y la comida coinciden, hace aparecer en otro lado la comida e incrementa el límite de crecimiento en una unidad
        if comidax == x1 and comiday == y1: 
            
            comidax= round(random.randrange(0, SCREENSIZE - bloque) / 10.0) * 10 
            comiday= round(random.randrange(0, SCREENSIZE - bloque) / 10.0) * 10
            limite += 1
        clock.tick(velocidad)

    pygame.quit()
    quit()

'''Ejecutar el juego'''
main()