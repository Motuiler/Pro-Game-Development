import pygame
pygame.init()

WIDTH=500
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Shoot the Alien')
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Shoot the alien\images\grass.png')
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
alien=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Shoot the alien\images\alien.png')
alien=pygame.transform.scale(alien,(40,80))
alienrect=pygame.Rect(250,250,40,80)
run=True
while run:
    window.blit(background,(0,0))
    window.blit(alien,(alienrect.x,alienrect.y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    pygame.display.update()