import pygame, random, time

running = True
cabezaX = 50
cabezaY = 50
vel = 10
direccion = "DERECHA"
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)
food_position=(random.randrange(0,500,10)),(random.randrange(0,500,10))
move_food=True
area=(10,10)
score=0
serpiente = [(cabezaX,cabezaY)]

def moverSerpiente(direccion, serpiente):
    global vel
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

def main():
    global running
    global cabezaX
    global cabezaY
    global serpiente
    global vel
    global direccion
    global move_food
    global food_position
    global score

    pygame.init()
    pantalla = pygame.display.set_mode((500,500))
    pygame.display.set_caption("SnakeGame by Alvaro")

    while running: 
        pygame.time.delay(100)
        
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
           
        pantalla.fill(yellow)
        moverSerpiente(direccion,serpiente)
        food=pygame.draw.rect(pantalla,blue,(food_position[0],food_position[1],area[0],area[1]))

        if  serpiente[0][0]==food_position[0] and serpiente[0][1]==food_position[1] :
            serpiente.append((50,50))
            score+=10
            move_food=False

        if not move_food:
            food_position=(random.randrange(0,500,10)),(random.randrange(0,500,10))
        move_food=True

        for pixel in serpiente:
            pygame.draw.rect(pantalla, (red), (pixel[0],pixel[1],area[0],area[1]))

        if serpiente[0][0]<=0 or serpiente[0][0]>=500 or serpiente[0][1]<=0 or serpiente[0][1]>=500:
            font2 = pygame.font.SysFont("Arial", 50)
            image2 = font2.render("Game Over", True, red)
            pantalla.blit(image2, (150, 200))
            font = pygame.font.SysFont("Arial", 30)
            image = font.render(str(score), True, green)
            pantalla.blit(image, (280, 280))
            font3 = pygame.font.SysFont("Arial", 30)
            image3 = font3.render("score: ", True, green)
            pantalla.blit(image3, (200, 280))
            pygame.display.flip()
            pygame.time.delay(4000)     
            running = False
            print("Your last score was: ",score)

        for block in serpiente[1: ]:
            if serpiente[0][0]==block[0] and serpiente[0][1]==block[1]:
                font2 = pygame.font.SysFont("Arial", 50)
                image2 = font2.render("Game Over", True, red)
                pantalla.blit(image2, (150, 200))
                font = pygame.font.SysFont("Arial", 30)
                image = font.render(str(score), True, green)
                pantalla.blit(image, (280, 280))
                font3 = pygame.font.SysFont("Arial", 30)
                image3 = font3.render("score: ", True, green)
                pantalla.blit(image3, (200, 280))
                pygame.display.flip()
                pygame.time.delay(4000)
                running=False
                print("Your last score was: ",score)
                    
        font = pygame.font.SysFont("Arial", 20)
        image = font.render(str(score), True, green)
        pantalla.blit(image, (10, 10))

        food=pygame.draw.rect(pantalla,blue,(food_position[0],food_position[1],area[0],area[1]))
        pygame.display.update()

    pygame.quit()

main()