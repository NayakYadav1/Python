number = [1, 5, 7, 9, 12, 15, 16, 19, 22, 55, 78, 99]
for num in number:
    if num % 3 == 0:
        continue
    if num > 20:
        break
    print(num, end = " ")