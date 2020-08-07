import pygame
import random

''' GLOBAL CONS'''
SCREEN_SIZE = 520
PIXEL_SIZE = 10

""" GLOBAL VARS """
PLAYER = []
KEYS = []
LEAD_X = 150
LEAD_Y = 250
DIR = 'RIGHT'
FOOD=(0,0)
FONT = ''
btn_array=[]
run = True

def begin():
    print('start')
    return True    

def end():
    print('death')
    return False

def create_button(x, y, w, h, text, callback, ACTIVE_COLOR, INACTIVE_COLOR):
    FONT = pygame.font.Font(None, 40)
    text_surf = FONT.render(text, True, (255, 255, 255))
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': INACTIVE_COLOR,
        'ACTIVE_COLOR':ACTIVE_COLOR,
        'INACTIVE_COLOR':INACTIVE_COLOR,
        'callback': callback,
        }
    return button

def draw_button(button, window):
    pygame.draw.rect(window, button['color'], button['rect'])
    window.blit(button['text'], button['text rect'])

def main():
    global KEYS, PLAYER, SCREEN_SIZE, PIXEL_SIZE, LEAD_X, LEAD_Y, DIR, FONT

    pygame.init()
    pygame.display.set_caption("SNAKE")
    window = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    LEAD_X = random.randrange(30, 470, PIXEL_SIZE)
    LEAD_Y = random.randrange(30, 470, PIXEL_SIZE)
    PLAYER = [(LEAD_X, LEAD_Y)]
    run = True
    btn_start = create_button(200, 280, 100, 60, 'START', begin, (23,123,181), (14,74,108))
    btn_exit = create_button(200, 350, 100, 60, 'EXIT', end, (197,73,0), (255,133,31))
    btn_array=[btn_start, btn_exit]
    while run != False:
        while run == True:
            pygame.time.delay(100)
            lvl = 1
            speed = 10 + (lvl * 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end() 

            KEYS = pygame.key.get_pressed()
            if KEYS[pygame.K_p]:
                run = 'pause'
                break
            
            if KEYS[pygame.K_LEFT] and DIR != 'RIGHT':
                DIR = 'LEFT'

            elif KEYS[pygame.K_RIGHT] and DIR != 'LEFT':
                DIR = 'RIGHT'

            elif KEYS[pygame.K_UP] and DIR != 'DOWN':
                DIR = 'UP'

            elif KEYS[pygame.K_DOWN] and DIR != 'UP':
                DIR = 'DOWN'

            window.fill((205, 237, 246))
            rec_up = pygame.draw.rect(window, (94, 177, 191), (0, 0, 510, 10)) #arriba
            rec_down = pygame.draw.rect(window, (94, 177, 191), (0, 510, 520, 520)) #abajo
            rec_left = pygame.draw.rect(window, (94, 177, 191), (0, 0, 10, 520)) # izquierdo
            rec_right = pygame.draw.rect(window, (94, 177, 191), (510, 0, 510, 520)) #derecho
            movement( DIR, PLAYER, speed )
            run = collision(rec_up, rec_down, rec_left, rec_right, window, PLAYER)
            eat( window, PLAYER, speed)
            score = str( len(PLAYER) )
            FONT = pygame.font.SysFont("arial", 20)
            label = FONT.render('SCORE: '+ score , 1, (4, 42, 43))
            window.blit( label, (220, 10) )        
            pygame.display.update()
        
        while run == 'loser':
            pygame.time.delay(100) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in btn_array:
                            if button['rect'].collidepoint(event.pos):
                                run = button['callback']()
                elif event.type == pygame.MOUSEMOTION:
                    for button in btn_array:
                        if button['rect'].collidepoint(event.pos):
                            button['color'] = button['ACTIVE_COLOR']
                        else:
                            button['color'] = button['INACTIVE_COLOR']
            KEYS = pygame.key.get_pressed()
            if KEYS[pygame.K_s] or run == True:
                LEAD_X = random.randrange(30, 470, PIXEL_SIZE)
                LEAD_Y = random.randrange(30, 470, PIXEL_SIZE)
                PLAYER = [(LEAD_X, LEAD_Y)]
                FOOD=(0,0)
                run = True
                break  

            window.fill((37, 36, 34))
            FONT = pygame.font.SysFont("arial", 50)
            label = FONT.render('YOU LOSE', 1, (235, 94, 40))
            window.blit( label, ( 120, 40) )
            score = str( len(PLAYER) )
            FONT = pygame.font.SysFont("arial", 50)
            label = FONT.render('FINAL SCORE: '+ score , 1, (235, 94, 40))
            window.blit( label, (80, 200) )  
            FONT = pygame.font.SysFont("arial", 20)
            label = FONT.render(' To play again press S' , 1, (235, 94, 40))
            window.blit( label, (150, 420) )

            rec_up = pygame.draw.rect(window, (204, 197, 185), (0, 0, 510, 10)) #arriba
            rec_down = pygame.draw.rect(window, (204, 197, 185), (0, 510, 520, 520)) #abajo
            rec_left = pygame.draw.rect(window, (204, 197, 185), (0, 0, 10, 520)) # izquierdo
            rec_right = pygame.draw.rect(window, (204, 197, 185), (510, 0, 510, 520)) #derecho
            for button in btn_array:
                draw_button(button, window)
            pygame.display.update()
        
        while run == 'pause':
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in btn_array:
                            if button['rect'].collidepoint(event.pos):
                                run = button['callback']()
                            print(run)
                elif event.type == pygame.MOUSEMOTION:
                    for button in btn_array:
                        if button['rect'].collidepoint(event.pos):
                            button['color'] = button['ACTIVE_COLOR']
                        else:
                            button['color'] = button['INACTIVE_COLOR']
            KEYS = pygame.key.get_pressed()
            if KEYS[pygame.K_s] or run == True:
                run = True
                break  

            FONT = pygame.font.SysFont("arial", 50)
            label = FONT.render('PAUSED', 1, (255, 159, 28))
            window.blit( label, (170, 100) )
            FONT = pygame.font.SysFont("arial", 20)
            label = FONT.render('Press S to go back', 1, (255, 159, 28))
            window.blit( label, (180, 420) )
            for button in btn_array:
                draw_button(button, window)
            pygame.display.update()
    pygame.quit()
    
def movement(DIR, PLAYER, speed):
    x = PLAYER[0][0]
    y = PLAYER[0][1]

    PLAYER.pop()

    if DIR == 'UP':
        y -= speed

    elif DIR == 'DOWN':
        y += speed

    elif DIR == 'LEFT':
        x -= speed

    elif DIR == 'RIGHT':
        x += speed

    PLAYER.insert(0,(x,y))

def collision(rec_up, rec_down, rec_left, rec_right, window, player):
    rec_player = pygame.draw.rect(window, (239, 123, 69), (player[0][0], player[0][1], PIXEL_SIZE, PIXEL_SIZE))
    if rec_player.colliderect(rec_up) or rec_player.colliderect(rec_down) or rec_player.colliderect(rec_left) or rec_player.colliderect(rec_right):
        print('chocaste con una pared buuu')
        return 'loser'

    for ln in range(1, len(player)):
        rec = pygame.draw.rect(window, (239, 123, 69), (player[ln][0],player[ln][1], PIXEL_SIZE, PIXEL_SIZE))
        if len(player) > 3 and rec_player.colliderect(rec):
            print('chocaste contigo mismo genio')
            return 'loser'
    return True

def eat(window, player, speed):
    global FOOD
    rec_player = pygame.draw.rect(window, (239, 123, 69), (player[0][0], player[0][1], PIXEL_SIZE, PIXEL_SIZE))
    if FOOD[0] == 0 and FOOD[1] == 0:
        FOOD = ( random.randrange(10, 490, PIXEL_SIZE), random.randrange(10, 490, PIXEL_SIZE) )
    rec_food = pygame.draw.rect(window, (216, 71, 39), (FOOD[0], FOOD[1], PIXEL_SIZE, PIXEL_SIZE))
    if rec_player.colliderect(rec_food):
        if DIR == 'UP':
            player.insert(0, ( player[0][0], player[0][1] - speed ))

        elif DIR == 'DOWN':
            player.insert(0, ( player[0][0], player[0][1] + speed ))

        elif DIR == 'LEFT':
            player.insert(0, ( player[0][0] - speed, player[0][1]  ))
        elif DIR == 'RIGHT':
            player.insert(0, ( player[0][0] + speed , player[0][1] ))
        FOOD = ( random.randrange(10, 490, PIXEL_SIZE), random.randrange(10, 490, PIXEL_SIZE) )
    while FOOD in player:
        FOOD = ( random.randrange(10, 490, PIXEL_SIZE), random.randrange(10, 490, PIXEL_SIZE) )
    return rec_food   

#MAIN()
main()