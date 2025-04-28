# Fibonacci series using for loop
"""
a = 0
b = 1
print("Fibonacci series using for loop:")
for i in range(1, 11):
    print(a, end=" ")
    next_num = a + b
    i = a + b
    print(a, end=" ")
    a = b
    b = next_num
"""
    
# Fibonacci series using while loop
a = 0
b = 1
count = 0
print("\nFibonacci series using while loop:")
while count < 10:
    """
    This is the code to print the Fibonacci series using while loop.
    The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones.
    """
    print(a, end = " ")
    next_num = a + b
    a = b
    b = next_num
    count += 1