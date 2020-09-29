class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model 
        self.top_speed = top_speed

    def start(self):
        return "Brmmm, Brmmm. I can go at " +str(self.top_speed)

# new instance of car
new_car = Car("Ford", "Fiesta", 60)

print (new_car.make)
print (new_car.start())