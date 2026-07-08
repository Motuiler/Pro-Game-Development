import pygame
pygame.init()

WIDTH=1000
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Invader')
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\background.png')
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
SIZE=50
red=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship red.png')
red=pygame.transform.scale(red,(SIZE,SIZE))
red=pygame.transform.rotate(red,90)
yellow=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship yellow.png')
yellow=pygame.transform.scale(yellow,(SIZE,SIZE))
yellow=pygame.transform.rotate(yellow,270)

border=pygame.Rect(WIDTH/2-10,0,20,HEIGHT)

def restart():
    run=True
    while run:
        window.blit(background,(0,0))
        window.blit(red,(200,250))
        window.blit(yellow,(750,250))
        pygame.draw.rect(window,(0,0,0),border)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

restart()