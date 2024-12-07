def zero_matrix(matrix):
  if not matrix or not matrix[0]:
    return # Edge case: empty matrix
  
  # Initialize sets to store rows and columns to be zeroed
  zero_rows = set()
  zero_cols = set()

  # Step 1: Identify the rows and columns to zero
  rows, cols = len(matrix), len(matrix[0])
  for i in range(rows):
    for j in range(cols):
      if matrix[i][j] == 0:
        zero_rows.add(i)
        zero_cols.add(j)

  # Step 2: Zero the rows
  for i in zero_rows:
    for j in range(cols):
      matrix[i][j] = 0

  # Step 3: Zero the columns
  for j in zero_cols:
    for i in range(cols):
      matrix[i][j] = 0
  
  return matrix

matrix = [
  [1, 2, 3],
  [4, 0, 6],
  [7, 8, 9]
]

result = zero_matrix(matrix)
for row in result:
  print(row)
