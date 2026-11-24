import pygame
from math import sin,cos,pi,atan2

class Zombie():
    def __init__(self,x,y,bullets):
        #make enemy
        self.x=x
        self.y=y
        self.speedx=0
        self.speedy=0
        self.theta=0
        self.flag=False
        self.image=pygame.Surface((52,43),pygame.SRCALPHA)
        
        #blit image on image and face
        self.ss=pygame.image.load('spritesheet_characters.png')
        self.area=(424,0,35,43)
        self.image.blit(self.ss,(0,0),self.area)
        self.rect=self.image.get_rect()
        self.bullets=bullets
        self.ogimage=self.image
    
    def draw(self,screen,camerax,cameray):
        
        #update player position
        self.image=pygame.transform.rotate(self.ogimage,self.theta)
        self.rect=self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image,(self.rect.x - camerax, self.rect.y - cameray))
        
        
    def update(self):
    
        #update rectangle
        self.rect.center=(self.x,self.y)
        self.rect.centerx=round(self.x)
        self.rect.centery=round(self.y)
        
        print(self.x)
        print(self.y)
        
        
    def checkplayer(self,camerax,cameray,player):
            self.field=pygame.rect #make a rect
            self.field.center=player.x,player.y
            self.x=self.rect.centerx
            self.y=self.rect.centery
            
            if self.rect.colliderect(self.field):
                phi=atan2(-deltay,deltax)
                self.theta=phi*180/pi
                self.x+=self.speed*cos(self.theta*pi/180)
                self.y-=self.speed*sin(self.theta*pi/180)
                self.rect.center=(self.x,self.y)
                self.rect.centerx=round(self.x)
                self.rect.centery=round(self.y)
            
            
    


        
    
        

