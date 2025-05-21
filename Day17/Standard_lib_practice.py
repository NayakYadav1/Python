# circumference of a circle
# import math
# def circumference(radius):
#     return 2 * math.pi * radius
# radius = 20
# print(f"The circumference of a circle with radius {radius} is {circumference(radius)}")

# Difference in days between two dates
# import datetime
# def diff_two_days(date1, date2):
#     date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
#     date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
#     return abs((date2 - date1).days)

# print(diff_two_days('2001-07-30', '2025-05-21'))

# os module to create a directory and list files
import os

directory_name = "test_directory"

if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created")
else:
    print(f"Directory '{directory_name}' already exists")

files = os.listdir(directory_name)

if files:
    for file in files:
        print(f"File: {file}")
else:
    print(f"No files found in '{directory_name}'")