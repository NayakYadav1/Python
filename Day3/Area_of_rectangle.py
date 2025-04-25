def area(length, width):
    """
    This function calculate the area of the rectangle.
    """
    return length * width

length = float(input("Enter the length og the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_of_rectangle = area(length, width)

print("The area of the rectangle is: ", area_of_rectangle)