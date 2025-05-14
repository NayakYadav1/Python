def Max_Min(numbers):
    """
    This dunction takes the list of numbers and print the max and muin number from the list.
    """
    return max(numbers), min(numbers)

max, min = Max_Min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Max number is: ", max)
print("Min number is: ", min)