# create a flatten list from the nested list (e.g., matrix)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten = [num for row in matrix for num in row]
# print(flatten)

# Create a transpose of given matrix which means convert column into rows
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [list(row) for row in zip(*matrix)]
print(transpose)