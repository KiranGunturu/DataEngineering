class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model
        self.speed = 0

    def accelerate(self, increment):
        self.speed = self.speed + increment

    def brake(self, decrement):
        self.speed = self.speed - decrement

    def stop(self):
        self.speed = 0
        print("car is stopped")


car1 = Car("nissan", "RAV", 2020)
car2 = Car("Tesla", "Y", 2020)
car1.accelerate(10)
print(car1.speed)
print(car2.speed)
car1.stop()


#https://t.me/+HdbH-Gpb0zs1OTdl
