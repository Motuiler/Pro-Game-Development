import pygame
import random
import time
pygame.init()

WIDTH=500
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Shoot the Alien')
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Shoot the alien\images\grass.png')
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
alien=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Shoot the alien\images\alien.png')
alien=pygame.transform.scale(alien,(40,80))
font=pygame.font.SysFont('Arial',50,True,True)
score=0
alienrect_width=40
alienrect_height=80
alienrect=pygame.Rect(250,250,alienrect_width,alienrect_height)
run=True
clock=pygame.time.Clock()
while run:
    window.blit(background,(0,0))
    window.blit(alien,(alienrect.x,alienrect.y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if alienrect.collidepoint(event.pos):
                    score=score+1
                    newx=random.randint(0,WIDTH-alienrect_width)
                    newy=random.randint(0,HEIGHT-alienrect_height)

                    alienrect.x=newx
                    alienrect.y=newy

    scoretext=font.render(f'Score:{score}',True,(0,0,0))
    window.blit(scoretext,(5,5))

    clock.tick(10)

    pygame.display.update()