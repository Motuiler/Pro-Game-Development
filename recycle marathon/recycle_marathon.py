import random
import time
import pygame
pygame.init()

WIDTH=800
HEIGHT=600

window=pygame.display.set_mode((WIDTH,HEIGHT))

background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\game.png')
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
font=pygame.font.SysFont('Arial',50,True,True)

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

class Recycle(pygame.sprite.Sprite):
    image1=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\recyclable box.png')
    image2=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\recyclable paper bag.png')
    image2=pygame.transform.scale(image2,(40,60))
    image3=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\recyclable pencil.png')
    images=[image1,image2,image3]
    def __init__(self):
        super().__init__()
        self.image=random.choice(self.images)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(self.rect.width,WIDTH-self.rect.width)
        self.rect.y=random.randint(self.rect.height,HEIGHT-self.rect.height)

class Nonrecycle(pygame.sprite.Sprite):
    image1=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\plastic bag.png')
    image1=pygame.transform.scale(image1,(40,60))
    images=[image1]
    def __init__(self):
        super().__init__()
        self.image=random.choice(self.images)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(self.rect.width,WIDTH-self.rect.width)
        self.rect.y=random.randint(self.rect.height,HEIGHT-self.rect.height)

nonrecycles=pygame.sprite.Group()
for i in range(15):
    new=Nonrecycle()
    nonrecycles.add(new)

recycles=pygame.sprite.Group()
for i in range(40):
    new=Recycle()
    recycles.add(new)

bin=Bin()
bins=pygame.sprite.Group()
bins.add(bin)

clock=pygame.time.Clock()
score=0
starttime=time.time()
totaltime=30
targetscore=70
run=True
while run:
    clock.tick(120)
    window.blit(background,(0,0))
    bins.draw(window)
    recycles.draw(window)
    nonrecycles.draw(window)
    timepassed=round(time.time()-starttime)
    if timepassed>=totaltime:
        if score>=targetscore:
            win=font.render('You Won!',True,(0,0,0))
            win1=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\win.png')
            window.blit(win1,(0,0))
            window.blit(win,(WIDTH/2,HEIGHT/2))
        else:
            win=font.render('Better Luck Next Time!',True,(0,0,0))
            win1=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\recycle marathon\images\loss.png')
            window.blit(win1,(0,0))
            window.blit(win,(WIDTH/2,HEIGHT/2))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    keyspressed=pygame.key.get_pressed()
    bins.update(keyspressed)

    recyclable=pygame.sprite.spritecollide(bin,recycles,True)
    nonrecyclable=pygame.sprite.spritecollide(bin,nonrecycles,True)
    for i in recyclable:
        score=score+3
    for i in nonrecyclable:
        score=score-5

    scoretext=font.render(f'Score:{score}',True,(0,0,0))
    window.blit(scoretext,(5,5))

    timetext=font.render(f'Remaining Time:{totaltime-timepassed}',True,(0,0,0))
    window.blit(timetext,(WIDTH-timetext.get_width(),5))

    pygame.display.update()