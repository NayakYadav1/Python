def sum_number(firstNum, secondNum):
    sum = firstNum + secondNum
    return sum

firstNum = int(input("Enter the first number: "))
secondNum = int(input('Enter the second number: '))

res = sum_number(firstNum, secondNum)

print("Your result is: ", res)