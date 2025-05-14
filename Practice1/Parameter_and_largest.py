def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

largest = find_largest(10, 20, 30) 
print("The largest number is:", largest)