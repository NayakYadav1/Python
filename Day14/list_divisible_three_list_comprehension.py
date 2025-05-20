# divisible = [int(i) for i in range(1, 21) if i % 3 == 0]
# print(divisible)

# List of first 10 even number
# even_num = [num for num in range (20) if num % 2 == 0]
# print(even_num)

# list of fruits that contain letter 'a' in list of fruits
fruits = ['apple', 'kiwi', 'orange', 'banana', 'avocado', 'pineapple', 'watermelon', 'Aamba'] 
# contains = [fruit for fruit in fruits if 'a' in fruit or 'A' in fruit] # use this explicitly
contains = [fruit for fruit in fruits if 'a' in fruit.lower()] # use this if we want to check regardless of case converting every a to lower and check
print(contains)