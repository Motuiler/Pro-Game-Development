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
BULLETSPEED=5
red=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship red.png')
red=pygame.transform.scale(red,(SIZE,SIZE))
red=pygame.transform.rotate(red,90)
redrect=pygame.Rect(200,250,SIZE,SIZE)
yellow=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\spaceship yellow.png')
yellow=pygame.transform.scale(yellow,(SIZE,SIZE))
yellow=pygame.transform.rotate(yellow,270)
yellowrect=pygame.Rect(750,250,SIZE,SIZE)
silencer=pygame.mixer.Sound(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Space Invaders\assets\Silencer+Gun Sound.mp3')

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

def handlebullet(redbullet,yellowbullet):
    for bullet in redbullet:
        bullet.x=bullet.x+BULLETSPEED
        if bullet.x>WIDTH:
            redbullet.remove(bullet)
    for bullet in yellowbullet:
        bullet.x=bullet.x-BULLETSPEED
        if bullet.x<0:
            yellowbullet.remove(bullet)

def restart():
    redbullet=[]
    yellowbullet=[]  
    run=True
    while run:
        clock.tick(FPS)
        window.blit(background,(0,0))
        window.blit(red,(redrect.x,redrect.y))
        window.blit(yellow,(yellowrect.x,yellowrect.y))
        pygame.draw.rect(window,(0,0,0),border)
        for bullet1 in redbullet:
            pygame.draw.rect(window,(255,255,255),bullet1)
        for bullet2 in yellowbullet:
            pygame.draw.rect(window,(255,255,255),bullet2)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LSHIFT:
                    bullet1=pygame.Rect(redrect.right,redrect.y+redrect.height/2,10,5)
                    redbullet.append(bullet1)
                    silencer.play()
                if event.key==pygame.K_KP0:
                    bullet2=pygame.Rect(yellowrect.left,yellowrect.y+yellowrect.height/2,10,5)
                    yellowbullet.append(bullet2)
                    silencer.play()
        keys=pygame.key.get_pressed()
        redspaceshipmovement(keys)
        yellowspaceshipmovement(keys)
        handlebullet(redbullet,yellowbullet)
        pygame.display.update()


restart()