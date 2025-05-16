num = int(input("Enter a number: "))
def calculate_fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
print("The factorial of ", num, "is", calculate_fact(num))