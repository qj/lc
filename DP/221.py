from typing import List 

def maximalSquare(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    max_length, R, C = 0, len(matrix), len(matrix[0])

    # convert matrix into ints

    for r in range(R):
        for c in range(C):
            matrix[r][c] = int(matrix[r][c])
            max_length = max(max_length, matrix[r][c])

    for r in range(1, R):
        for c in range(1, C):
            if matrix[r][c]:
                matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                max_length = max(max_length, matrix[r][c])

    return max_length * max_length