with open('Day20/data.txt', 'a') as file:
    file.write('\nThis is a new line added to the file using append mode.')

with open('Day20/data.txt', 'r') as file:
    content = file.read()
    print(content)