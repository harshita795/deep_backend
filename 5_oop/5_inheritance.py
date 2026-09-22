# Inheritance
# A child class can reuse properties and methods from a parent class.
# The child can also add its own behavior.


class Vehicle:
    def __init__(self, brand: str, speed: int) -> None:
        self.brand = brand
        self.speed = speed

    def move(self) -> None:
        print(f"{self.brand} is moving")


class Car(Vehicle):
    def __init__(self, brand: str, speed: int, doors: int) -> None:
        super().__init__(brand, speed)
        self.doors = doors

    def honk(self) -> None:
        print("Beep!")


car = Car("Toyota", 120, 4)

car.move()
car.honk()
print(car.doors)

# super() calls functionality from the parent class.
# One parent class can be reused by multiple child classes.

class Bike(Vehicle):
    def ring_bell(self) -> None:
        print("Ring ring!")


bike = Bike("Yamaha", 80)

bike.move()
bike.ring_bell()


#! When to use inheritance
# Use inheritance when the child class is always a type of the parent class.
# Example: Car is always a Vehicle.
#
# Avoid inheritance just to share a few functions.
# If two classes only share some behavior, prefer shared functions
# or another suitable design instead.



#! Inheritance hierarchy
# Inheritance can continue across multiple levels.
# Each child becomes a more specific type of its parent.
#
# Keep inheritance hierarchies simple.
# Deep or unnecessary inheritance can make code harder to understand and maintain.


class Vehicle:
    pass


class Car(Vehicle):
    pass


class ElectricCar(Car):
    pass


#! Wide vs Deep Inheritance
# Prefer simple, wide inheritance hierarchies over deeply nested ones.
# A base class can have several specific child classes.
# Very deep inheritance chains can make code harder to understand and maintain.