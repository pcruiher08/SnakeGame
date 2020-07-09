import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("SnakeGame")

x = 50
y = 50
width = 5
height = 5
vel = 5
snakeSize = 1

run = True

while run: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (x,y,width, height))
    pygame.display.update()

pygame.quit()