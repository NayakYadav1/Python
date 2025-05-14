def analyze_numbers(numbers):
    add = sum(numbers)
    count = len(numbers)
    average = add / count 
    return add, count, average

total, count, average = analyze_numbers([1, 2, 3, 4, 5])
print('Total:', total)
print('Count:', count)
print('Average:', average)