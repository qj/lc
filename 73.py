from typing import List 

def setZeroes(matrix: List[List[int]]) -> None:
    R, C, colZero, rowZero = len(matrix), len(matrix[0]), False, False 
    for r in range(R):
        if not matrix[r][0]:
            colZero = True
            break
    for c in range(C):
        if not matrix[0][c]:
            rowZero = True 
            break
    for r in range(1, R):
        for c in range(1, C):
            if not matrix[r][c]:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(1, R):
        for c in range(1, C):
            if not matrix[r][0] or not matrix[0][c]:
                matrix[r][c] = 0
    if rowZero:
        for c in range(C):
            matrix[0][c] = 0
    if colZero:
        for r in range(R):
            matrix[r][0] = 0
    

