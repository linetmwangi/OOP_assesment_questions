class Engine:
    def __init__(self):
        self.is_running = False 

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()

    def start_engine(self):
        print(f"{self.make} {self.model} is trying to start the engine.")
        self.engine.start()

    def stop_engine(self):
        print(f"{self.make} {self.model} is trying to stop the engine.")
        self.engine.stop()

# Usage
my_car = Car("Toyota", "Camry")
my_car.start_engine()
my_car.stop_engine()