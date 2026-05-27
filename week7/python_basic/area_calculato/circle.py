import calculator
import math

class Circle(calculator.Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"shape: circle, area: {self.get_area()}, perimeter: {self.get_perimeter()}"