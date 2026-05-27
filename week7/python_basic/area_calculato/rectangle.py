import calculator

class Rectangle(calculator.Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    

    def get_area(self):
        return self.height * self.width
    

    def get_perimeter(self):
        return 2 * (self.height + self.width)
    

    def __str__(self):
        return f"Shape: rectangle, area: {self.get_area()}, perimeter: {self.get_perimeter()}"
    