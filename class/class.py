import pygame
pygame.init()

WIDTH=500
HEIGHT=500

window=pygame.display.set_mode((WIDTH,HEIGHT))

class Vehicle():
    brand='Honda'

    def __init__(self,color,speed,people):
        self.color=color
        self.speed=speed
        self.people=people

    def move(self):
        print(f'You are driving at {self.speed}kmh')

    def accelarate(self):
        self.speed=self.speed+50

    def brake(self):
        self.speed=self.speed-50

car=Vehicle('White',200,5)
print(car.brand)
print(car.color)
print(car.speed)
print(car.people)
car.move()
car.accelarate()
car.move()

bike=Vehicle('Black',150,2)
print(bike.brand)
print(bike.color)
print(bike.speed)
print(bike.people)
bike.move()
bike.brake()
bike.move()