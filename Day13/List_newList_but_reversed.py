words = ['apple', 'banana', 'orange', 'blueberry', 'kiwi']

def reverse_word_list(word):
    wordPosition = words[::-1]
    reverse_Word = [word[::-1] for word in words]
    return reverse_Word, wordPosition

reverse_Word, wordPosition = reverse_word_list(words)
print('Original list: ', words)
print('Reversed list: ', reverse_Word)
print('New position list: ', wordPosition)