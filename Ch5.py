class Car:
    def __init__(self):
        self.speed = 0
        self.minSpeed = 0


class SportCar(Car):
    ### code here ###
    def __init__(self):
        super().__init__()
        self.max_speed = 200
        self.speedValue = 45

    def speed_up(self):
        if self.speed + self.speedValue > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.speedValue
        print("Sport Car의 현재 속도: ", self.speed)

    def speed_down(self):
        if self.speed - self.speedValue < self.minSpeed:
            self.speed = self.minSpeed
        else:
            self.speed -= self.speedValue
        print(f"Sport Car의 현재 속도: {self.speed}")

    ### code here ###


class Truck(Car):
    ### code here ###
    def __init__(self):
        super().__init__()
        self.max_speed = 100
        self.speedValue = 15
        self.cargo = 0
        self.minCargo = 0
        self.maxCargo = 50

    def speed_up(self):
        if self.speed + self.speedValue > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.speedValue
        print("Truck의 현재 속도: ", self.speed)

    def speed_down(self):
        if self.speed - self.speedValue < self.minSpeed:
            self.speed = self.minSpeed
        else:
            self.speed -= self.speedValue
        print("Truck의 현재 속도: ", self.speed)

    def update_cargo(self, value):
        if (self.cargo + value) < self.minCargo:
            self.cargo = self.minCargo
        elif (self.cargo + value) > self.maxCargo:
            self.cargo = self.maxCargo
        else:
            self.cargo += value

        print("Truck의 현재 적재 화물량: ", self.cargo)

    ### code here ###


sport_car = SportCar()
truck = Truck()
sport_car.speed_up()
sport_car.speed_down()
truck.speed_up()
truck.speed_down()
truck.update_cargo(10)
truck.update_cargo(60)
truck.update_cargo(-20)
truck.update_cargo(-60)
