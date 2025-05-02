num = int(input("Enter number to check the prime number upto: "))
for i in range (2, num):
    for j in range (2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end = " ")