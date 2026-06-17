import pygame
import random 
pygame.init()

WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Draw')
window.fill((255,255,255))
run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(window,(0,0,0),pos,5)
        if event.type==pygame.MOUSEBUTTONDOWN:
            window.fill((255,255,255))
        if event.type==pygame.MOUSEBUTTONUP:
            window.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.update()