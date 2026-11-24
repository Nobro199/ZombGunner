import pygame
from math import sin,cos,pi,radians
from random import randint
from enemy import Zombie

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,theta):
        super().__init__()
        self.x=x
        self.y=y
        self.theta=theta
        self.ss=r"bullet.png"
        self.image=pygame.image.load(self.ss)
        self.og_img=self.image
        self.speed=7
        self.image=pygame.transform.rotate(self.og_img,self.theta)
        self.rect=self.image.get_rect(center=(self.x,self.y))
        
        
    def update(self,walls,player,zombies):
        #make a list of walls in conact with bullet             
        hit_walls = pygame.sprite.spritecollide(self,walls,False)
        #loop through list and if collides, kill
        for wall in hit_walls:
            if wall.rect.colliderect(self.rect):
                self.kill()
        #default bullet movement using trig to keep trojectory        
        self.x+=self.speed*cos(self.theta*pi/180)
        self.y-=self.speed*sin(self.theta*pi/180)
        self.rect.center=(self.x,self.y)
        
        hit_zombies = pygame.sprite.spritecollide(self,zombies,False)
        #loop through list and if collides, kill
        for zombie in hit_zombie:
            if zombie.rect.colliderect(self.rect):
                self.kill()
                zombie.kill()
        
#         ############DETETE AFTER MAKING ENEMY CLASS
#         if self.rect.colliderect(player.brect):
#                 player.og=(randint(0,500),randint(0,500))
                
        
    
         