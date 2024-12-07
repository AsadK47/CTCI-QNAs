def rotate_matrix(matrix):
    N = len(matrix)  # Assuming it's an NxN matrix

    # Perform the layer-by-layer rotation
    for layer in range(N // 2):  # Only iterate through half the layers
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            # Calculate the offset within the layer
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix=matrix))