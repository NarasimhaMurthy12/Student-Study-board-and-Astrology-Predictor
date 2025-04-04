import pygame as py
import sys
import math
import random
import time
from pygame import mixer
import os

#initiaisation
py.init()
clock = py.time.Clock()

# Bg Music
'''py.mixer.music.load('background.wav')
py.mixer.music.play(-1)'''

#main screen
width=800
height=600
screen=py.display.set_mode((width,height))

#Background
bgimg = py.image.load(r'files\bg.jpg')
bgimg = py.transform.scale(bgimg,(800,600))


def bg():
    screen.blit(bgimg,(0,0))

#title and icon
py.display.set_caption("Game")
icon = py.image.load(r'files\rocket.png')
#icon = py.transform.smoothscale(icon,(1,1))
py.display.set_icon(icon)

#Player

playerimg = py.image.load(r'files\space-invaders.png')
pos_x = 370
pos_y = 535
moving_right = False
moving_left = False
moving_down = False

#Enemy
enemyimg = []
eos_x =[]
eos_y = []
change_eos_x = []
change_eos_y = []
n_enemies = 6

for i in range(n_enemies):
    enemyimg.append(py.image.load(r'files\alien2.png'))
    enemyimg.append(py.image.load(r'files\alien4.png'))
    enemyimg.append(py.image.load(r'files\alien3.png'))
    eos_x.append(random.randint(0,736))
    eos_y.append(random.randint(0,100))
    change_eos_x.append(3)
    change_eos_y.append(30) 


#Bullet
bulletimg = py.image.load(r'files\bullet.png')
bos_x = 0
bos_y = 480
change_bos_x = 0
change_bos_y = 5
#Ready - not seen
#Fire - moving 
b_state = 'ready'


#Score
score_v = 0
disp = py.font.Font('freesansbold.ttf',40)
disp_1 = py.font.Font('freesansbold.ttf',70)

def game_end(s):
    score1 = disp_1.render('GAME OVER!',True,(255,3,25))
    screen.blit(score1,(200,250))



def score():
    score1 = disp.render('Score : '+str(score_v),True,(255,3,25))
    screen.blit(score1,(10,10))

def player(x,y):
    screen.blit(playerimg,(pos_x,pos_y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def bullet(x,y):
    global b_state
    b_state='fire'
    screen.blit(bulletimg,(x+16,y+10))

def collision(eos_x,eos_y,bos_x,bos_y):
    dist = math.sqrt(math.pow((eos_x-bos_x),2)+math.pow((eos_y-bos_y),2))
    if dist < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill(('black'))
    bg()
    player(pos_x,pos_y)
    
    
    for e in py.event.get():
        if e.type==py.QUIT:
            running = False
            
            
        if e.type == py.KEYDOWN:
            if e.key == py.K_RIGHT:
                moving_right = True
            elif e.key == py.K_LEFT:
                moving_left = True
            if e.key == py.K_RETURN:
                running = True
                print('1')
            if e.key==py.K_SPACE:
                if b_state=='ready':
                    bos_x = pos_x
                    bullet(bos_x,pos_y)
                    snd = mixer.Sound(r'files\laser.wav')
                    snd.play()
                
        if e.type == py.KEYUP:
            if e.key == py.K_RIGHT:
                moving_right = False
            elif e.key == py.K_LEFT:
                moving_left = False
            
    # UPDATING
    if moving_right:
        pos_x += 2
    elif moving_left:
        pos_x -= 2


    x=pos_x
    y=pos_y
    # CONSTRAINTS
    if pos_x < 0:
        pos_x = 0
    if pos_x > 736:
        pos_x = 736
    if pos_y < 0:
        pos_y = 0
    if pos_y > 536:
        pos_y = 536


    #Enemy Movement
    for i in range(n_enemies):
        # game end
        if eos_y[i]>450:
            for j in range(n_enemies): 
                eos_y[j]=2000
            game_end(score_v)
            b_state='ready'
            
            break
        eos_x[i] += change_eos_x[i]
        if eos_x[i] < 0:
            change_eos_x[i] = 5
            eos_y[i] += change_eos_y[i]
        if eos_x[i] > 736:
            change_eos_x[i] = -5
            eos_y[i] += change_eos_y[i]

        #collision
        Collision = collision(eos_x[i], eos_y[i], bos_x, bos_y)
        if Collision:
            sod = mixer.Sound(r'files\collision.wav')
            sod.play()
            bos_y = 480
            b_state = 'ready'
            score_v +=5
            eos_x[i] = random.randint(0,735)
            eos_y[i] = random.randint(0,50)
        enemy(eos_x[i],eos_y[i],i)
    
    
    #Bullet Movement
    if bos_y<=0:
        bos_y = 480
        b_state = 'ready'
    if b_state == 'fire':
        bullet(bos_x,bos_y)
        bos_y-=change_bos_y
    
    score()
    #update
    py.display.update()
    clock.tick(120)


