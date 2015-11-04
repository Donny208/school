import pygame, sys, random, time
from pygame import *
import time
pygame.init()
x = int(400)
y = int(400)
useless = 0
speed = 0
screen = pygame.display.set_mode((800,800))
myfont = pygame.font.SysFont("monospace", 60)
pygame.mixer.music.load("pong.mp3")
color = (0,0,0)
color4 = (255,255,255)
screen.fill( color )
pygame.display.update()
display.set_caption('By Donovan')
score = {
    'play1': 0,
    'play2': 0
}
edgex = 'true'
edgey = 'true'
p1x = 25
p1y = 350
p2x = 750
p2y = 350
rightleft = random.randint(1,2)
if rightleft == 1:
    edgex = 'false'
    edgey = 'false'
elif rightleft == 2:
    edgex = 'true'
    edgey = 'true'

def random_color():
    global x, y, edgex, edgey, score,speed
    screen.fill( color )
    time.sleep(0.0045)
    color2 = (255,255,255)
    color3 = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    pygame.draw.circle(screen, color2, (x, y), 10, 0)
    #pygame.draw.polygon(screen, color2, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    #pygame.draw.polygon(screen, color3, ((146, 10), (281, 106), (226, 267), (66, 267), (10, 106)))
    score1 = myfont.render(str(score['play1']), 1, (0,191,255))
    screen.blit(score1, (100, 100))

    score2 = myfont.render(str(score['play2']), 1, (255,20,147))
    screen.blit(score2, (650, 100))

    #color5 = myfont.render("Bo U R Bad.", 1, (255,0,0))
    #screen.blit(color5, (0, 150))
    
    #Player 1 Rect
    p1 = pygame.draw.rect(screen,color4,(p1x,p1y,20,120))
    #Player 2 Rect
    p2 = pygame.draw.rect(screen,color4,(p2x,p2y,20,120))
        
    if edgex == 'true':
        x = x + 2
        if x > 800:
            edgex = 'false'
            #Player 1 Point
            score['play1'] = score['play1'] + 1
            print('Player 1:',score['play1'],'Player 2:',score['play2'])
            x = 400
            y = 400
            time.sleep(1.5)
            
    elif edgex == 'false':
        x = x - 2
        if x < 0:
            edgex = 'true'
            #Player 2 Point
            score['play2'] = score['play2'] + 1
            print('Player 1:',score['play1'],'Player 2:',score['play2'])
            x = 400
            y = 400
            time.sleep(1.5)
            
    if edgey == 'true':
        y = y + 2
        if y > 800:
            edgey = 'false'
            
    elif edgey == 'false':
        y = y - 2
        if y < 0:
            edgey = 'true'
            
    pygame.display.update()
    #print(x,y)

def player1(key):
    global p1x, p1y
    if key == "down":
        p1y = p1y + 5
        #print('player1 down')
    elif key =="up":    
        p1y = p1y - 5
        #print('player1 up')

def player2(key):
    global p2x, p2y
    if key == "down":
        p2y = p2y + 5
        #print('player2 down')
        
    elif key =="up":
        p2y = p2y - 5
        #print('player2 up')

while (True):
    random_color()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit();
            sys.exit();
    pressed = pygame.key.get_pressed()
    #Player 1
    if pressed[pygame.K_w]:
        if p1y == 0:
            useless = 0
        else:
            player1('up')
    if pressed[pygame.K_s]:
        if p1y == 700:
            useless = 0
        else:
            player1('down')

    #Player 2
    if pressed[pygame.K_UP]:
        if p2y == 0:
            useless = 0
        else:
            player2('up')
    if pressed[pygame.K_DOWN]:
        if p2y == 700:
            useless = 0
        else:
            player2('down')

    if x <= 45:
        print('Ball is at 45')
        if y >= p1y and y <= p1y+120:
            print('HIT')
            speed = speed + 1
            print(speed)
            edgex = 'true'
            pygame.mixer.music.play()

    elif x >= 750:
        print('Ball is at 750')
        if y >= p2y and y <= p2y+120:
            print('Hit!')
            speed = speed + 1
            print(speed)
            edgex = 'false'
            pygame.mixer.music.play()
