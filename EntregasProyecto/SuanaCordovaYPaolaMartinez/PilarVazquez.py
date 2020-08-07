# Libraries
import pygame, random

# Colors
black=(0,0,0)
background=(231,197,130)
green=(77,228,145)
red=(255,38,78)

# Variables
running=True
pause=False
screenSize=500  
pixelSize=10
speed=10
direction="RIGHT"
game_over=False
pause=False
headX=50
headY=50
screen=pygame.display.set_mode((screenSize,screenSize))

snake=[(headX,headY)]


# Coordinates
randomX=random.randrange(50,450,10)
randomY=random.randrange(50,450,10)

snack=[(randomX,randomY)]

# Fuctions
def initialization():
    pygame.init()
    pygame.display.set_caption("Snake Game")

def checkEvents(events):
    global running

    for event in events:
        if event.type==pygame.QUIT:
            running=False

def drawSnake(screen,snake):
    global pixelSize
            
    for pixel in snake:
        pygame.draw.rect(screen,(green),(pixel[0],pixel[1],pixelSize,pixelSize))
        
def moveSnake(direction,snake):
    global speed
            
    newHeadX=snake[0][0]
    newHeadY=snake[0][1]
    snake.pop()
    if direction=="UP":
        newHeadY-=speed
    elif direction=="DOWN":
        newHeadY+=speed
    elif direction=="RIGHT":
        newHeadX+=speed
    elif direction=="LEFT":
        newHeadX-=speed
            
    snake.insert(0,(newHeadX,newHeadY))

def drawSnack(screen,snack):
    global pixelSize
    pygame.draw.rect(screen,(red),(snack[0][0],snack[0][1],pixelSize,pixelSize))

def Snake_Snack(snake,snack,screen):

    def addPixel(snake):
        newX=snake[0][0]
        newY=snake[0][1]
        snake.insert(0,(newX,newY))

    def redrawSnack(screen,snack):
        randomX=random.randrange(50,450,10)
        randomY=random.randrange(50,450,10)
        global pixelSize

        pygame.display.flip()
        
        snack.pop()
        
        snack.insert(0,(randomX,randomY))

    if snake[0]==snack[0]:
            addPixel(snake)
            redrawSnack(screen,snack)

def Snake_Snake(snake):
    global game_over
    for i in range(2,len(snake)):
            if snake[0]==snake[i]:
                game_over=True

def Snake_Screen(snake):
    global screenSize
    global game_over
    if (snake[0][0]>screenSize-10 or snake[0][0]<0):
        game_over=True
    elif (snake[0][1]>screenSize-10 or snake[0][1]<0):
        game_over=True

def k_direction(keys,headX,headY):
    global direction
    global speed

    if keys[pygame.K_RIGHT] and direction!="LEFT":
        direction="RIGHT"
        headX+=speed
    elif keys[pygame.K_LEFT] and direction!="RIGHT":
        direction="LEFT"
        headX-=speed
    elif keys[pygame.K_UP] and direction !="DOWN":
        direction="UP"
        headY-=speed
    elif keys[pygame.K_DOWN] and direction !="UP":
        direction="DOWN"
        headY+=speed
    return headX,headY, direction

def drawGame_Over(game_over):
    global screenSize
    global running

    def drawRestart(screen):
        font=pygame.font.SysFont("serif",30) 
        text= font.render("Play again: R",True,black)
        X=(250)-(text.get_width()//2)
        Y=(350)-(text.get_height()//2)
        screen.blit(text,((X,Y)))

    def drawScore(screen):
        score=(len(snake)*10)-10
        font=pygame.font.SysFont("serif",30) 
        text= font.render((f"Your score: {score}"),True,black)
        X=(250)-(text.get_width()//2)
        Y=(150)-(text.get_height()//2)
        screen.blit(text,((X,Y)))


    if game_over:
        screenG_O=pygame.display.set_mode((screenSize,screenSize))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        screenG_O.fill(background)
        font=pygame.font.SysFont("serif",50) 
        text= font.render("GAME OVER",True,black)
        centerX=(screenSize//2)-(text.get_width()//2)
        centerY=(screenSize//2)-(text.get_height()//2)
        screenG_O.blit(text,[centerX,centerY])
        drawRestart(screenG_O)
        drawScore(screenG_O)
        pygame.display.flip()

def drawScore(screen):
    score=(len(snake)*10)-10
    font=pygame.font.SysFont("serif",20) 
    text= font.render((f"Your score: {score}"),True,black)
    X=(400)-(text.get_width()//2)
    Y=(20)-(text.get_height()//2)
    screen.blit(text,((X,Y)))

def paused(keys):
    global running
    global pause
    if keys[pygame.K_p]:
        pause=True
        running=False
    while pause:    
        font=pygame.font.SysFont("serif",50) 
        text= font.render("PAUSE",True,black)
        centerX=(250)-(text.get_width()//2)
        centerY=(250)-(text.get_height()//2)
        screen.blit(text,(centerX,centerY))
        pygame.display.flip()   
        pygame.event.wait()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause=False
            running=True
            main()

def restart(keys):
    global running
    global pause
    global game_over
    global direction
    global headX
    global headY
    global snake
    global randomX
    global randomY
    global snack

    if keys[pygame.K_r]:
        if not running:
            running=True
        if pause:
            pause=False
        if game_over:
            game_over=False
        
        direction="RIGHT"
        headX=50
        headY=50

        snake=[(headX,headY)]

        randomX=random.randrange(50,450,10)
        randomY=random.randrange(50,450,10)

        snack=[(randomX,randomY)]

        main()


# Principal fuction
def main():

    # Global variables
    global running
    global pause
    global screenSize
    global game_over
    global headX
    global headY
    global direction

    # Initialization
    initialization()

    screen=pygame.display.set_mode((screenSize,screenSize))
    
    while running:

        clock=pygame.time.Clock()

        # Events
        events=pygame.event.get()
        checkEvents(events)

        # Color de fondo
        screen.fill(background)

        # Keys
        keys=pygame.key.get_pressed()
        k_direction(keys,headX,headY)

        # Fuctions
        drawScore(screen)

        moveSnake(direction,snake)

        drawSnake(screen,snake)

        drawSnack(screen,snack)

        # Collisions

        # Snake-Snack
        Snake_Snack(snake,snack,screen)

        # Snake-Snake
        Snake_Snake(snake)
        
        # Snake-Screen
        Snake_Screen(snake)

        # Game_Over
        drawGame_Over(game_over)

        # Paused
        paused(keys)

        # Restart
        restart(keys)

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(10)

    pygame.quit


main()

# python .\Snake.py