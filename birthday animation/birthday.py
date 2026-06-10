import pygame
import time

pygame.init()

WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
window.fill((255,0,0))
cake=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\birthday animation\Cake.jpg')
cake=pygame.transform.scale(cake,(WIDTH,HEIGHT))
card=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\birthday animation\Card.jpg')
card=pygame.transform.scale(card,(WIDTH,HEIGHT))
font=pygame.font.SysFont('jokerman',50)
text=font.render('Happy Birthday!',True,(150,150,150))
run=True
while run:
    window.blit(card,(0,0))
    window.blit(text,(70,250))
    pygame.display.update()
    time.sleep(2)
    window.blit(cake,(0,0))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()