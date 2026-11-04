import pygame
pygame.init()

WIDTH=864
HEIGHT=936

window=pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\background.png')
ground=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Flappy Bird\assets\infinite.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

clock=pygame.time.Clock()
fps=60
scrollspeed=5
groundpos=0
run=True
while run:
    clock.tick(fps)
    window.blit(background,(0,0))
    window.blit(ground,(groundpos,768))
    groundpos=groundpos-scrollspeed
    if abs(groundpos)>35:
        groundpos=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    
    pygame.display.update()