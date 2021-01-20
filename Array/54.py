from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    result = []
    direction = (0, 1)
    m, n, offset, i, j  = len(matrix), len(matrix[0]), 1, 0, 0
    if m == 1:
        return matrix[0]
    if n == 1:
        return [matrix[i][0] for i in range(m)]

    for _ in range(m * n):
        result.append(matrix[i][j])
        i, j = i + direction[0], j + direction[1]
        if i == offset - 1 and j == n - offset:
            direction = (1, 0)
        elif i == m - offset and j == n - offset:
            direction = (0, -1)
        elif i == m - offset and j == offset - 1:
            direction = (-1 , 0)
        elif i == offset and j == offset - 1:
            direction = (0, 1)
    
    return result 