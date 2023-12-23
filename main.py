from abstract_class import Vehicle

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print(f"Start with Kick")


class Scooty(Vehicle):
    def __init__(self, n):
        super().__init__(n)
        self.no_of_tyres = 2

    def start(self):
        print("Self start")


class Car(Vehicle):
    def __init__(self, n, x):
        super().__init__(n)
        self.no_of_gears = 5
        
    def start(self):
        print("Start with Key")



