my_dict = {'name': 'Nayak', 'age': 24, 'location': 'Nepal'}
# print(my_dict)
# print(my_dict['name']) # Access value using the key

# To access the value associated with a key
# my_dict['addess'] = 'Handigaun'
# my_dict['college'] = 'NIST'
# print(my_dict)

# Remove a key-value pair
# del my_dict['college']
# print(my_dict)

# Remove using pop
# my_dict.pop('addess')
# print(my_dict)

for key, value in my_dict.items():
    print(f"{key}: {value}")