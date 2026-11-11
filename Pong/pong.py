import pygame
pygame.init()

WIDTH=1000
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))
paddle=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Pong\assets\paddle.png')
paddle=pygame.transform.scale(paddle,(20,50))
ball=pygame.image.load(r'C:\Users\Ekaansh\Desktop\Coding Jetlearn\Pro Game Development\Pong\assets\ball.png')
ball=pygame.transform.scale(ball,(30,30))

run=True
while run:
    window.blit(paddle,(0,0))
    window.blit(ball,(500,250))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

    pygame.display.update()