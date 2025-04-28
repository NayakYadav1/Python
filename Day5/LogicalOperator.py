year = int(input("Enter the year: "))
"""
checks if the year is Leap year or not
If the year is divisible by 4 and not divisible by 100, and also divisible by 400, then it is a leap year. 
"""

"""
One way 
if year % 4 == 0 and year% 400 == 0:
    print(year, "is a Leap year")
else:
    print(year, "is not a Leap year")
"""

# Another way
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap year")
else:
    print(year, "is not a Leap year")