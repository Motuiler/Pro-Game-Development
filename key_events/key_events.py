import pygame 
pygame.init()

WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Keys')
rocket=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\key_events\rocket.png')
rocketrect=pygame.Rect(250,250,150,219)
background=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\key_events\background.png')
directions={'up':False,'down':False,'right':False,'left':False}
run=True
while run:
    window.blit(background,(0,0))
    window.blit(rocket,(rocketrect.x,rocketrect.y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                directions['up']=True
            if event.key==pygame.K_s:
                directions['down']=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                directions['up']=False
            if event.key==pygame.K_s:
                directions['down']=False
        
    if directions['up']:
        rocketrect.y=rocketrect.y-1
    if directions['down']:
        rocketrect.y=rocketrect.y+1

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rocketrect.x=rocketrect.x-1
    if keys[pygame.K_d]:
        rocketrect.x=rocketrect.x+1