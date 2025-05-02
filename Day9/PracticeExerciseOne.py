sum = 0
while True:
    """
    This Loop will continue to ask age of the user and sums it as soon as the user 
    enter's a negative number the loop will terminate and the sum of the age will be printed
    """
    age = int(input("Enter your age: "))
    if age < 0:
        break
    else:
        sum = sum + age
print("The sum of your age is: ", sum)