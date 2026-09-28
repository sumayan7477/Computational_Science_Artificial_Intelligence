def print_menu():
    """Prints the menu options for calculating areas."""
    print("\nCompute the area of:")
    print("1) a circle")
    print("2) a rectangle")
    print("3) a triangle")
    print("4) quit")
    return int(input("Enter your choice:\n"))

def circle_area(r):
    """Calculates the area of a circle."""
    return 3.14159 * r**2

def rectangle_area(w, h):
    """Calculates the area of a rectangle."""
    return w * h

def triangle_area(a, b, c):
    """Calculates the area of a triangle using Heron's formula."""
    s = (a + b + c) / 2
    return square_root(s*(s-a)*(s-b)*(s-c))

def square_root(x):
    """Calculates the square root of a number."""
    return x**0.5

# Main program loop
while True:
    choice = print_menu()  # Get the user's choice

    if choice == 1:  # Circle
        radius = float(input("Give the radius of a circle:\n"))
        area = circle_area(radius)
        print("The area of this circle is:", round(area,2))

    elif choice == 2:  # Rectangle
        width = float(input("Give the width of a rectangle:\n"))
        height = float(input("Give the height of a rectangle:\n"))
        area = rectangle_area(width, height)
        print("The area of this rectangle is:", round(area,2))

    elif choice == 3:  # Triangle
        print("Give the three sides of a triangle.")
        s1 = float(input("Side 1:\n"))
        s2 = float(input("Side 2:\n"))
        s3 = float(input("Side 3:\n"))
        area = triangle_area(s1, s2, s3)
        print("The area of this triangle is:", round(area,2))

    elif choice == 4:  # Quit
        print("Bye!")
        break

    else:  # Invalid choice
        print("Oops! No such choice.")
