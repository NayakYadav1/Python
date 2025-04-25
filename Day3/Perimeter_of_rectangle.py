def perimeter(length, width):
    """
    This Function calculate the perimeter of the rectangle 
    Taking Length and width as input
    """
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter_of_rectangle  = perimeter(length, width)

print("The perimeter of the rectangle is: ", perimeter_of_rectangle)