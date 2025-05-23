#  Word with length 5 using list comprehension
words = ['Hello', 'World', 'Python', 'is', 'awesome', 'Data', 'Structures', 'Algorithms', 'are', 'fun']

new_list = [word for word in words if len(word) >= 5]

print("Words with length 5 or more: ", new_list)