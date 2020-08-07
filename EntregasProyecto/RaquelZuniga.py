import pygame
import time
import random
 
pygame.init()

# INICIAN DETALLES DE PANTALLA Y CONFIGURACIÓN  
# Colores
yellow = (255, 255, 102) # Color puntaje y comida
black = (0, 0, 0) # Color de serpiente
red = (213, 50, 80) # Color mensaje Game Over
purple = (157, 0, 255) # Color de pantalla

# Misc para diseño pantalla
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 35)
 
# Tamaño de ventana
screen_width = 500
screen_height = 500

# Detalles de ventana 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake - MPH')
 
clock = pygame.time.Clock()
 
snake_block = 10 # Tamaño de cada bloque de la serpiente
snake_speed = 15 # Velocidad de FPS

# Actualizar el resultado 
def updateScore(score):
    value = score_font.render("Puntos: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# Actualizar dibujo de la serpiente en pantalla
def drawSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
 
# Ventana de mensaje 
def quitMessage(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [10, 50])
        
# Método de juego principal 
def game():
    game_over = False
    game_close = False
 
    # Cambio de dirección
    x1_change = 0
    y1_change = 0
 
    snake_list = []
    snake_length = 1

    # Posición inicial de la serpiente es random
    x1 = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    y1 = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
 
    # Posición aleatoria de la comida
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Generar dirección inicial aleatoria
    initial_direction = random.randint(1,4)
    if initial_direction == 1:
        x1_change = -snake_block
        y1_change = 0
        direction = "left"
    elif initial_direction == 2:
        x1_change = snake_block
        y1_change = 0
        direction = "right"
    elif initial_direction == 3:
        y1_change = -snake_block
        x1_change = 0
        direction = "up"
    elif initial_direction == 4:
        y1_change = snake_block
        x1_change = 0
        direction = "down"
 
    while not game_over:
 
        while game_close == True:
            screen.fill(purple)
            quitMessage("¡Perdiste! R para empezar de nuevo o C para cerrar.", red)
            updateScore(snake_length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: # Cierra pantalla
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r: # Reinicia el juego
                        game()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Fin del juego
                game_over = True
            if event.type == pygame.KEYDOWN: # Movimiento en 4 direcciones
                if event.key == pygame.K_LEFT and direction != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    y1_change = snake_block
                    x1_change = 0
                    direction = "down"
                # elif event.key == pygame.K_p: # Pausa
                    # pauseGame()
 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0: # Choque de paredes
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(purple)
        pygame.draw.rect(screen, yellow, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
 
        drawSnake(snake_block, snake_list) # Actualiza el largo de la serpiente
        updateScore(snake_length - 1) # Actualiza el puntaje
 
        pygame.display.update()
 
        if x1 == food_x and y1 == food_y: # Posición coincide con la del random de la comida
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
game()