import rectangle
import square
import triangle
import circle
import hexagon


def menu():
    print("For rectangle press 1")
    print("For square press 2")
    print("For triangle press 3")
    print("For circle press 4")
    print("For hexagon press 5")
    print("for exit press 0")


def troubleshooter(*nums):
    for num in nums:
        if num < 1:
            print("you cna't put a number below 0 or 0")
            return False
    return True


def main():
    menu()
    my_choice = input("my choice ")
    try:
        if my_choice == "1":
            height = int(input("Enter height "))
            width = int(input("Enter width "))
            if troubleshooter(height, width):
                print(rectangle.Rectangle(height, width))
        
        elif my_choice == "2":
            side = int(input("Enter side "))
            if troubleshooter(side):
                print(square.Square(4))
        
        elif my_choice == "3":
            height = int(input("Enter height "))
            base = int(input("Enter base "))
            side_a = base
            side_b = int(input("Enter side b "))
            side_c = int(input("Enter side c "))
            if troubleshooter(height, base, side_b, side_c):
                print(triangle.Triangle(height, base, side_a, side_b, side_c))
        
        
        elif my_choice == "4":
            radius = int(input("Enter radius"))
            if troubleshooter(radius):
                print(circle.Circle(radius))
        
        elif my_choice == "5":
            side = int(input("Enter side "))
            if troubleshooter(side):
                print(hexagon.Hexagon(side))
        
        else:
            print("you need to put a number from the list!")

        
    except ValueError as e:
        print(f"you need to put a number! {e}")


main()
