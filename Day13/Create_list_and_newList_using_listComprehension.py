words = ['apple', 'banana', 'orange', 'blueberry', 'kiwi']
# length = []
# for word in words:
#     length.append(len(word))

length = [len(word) for word in words]

print('Original list: ', words)
print('Length of each word: ', length)