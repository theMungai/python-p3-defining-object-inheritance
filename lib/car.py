from vehicle import Vehicle

# Child class
class Car(Vehicle):
    def __init__(self,wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"