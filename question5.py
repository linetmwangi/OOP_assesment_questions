from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display_message(self):
        return "This is an abstract class"

class Rectangle(Shape):
    def __init__(self, width, height=None):
        # Simulate constructor overloading: If height is not provided, make it a square (width = height)
        if height is None:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

# Create a square (one parameter provided)
square = Rectangle(10)
print("Square Area:", square.area())  # Expected output: 100
print(square.display_message())

# Create a rectangle (two parameters provided)
rectangle = Rectangle(10, 20)
print("Rectangle Area:", rectangle.area())  # Expected output: 200
print(rectangle.display_message())
