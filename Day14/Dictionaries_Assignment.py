dict = {'tile': 'The Earth', 'author': 'Alice Bob', 'year': 2021, 'genre': 'Science Fiction'}

# for key, value in dict.items():
#     print(f"{key}: {value}")

# Adding a new key-value pair
dict['publisher'] = 'XYZ Publishing'
dict['page_count'] = 350
dict['year'] = 2029

# print("\nAfter adding new key-value pairs:")
# for key, value in dict.items():
#     print(f"{key}: {value}")

# Using key, values, and items methods
# res = dict.keys()
# res = dict.values()
res = dict.items()
print(res)