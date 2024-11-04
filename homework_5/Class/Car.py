class Car:
    def __init__(self, yearModal: int, make: str):
        self.yearModal = yearModal
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

a = Car(1999, "Nexia")

a.accelerate()
a.accelerate()
a.accelerate()
a.accelerate()
print(a.speed)