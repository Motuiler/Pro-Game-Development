import pygame
import time

pygame.init()

WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
window.fill((255,0,0))
bulbon=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\bulb animation\bulb on.png')
bulbon=pygame.transform.scale(bulbon,(WIDTH,HEIGHT))
bulboff=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\bulb animation\bulb off.png')
bulboff=pygame.transform.scale(bulboff,(WIDTH,HEIGHT))
run=True
while run:
    window.blit(bulboff,(0,0))
    pygame.display.update()
    time.sleep(2)
    window.blit(bulbon,(0,0))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()