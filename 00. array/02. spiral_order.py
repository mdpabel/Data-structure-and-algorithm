""" 
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[1,2,3,6,9,8,7,4,5,6]

"""


def spiral_order(matrix):
    linear_arr = []

    m = len(matrix)
    if m == 0:
        return linear_arr
    n = len(matrix[0])

    key = 0

    while True:
        # left to right
        if key == 0:
            for i in range(0, n+1):
                linear_arr.append(matrix[0][i])
            key += 1
        # top to bottom
        if key == 1:
            for i in range(1, m+1):
                linear_arr.append(matrix[i][m-1])
            key += 1
        # right to left
        if key == 2:
            for i in range(n - 2, 1):
                linear_arr.append(matrix[i][m-1])
            key += 1
        # bottom to top
        if key == 3:
            pass
