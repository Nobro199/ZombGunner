import pygame

class BG(pygame.sprite.Sprite):
    def __init__(self,level,player,screen,walls):
        super().__init__()
        #import tiles and make them variable
        self.i=0
        self.walls=walls
        self.player=player
        self.screen=screen
        if level==1:
            self.ts=64
            self.width=self.ts*23
            self.height=self.ts*12
            self.size=(self.width,self.height)
            a=pygame.image.load(r"Tiles\tile_118.png")
            b=pygame.image.load(r"Tiles\tile_120.png")
            c=pygame.image.load(r"Tiles\tile_121.png")
            d=pygame.image.load(r"Tiles\tile_119.png")
            e=pygame.image.load(r"Tiles\tile_147.png")
            f=pygame.image.load(r"Tiles\tile_11.png")
            g=pygame.image.load(r"Tiles\tile_124.png")
            h=pygame.image.load(r"Tiles\tile_150.png")
            i=pygame.image.load(r"Tiles\tile_122.png")
            j=pygame.image.load(r"Tiles\tile_123.png")
            k=pygame.image.load(r"Tiles\tile_151.png")
            l=pygame.image.load(r"Tiles\tile_146.png")
            m=pygame.image.load(r"Tiles\tile_148.png")
            n=pygame.image.load(r"Tiles\tile_149.png")
            o=pygame.image.load(r"Tiles\tile_296.png")
            p=pygame.image.load(r"Tiles\tile_297.png")
            q=pygame.image.load(r"Tiles\tile_323.png")
            r=pygame.image.load(r"Tiles\tile_145.png")
            s=pygame.image.load(r"Tiles\tile_86.png")
            
            self.tile_matrix=[
                [a,b,b,b,c,b,b,b,c,b,b,b,b,c,b,b,b,b,b,c,b,b,d],
                [e,f,f,f,g,f,f,f,e,f,f,f,f,e,o,p,q,f,f,e,f,f,e],
                [e,f,f,f,f,f,f,f,e,f,f,f,f,e,f,f,f,f,f,e,f,f,e],
                [e,f,f,f,f,f,f,f,e,f,f,f,f,e,f,f,f,f,f,e,f,f,e],
                [e,f,f,f,h,f,f,f,e,f,f,a,b,i,j,f,f,k,b,l,f,f,e],
                [m,b,b,b,n,f,f,f,g,f,f,g,f,f,f,f,f,f,f,f,f,f,e],
                [e,f,f,f,e,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,e],
                [e,f,f,f,r,j,f,f,f,f,f,f,f,f,a,b,b,d,f,f,f,f,e],
                [e,f,f,f,f,f,f,f,f,f,f,h,f,f,g,f,f,g,f,f,f,f,e],
                [e,f,f,f,f,f,f,f,f,f,f,e,f,f,f,f,f,f,f,f,f,f,e],
                [e,f,f,f,h,f,f,f,f,f,f,e,f,f,f,f,f,f,f,f,f,f,e],
                [r,b,b,b,i,b,b,b,b,b,b,i,b,b,b,b,b,b,s,s,s,b,l]
            ]
            w1=Wall(0,0,64,(23*64))
            self.walls.add(w1)
            w2=Wall(0,0,(12*64),64)
            self.walls.add(w2)
            w3=Wall(64*4,0,(1*64),(64*2))
            self.walls.add(w3)
            w4=Wall((0),(5*64),(4*64),(64*1))
            self.walls.add(w4)
            
            
    def make_bg(self):
        self.bg=pygame.Surface(self.size)
        
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                self.bg.blit(self.tile_matrix[r][c], (c*self.ts,r*self.ts))
        self.rect=self.bg.get_rect()
        return self.bg
    def draw(self):
        #follow the player
        self.plx=(self.screen.get_width()//2)-self.player.rect.centerx
        self.ply=(self.screen.get_height()//2)-self.player.rect.centery
        #keep camera in view
        self.plx=max(0,min(self.plx,self.rect.width - (12*64)))
        self.ply=max(0,min(self.ply,self.rect.height - (9*64)))
        
        #blit screen
        self.screen.blit(self.bg,(self.plx,self.ply))
        
        
#wall class as a sprite so that player and bullets can't collide        
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,length):
        super().__init__()
        self.rect=pygame.Rect(x,y,width,length)

        
        