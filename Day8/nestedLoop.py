# Printing a multiplication table for number 1 to 5 using nested for loop
i = 1
j = 1
for i in range(1, 6):
    print("Multiplication table for: ", i)
    for j in range(1, 11):
        """
        This is a nested loop that iterates from 1 to 10 and prints the multiplication table for the current value of i.
        The outer loop iterates from 1 to 5, and for each value of i, the inner loop iterates from 1 to 10.
        """
        print(i, "x", j, "=", i * j)
    print("\n") 