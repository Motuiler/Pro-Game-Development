import pygame 
pygame.init()

WIDTH=500
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__()
        self.image=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship red.png')
        self.image=pygame.transform.scale(self.image,size)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def update(self):
        #self.image=pygame.transform.rotate(self.image,1)
        if self.rect.y<HEIGHT:
            self.rect.y=self.rect.y+1

red=Spaceship((50,50),225,225)
red1=Spaceship((100,100),10,10)
reds=pygame.sprite.Group()
reds.add(red)
reds.add(red1)

run=True
while run:
    window.fill('White')
    #window.blit(red.image,red.rect)
    reds.draw(window)
    reds.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

    pygame.display.update()