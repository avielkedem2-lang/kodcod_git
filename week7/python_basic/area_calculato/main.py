import rectangle
import square
import triangle
import circle
import hexagon

r1 = rectangle.Rectangle(4, 5)
s1 = square.Square(4)
t1 = triangle.Triangle(8, 6, 6, 3, 8)
c1 = circle.Circle(4)
h1 = hexagon.Hexagon(5)


shapes = [r1, s1, t1, c1, h1]
for shape in shapes:
    print(shape)

