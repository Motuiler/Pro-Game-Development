import pygame
pygame.init()

WIDTH=600
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))

background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\game.png')

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\recyclable bin.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

    def update(self,keyspressed):
        if keyspressed[pygame.K_w]:
            self.rect.y=self.rect.y-2
        if keyspressed[pygame.K_s]:
            self.rect.y=self.rect.y+2
        if keyspressed[pygame.K_d]:
            self.rect.x=self.rect.x+2
        if keyspressed[pygame.K_a]:
            self.rect.x=self.rect.x-2

bin=Bin()
bins=pygame.sprite.Group()
bins.add(bin)

run=True
while run:
    window.blit(background,(0,0))
    bins.draw(window)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    keyspressed=pygame.key.get_pressed()
    bins.update(keyspressed)
    pygame.display.update()