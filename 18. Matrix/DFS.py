#top, right, bottom, left
directions = [
    [-1, 0],  # row, col
    [0, 1],
    [1, 0],
    [0, -1]
]


def dfs(matrix, row, col, seen, values):
    isCorrectDirection = row < 0 or col < 0 or row >= len(
        matrix) or col >= len(matrix[0])
    isSeen = seen[row][col]

    if isCorrectDirection or isSeen:
        return

    seen[row][col] = True
    values.append(matrix[row][col])

    for direction in directions:
        dfs(matrix, row + direction[0], col + direction[1], seen, values)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


seen = [
    [False for _ in matrix[0]] for _ in matrix
]

values = []

dfs(matrix, 0, 0, seen, values)

print(values)
