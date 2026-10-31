class vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class car(vehicle):
    def __init__(self, brand, year, seat):
        super().__init__(brand, year)
        self.seat = seat

    def info(self):
        return f"Car: {self.brand}, Year: {self.year}, Seat: {self.seat}"

class motorcycle(vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc

    def info(self):
        return f"Motorcycle: {self.brand}, Year: {self.year}, cc: {self.cc}"

class bicycle(vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        return f"Bicycle: {self.brand}, Year: {self.year}, Model: {self.model}"

vehicles = []

while True:
    line = input().split()
    if not line:
        continue

    v = line[0]

    if v == "stop":
        break
    elif v == "print":
        for i in vehicles:
            print(i.info())
    elif v == "Car":
        brand, year, seat = line[1], line[2], line[3]
        vehicles.append(car(brand, year, seat))
    elif v == "Motorcycle":
        brand, year, cc = line[1], line[2], line[3]
        vehicles.append(motorcycle(brand, year, cc))
    elif v == "Bicycle":
        brand, year, model = line[1], line[2], line[3]
        vehicles.append(bicycle(brand, year, model))