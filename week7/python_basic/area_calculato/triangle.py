import rectangle

class Triangle(rectangle.Rectangle):
    def __init__(self, height, base, side_a, side_b, side_c):
        super().__init__(width= base, height=height)
        self.height = height
        self.base = base
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def get_area(self):
        return super().get_area() / 2
    
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def __str__(self):
        return f"shape: triangle, area: {self.get_area()}, perimeter: {self.get_perimeter()}"
