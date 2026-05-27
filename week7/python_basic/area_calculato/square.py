import rectangle

class Square(rectangle.Rectangle):
    def __init__(self,width, height, side):
        super().__init__(width, height)
        self.side = side
    
    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return f"Shape: square, area: {self.get_area()}, perimeter: {self.get_perimeter()}"
    