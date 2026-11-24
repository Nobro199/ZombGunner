import pygame
from math import sin,cos,pi,atan2
from shoot import Bullet
from enemy import Zombie

class Player():
    def __init__(self,x,y,bullets):
        #make player
        self.x=x
        self.y=y
        self.speedx=0
        self.speedy=0
        self.theta=0
        self.flag=False
        self.image=pygame.Surface((52,43),pygame.SRCALPHA)
        
        #blit image on image and face
        self.ss=pygame.image.load('spritesheet_characters.png')
        self.area=(110,132,52,43)
        self.image.blit(self.ss,(0,0),self.area)
        self.rect=self.image.get_rect()
        self.bullets=bullets
        self.ogimage=self.image
        #enemy
        self.bimage=pygame.Surface((35,43),pygame.SRCALPHA)
        self.barea=(424,0,35,43)
        self.bimage.blit(self.ss,(0,0),self.barea)
        self.brect=self.bimage.get_rect()
        self.og=(400,400)
        
    
    def draw(self,screen,camerax,cameray):
        
        #update player position
        self.image=pygame.transform.rotate(self.ogimage,self.theta)
        self.rect=self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image,(self.rect.x - camerax, self.rect.y - cameray))
        
        self.brect.center=self.og
        screen.blit(self.bimage,(self.brect.x-camerax,self.brect.y-cameray))
        
        
        
        
    def update(self):
    
        #update rectangle
        self.rect.center=(self.x,self.y)
        self.rect.centerx=round(self.x)
        self.rect.centery=round(self.y)
        
        print(self.x)
        print(self.y)
        if self.flag==True:
            bullet=Bullet(self.x,self.y,self.theta)
            self.bulletrect=bullet.rect
            self.bullets.add(bullet)
            self.flag=False
      
      
        
        
    def checkm(self,camerax,cameray):
            self.x=self.rect.centerx
            self.y=self.rect.centery
            mousex,mousey=pygame.mouse.get_pos()
            screenx=self.x-camerax
            screeny=self.y-cameray
            deltax=mousex-screenx
            deltay=mousey-screeny
            phi=atan2(-deltay,deltax)
            self.theta=phi*180/pi
            self.rect.centerx=round(self.x)
            self.rect.centery=round(self.y)
            
            
    
    def colli(self):
        z=False
        if self.rect.colliderect(self.brect):
            z=True
        return z

        
    
        
