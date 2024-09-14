class Transport:
    def __init__(self, manufacturer: str, model: str, year: int, color: str):
        self.manufacturer: manufacturer
        self.model = model
        self.year = year
        self.color = color


class Car(Transport):
    def __init__(self, manufacturer: str, model: str, year: int, color: str, body_type: str, count_of_doors: int,
                 engine_capacity: float):

        super().__init__(manufacturer, model, year, color)
        self.body_type = body_type
        self.count_of_doors = count_of_doors
        self.engine_capacity = engine_capacity

    def car_information(self):
        return f'Motor car: {self.count_of_doors} doors, {self.body_type}, engine capacity: {self.engine_capacity}'


class Motorcycle(Transport):
    def __init__(self, manufacturer: str, model: str, year: int, color: str, bike_type: str, count_of_cylinders: int):
        super().__init__(manufacturer, model, year, color)
        self.bike_type = bike_type
        self.count_of_cylinders = count_of_cylinders

    def bike_information(self):
        return f'The motorcycle: {self.bike_type}, count of cylinders in bike: {self.count_of_cylinders}'


class Cycle(Transport):
    def __init__(self, manufacturer: str, model: str, year: int, color: str, frame_type: str, number_of_gears: int, frame_material: str):
        super().__init__(manufacturer, model, year, color)
        self.frame_type = frame_type
        self.number_of_gears = number_of_gears
        self.frame_material = frame_material

    def cycle_information(self):
        return (f'The bicycle have {self.frame_type} frame, {self.number_of_gears} gears and {self.frame_material} '
                f'frame material.')


car1 = Car('Mazda', 'Miata', 2012, 'gray', 'roadster', 2, 3500.32)
car2 = Car('Hyundai', 'Accent', 2011, 'white', 'sedan-hatchback', 4, 4400.47)
print(car1.car_information())
print(car2.car_information())

bike1 = Motorcycle('Kawasaki',  'Ninja', 2012, 'green', 'mechanical', 4)
bike2 = Motorcycle('Dnipro',  'MT-10-36', 1986, 'black', 'mechanical', 2)

print(bike1.bike_information())
print(bike2.bike_information())

cycle1 = Cycle('Crossride', 'Skyline', 2022, 'orange', 'steel', 8, 'steel')
cycle2 = Cycle('Merida','Crossway', 2023, 'gray', 'aluminium', 8, 'aluminium')

print(cycle1.cycle_information())
print(cycle2.cycle_information())
