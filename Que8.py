def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # Traverse rightmost column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Check if there are more rows or columns to traverse
        if top <= bottom:
            # Traverse bottom row
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse leftmost column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = spiral_order(matrix)
print(result)
