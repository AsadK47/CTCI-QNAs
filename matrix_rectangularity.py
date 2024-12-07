# Checks if a matrix is rectangular or not

def is_rectangular(matrix):
  if not matrix:
    return True # An empty matrix is considered rectangular
  num_cols = len(matrix[0])
  return all(len(row) == num_cols for row in matrix)

# Rectangular
matrix_one = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

# Jagged array
matrix_two = [
  [1, 2, 3],
  [4, 5],
  [6, 7, 8, 9],
]

print(is_rectangular(matrix_one))
print(is_rectangular(matrix_two))