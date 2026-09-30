import pygame
pygame.init()

WIDTH=500
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))

class Rect():
    def __init__(self,size,colour):
        self.size=size
        self.colour=colour

    def draw(self):
        pygame.draw.rect(window,self.colour,self.size)

rect1=Rect((30,30,50,50),(124,183,96))
rect1.draw()

rect2=Rect((100,100,100,100),(93,223,153))
rect2.draw()

pygame.display.update()
        





    


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
