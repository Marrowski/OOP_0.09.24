class Car:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __str__(self):
        return f'Name of car: {self.name}, type: {self.type}'


class MotorCar(Car):
    def output_car(self):
        print('This is cars in this list:')


class Mazda(Car):
    pass

car1 = Car('Mazda','motor car')
print(car1)

car2 = MotorCar('Mazda', 'motor car')
car2.output_car()
print(car2)

print(Mazda.__mro__)