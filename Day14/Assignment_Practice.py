# First 10 cubes from list
# cubes = [num ** 3 for num in range(1, 11)]
# print(cubes)

# list with the uppercase letter 
# words = ['apple', 'nayak', 'yadav', 'orange', 'kiwi']
# upper = [word.upper() for word in words]
# print(upper)

# Condition - Based List Comprehension
# nums = [12, 4, 5, 87, -1, 48, -57, -3, 100]
# positive = [num for num in nums if num >= 0]
# positive.sort()
# print(positive)

# Given a list of words create a list of word that start with a vowel
# words = ['apple', 'nayak', 'yadav', 'orange', 'kiwi', 'imigrant', 'owl', 'elephant', 'urus']
# vowels = 'aeiou'
# vowel = [word for word in words if word[0].lower() in 'aeiou']
# count_vowel = sum(1 for word in words for char in word.lower() if char in vowels)
# print("list with starting vowel :", vowel)
# print("Count the number or vowel in word :", count_vowel)

# Flatten the matrix
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)

# Transpose matrix
matrix = [[1, 2], [3, 4], [5, 6]]
transpose = [list(row) for ]