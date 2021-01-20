from typing import List 

def searchMatrix(matrix: List[List[int]], target: int) -> bool: 
    if not matrix:
        return False 
    R, C = len(matrix), len(matrix[0])
    r, c = 0, C - 1

    while r < R and c >= 0:
        if matrix[r][c] == target:
            return True 
        if matrix[r][c] < target:
            r += 1
        else:
            c -= 1
    return False