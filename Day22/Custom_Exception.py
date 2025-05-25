class NegativeNumberError(Exception):
    """Raised when the age is negative"""
    pass

num = -2
if num < 0:
    raise NegativeNumberError("Negative numbers are not allowed.")