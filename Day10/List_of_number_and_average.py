def average(numbers):
    """
    This function takes a list of numbers and returns the average.
    """
    return sum(numbers) / len(numbers)

result = average([1, 2, 3, 4, 5])
print("The average of the list is: ", result)