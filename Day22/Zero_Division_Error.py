try:
    result = 10 / 2
except ZeroDivisionError as e:
    # print("Cannot divide by zero!")
    print(f"Error: {e}")
else:
    print("Division successful, result is:", result)
finally:
    print("Cleaning up resources.")