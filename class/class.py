class Vehicle():
    brand='Honda'

    def __init__(self,color,speed,people):
        self.color=color
        self.speed=speed
        self.people=people

car=Vehicle('White',200,5)
print(car.brand)
print(car.color)
print(car.speed)
print(car.people)

bike=Vehicle('Black',150,2)
print(bike.brand)
print(bike.color)
print(bike.speed)
print(bike.people)