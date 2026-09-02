import pygame
pygame.init()

WIDTH=1000
HEIGHT=500
FPS=60

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Invader')
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\background.png')
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
SIZE=50
SPEED=3
red=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship red.png')
red=pygame.transform.scale(red,(SIZE,SIZE))
red=pygame.transform.rotate(red,90)
redrect=pygame.Rect(200,250,SIZE,SIZE)
yellow=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship yellow.png')
yellow=pygame.transform.scale(yellow,(SIZE,SIZE))
yellow=pygame.transform.rotate(yellow,270)
yellowrect=pygame.Rect(750,250,SIZE,SIZE)

border=pygame.Rect(WIDTH/2-10,0,20,HEIGHT)
clock=pygame.time.Clock()

def redspaceshipmovement(keys):
    if keys[pygame.K_w] and redrect.top>0:
        redrect.y=redrect.y-SPEED
    if keys[pygame.K_s] and redrect.bottom<HEIGHT:
        redrect.y=redrect.y+SPEED
    if keys[pygame.K_a] and redrect.left>0:
        redrect.x=redrect.x-SPEED
    if keys[pygame.K_d] and redrect.right<border.left:
        redrect.x=redrect.x+SPEED

def yellowspaceshipmovement(keys):
    if keys[pygame.K_UP] and yellowrect.top>0:
        yellowrect.y=yellowrect.y-SPEED
    if keys[pygame.K_DOWN] and yellowrect.bottom<HEIGHT:
        yellowrect.y=yellowrect.y+SPEED
    if keys[pygame.K_LEFT] and yellowrect.left>border.right:
        yellowrect.x=yellowrect.x-SPEED
    if keys[pygame.K_RIGHT] and yellowrect.right<WIDTH:
        yellowrect.x=yellowrect.x+SPEED

def restart():
    run=True
    while run:
        clock.tick(FPS)
        window.blit(background,(0,0))
        window.blit(red,(redrect.x,redrect.y))
        window.blit(yellow,(yellowrect.x,yellowrect.y))
        pygame.draw.rect(window,(0,0,0),border)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

        keys=pygame.key.get_pressed()
        redspaceshipmovement(keys)
        yellowspaceshipmovement(keys)
        pygame.display.update()


restart()