# Continue in for loop
for i in range (10):
    """"    
    This is a loop that continues to iterate until it reaches to 10
    But when continue is used if still iterates but skips the value when i == 5
    """
    if i == 5:
        continue
    print(i, end = " ")

# Using continue in while Loop
i = 0
while i < 11:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end = " ") 