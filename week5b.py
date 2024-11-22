# Parent class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create instances of both classes
vehicle1 = Car()
vehicle2 = Plane()

# Demonstrating polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Calling the same method (move) on different objects
demonstrate_movement(vehicle1)  # Output: Driving 🚗
demonstrate_movement(vehicle2)  # Output: Flying ✈️
