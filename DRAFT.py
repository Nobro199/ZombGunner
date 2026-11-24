#default code
import pygame
from player import Player
from shoot import Bullet
from background import BG
from enemy import Zombie
pygame.init()
clock=pygame.time.Clock()

#unit settings
TS=64
Wid=TS*12
Len=TS*9
SIZE=(Wid,Len)

#screen and bg
screen=pygame.display.set_mode(SIZE)
bluey=(40,40,120)
bg=pygame.Surface(SIZE)
bg.fill(bluey)

#font setting
font=pygame.font.Font('oj.ttf', size=100)
#render title on surface
title=font.render('Hitman Run!',1,(255,255,255))
titleRect=title.get_rect()
titleRect.center=(Wid/2,Len/2-50)
#make subtitle
sfont=pygame.font.Font('oj.ttf', size=50)
subtitle=sfont.render('(Click any button so start)',1,(255,255,255))
subtitleRect=subtitle.get_rect()
subtitleRect.center=(Wid/2,Len/2)

#load sounds
pygame.mixer.init()
swoosh=pygame.mixer.Sound('mixkit-cartoon-toy-whistle-616.wav')
bonk=pygame.mixer.Sound('bonk.mp3')
coin=pygame.mixer.Sound('coin.wav')
#make player and class bullets as sprite group
bullets=pygame.sprite.Group()
player=Player(100,100,bullets)
enemy=Zombie(1000,800,bullets)



############################# INTRO SCREEN LOOP

running=1
while running:
    #blit bg and then title
    screen.blit(bg,(0,0))
    screen.blit(title,titleRect)
    screen.blit(subtitle,subtitleRect)
    pygame.display.flip()
    
    #get events
    events=pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            pygame.quit()
        if e.type==pygame.KEYDOWN:
            coin.play()
            running=0
            ##################################
black=(0,0,0)
bg=pygame.Surface(SIZE)
bg.fill(black)
#font setting
font=pygame.font.Font('oj.ttf', size=80)
#render title on surface
title=font.render('Instructions:',1,(255,255,255))
titleRect=title.get_rect()
titleRect.center=(Wid/2,Len/2-120)
#make subtitle
sfont=pygame.font.Font('oj.ttf', size=40)
subtitle=sfont.render('-Shoot the zombies before they touch you.\n-Youll have 3 lives.\n-Click cursor to shoot.\n-Destroy all the spawnpoints to win!!',1,(255,255,255))
subtitleRect=subtitle.get_rect()
subtitleRect.center=(Wid/2,Len/2)

############################# Instruction Screen
running=1
while running:
    #blit bg and then title
    screen.blit(bg,(0,0))
    screen.blit(title,titleRect)
    screen.blit(subtitle,subtitleRect)
    pygame.display.flip()
    
    #get events
    events=pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            pygame.quit()
        if e.type==pygame.KEYDOWN:
            coin.play()
            running=0            
            
            
            

#############################
 #make background for game           
walls=pygame.sprite.Group()
zombies=pygame.sprite.Group()
level1=BG(1,player,screen,walls)
bg=level1.make_bg()
running=1
x=0
y=0
speedx=4
speedy=4

#make screen variables to edit
camerax=0
cameray=0
dist=200

mapw=level1.width
maph=level1.height
screenw=screen.get_width()
screenh=screen.get_height()
############################# MAIN GAME LOOP
running=1
colli=False
while running:
#blit bg and then player
    clock.tick(60)
    level1.draw
#######MOVEMENT
    
    #basic movement when key pressed
    key=pygame.key.get_pressed()
    
    #while L or R pressed, move player
    if key[pygame.K_LEFT]:
        player.x -= speedx
        print(player.x)
    if key[pygame.K_RIGHT]:
        player.x += speedx
        print(player.x)
    #round rectangle because too many errors with going throuhh walls when aiming
    player.rect.centerx=round(player.x)
    
    #while Up or Down pressed, move player
    if key[pygame.K_UP]:
        player.y -= speedy
        print(player.y)
    if key[pygame.K_DOWN]:
        print(player.y)
        player.y += speedy
    #round rectangle because too many errors with going throuhh walls when aiming
    player.rect.centery=round(player.y)
    
#########WALL COLLISION
    
    #create list of walls(sprites) in contact with player
    contact=pygame.sprite.spritecollide(player,walls,False)
    for sprite in contact:
        #if key held down, be sure to keep player inside domain
        if key[pygame.K_RIGHT]:
            player.rect.right=sprite.rect.left
        elif key[pygame.K_LEFT]:
            player.rect.left=sprite.rect.right
        #round rectangle again
        player.x=player.rect.centerx

    #create list of walls(sprites) in contact with player
    contact=pygame.sprite.spritecollide(player,walls,False)
    for sprite in contact:
        #if key held down, be sure to keep player inside domain
        if key[pygame.K_DOWN]:  
            player.rect.bottom=sprite.rect.top
        elif key[pygame.K_UP]:  
            player.rect.top=sprite.rect.bottom
        player.y=player.rect.centery
    

#######CAMERA MOVEMENT

#move screen right or left if player moved
    if player.rect.right-camerax > screenw-dist:
        camerax=player.rect.right-(screenw-dist)
    elif player.rect.left-camerax < dist:
        camerax=player.rect.left-dist
    #move screen up or down
    if player.rect.bottom-cameray > screenh-dist:
        cameray=player.rect.bottom-(screenh-dist)
    elif player.rect.top-cameray < dist:
        cameray=player.rect.top-dist
    #keep camera  from going too far off edge to blackness
    camerax=max(0, min(camerax,mapw-screenw))
    cameray=max(0, min(cameray,maph-screenh))
    
    #check the player method for mouse movement
    player.checkm(camerax,cameray)
    enemy.checkplayer(camerax,cameray,player)
    
    #draw player and background
    screen.blit(bg,(-camerax,-cameray))
    player.draw(screen,camerax,cameray)
    enemy.draw(screen,camerax,cameray)
    
   #edit missile group
    bullets.update(walls,player)
    
    
    #blit other objects on screen with moving screen
    for bullet in bullets:
        screen.blit(bullet.image,(bullet.rect.x-camerax,bullet.rect.y-cameray))
    
    #finalize flip
    pygame.display.flip()
    
    #get events
    events=pygame.event.get()
    
    #check e types and make elif for each type
    for e in events:
        #keep exit method plusible
        if e.type==pygame.QUIT:
            pygame.quit()
        
        #if mouse clicked then shoot a bullet
        elif e.type==pygame.MOUSEBUTTONDOWN:
            #call flag true to enable shooting
            player.flag=True
            player.update()

            #use player variables inside the bullet class
            bullet = Bullet(player.x,player.y,player.theta)
            #add a new bullet sprite group each time a bullet is created
            bullets.add(bullet)
        

        
    #if player collides with zombie then game over    
    if player.colli():
        print('Lost')
        running=0
    #get fps
    clock.tick(60)
    fps=clock.get_fps()
    pygame.display.set_caption(f"{fps:0.1f}")

#############################GAME OVER SCREEN
reddy=(230,30,20)
bg.fill(reddy)
#Title
title=font.render('GAME OVER!!!',1,(255,255,255))
titleRect=title.get_rect()
titleRect.center=(Wid/2,Len/2-50)
#make subtitle
sfont=pygame.font.Font('oj.ttf', size=50)
subtitle=sfont.render('(Click any button to exit game)',1,(255,255,255))
subtitleRect=subtitle.get_rect()
subtitleRect.center=(Wid/2,Len/2)

running=1
while running:
    #blit bg and then title
    screen.blit(bg,(0,0))
    screen.blit(title,titleRect)
    screen.blit(subtitle,subtitleRect)
    pygame.display.flip()
    
    #get events
    events=pygame.event.get()
    for e in events:
        if e.type==pygame.QUIT:
            pygame.quit()
        if e.type==pygame.KEYDOWN:
            running=0


pygame.quit()


