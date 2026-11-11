import pygame
pygame.init()

WIDTH=864
HEIGHT=936

window=pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\background.png')
ground=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\infinite.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        bird1=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\bird1.png')
        bird2=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\bird2.png')
        bird3=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\bird3.png')
        self.birds=[bird1,bird2,bird3]
        self.index=0
        self.image=self.birds[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
        self.counter=0
        self.velocity=0
    def update(self):
        #Bird Flying Animation
        self.counter=self.counter+1
        limit=5
        if self.counter>limit:
            self.counter=0
            self.index=self.index+1
            if self.index==len(self.birds):
                self.index=0
        self.image=self.birds[self.index]

        #Gravity
        self.velocity=self.velocity+0.5
        if self.velocity>8:
            self.velocity=8
        if self.rect.bottom<768:
            self.rect.y=self.rect.y+self.velocity

        #Bird Movement
        if pygame.mouse.get_pressed()[0]==1:
            self.velocity=-10


        



groupbirds=pygame.sprite.Group()
bird=Bird(50,HEIGHT/2)
groupbirds.add(bird)




                
                

clock=pygame.time.Clock()
fps=60
scrollspeed=5
groundpos=0
run=True
while run:
    clock.tick(fps)
    window.blit(background,(0,0))
    window.blit(ground,(groundpos,768))
    groupbirds.draw(window)
    groupbirds.update()
    groundpos=groundpos-scrollspeed
    if abs(groundpos)>35:
        groundpos=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    
    pygame.display.update()