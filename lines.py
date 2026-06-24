import pygame

WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Draw')
window.fill((255,255,255))
run=True
draw=False

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            startpos=pygame.mouse.get_pos()
            #draw=True
        if event.type==pygame.MOUSEBUTTONUP:
            endpos=pygame.mouse.get_pos()
            pygame.draw.line(window,(0,0,0),startpos,endpos,5)
    pygame.display.update()