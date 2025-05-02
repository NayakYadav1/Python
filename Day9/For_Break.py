# Using break statement in for Loop
for i in range (10):
    if i == 7:
        break
    print(i, end = " ")
print("Loop ended")

# Usin break in while Loop
while True:
    num = int(input("Enter a negative number to exit: "))
    if num < 0:
        break
print("You entered: ", num, "so loop chain breaked from here")