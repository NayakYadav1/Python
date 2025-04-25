def say_day(number):
    """
    This function takes a number as input and retuns a string indicating which day of the week it is.
    """
    if number == 1:
        """If number is 1, return 'Sunday' """
        return 'Sunday'
    elif number == 2:
        """If num is 2, return Monday"""
        return 'Monday'
    elif number == 3:
        """If num is 3, return Tuesday"""
        return 'Tuesday'
    elif number == 4:
        """If num is 4, return Wednesday"""
        return 'Wednesday'
    elif number == 5:   
        """If num is 5, return Thursday"""
        return 'Thursday'
    elif number == 6:
        """If num is 6, return Friday"""
        return 'Friday'
    elif number == 7:
        """If num is 7, return Saturday"""
        return 'Saturday'
    else:
        """If num is not in the range of 1-7, return 'Invalid number' """
        return 'Invalid number'

number = int(input("Enter a number between 1 and 7: "))
print(say_day(number))
