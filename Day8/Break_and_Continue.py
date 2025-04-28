# Simple usecase of break in Loop
for i in range (1, 11):
    if i == 5:
        """
        This is a conditional statement that checks if the current value of i is equal to 5.
        If it is, the loop will stop execution of the current iteration
        """
        break
    print(i)

# Usecase of continue in Loop
for i in range(1, 11):
    if i == 5:
        """
        This is a conditional statement that checks if the current value of i is equal to 5.
        If it is, the loop will skip the current iteration and continue with the next iteration.
        """
        continue
    print(i)