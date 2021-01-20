from typing import List 

def max_product_path_naive(grid: List[List[int]]) -> int:
    max_product = max(paths(grid, 0, 0, 1, []))
    return max_product % 1000000007 if max_product > 0 else -1

def paths(grid: List[List[int]], r: int, c: int, current_product: int, results: List[int]) -> List[int]:
    if r == len(grid) - 1 and c == len(grid[0]) - 1: 
        results.append(current_product * grid[len(grid) - 1][len(grid[0]) - 1])
    elif r >= len(grid) or c >= len(grid[0]): 
        return
    else:
        current_product *= grid[r][c]
        paths(grid, r + 1, c, current_product, results)
        paths(grid, r, c + 1, current_product, results)
    return results

def max_product_path_bottom_up(grid: List[List[int]]) -> int:
    R, C = len(grid), len(grid[0])
    dp = [[0 for _ in range(C)] for _ in range(R)]
    dp[0][0] = grid[0][0], grid[0][0]
    for c in range(1, C):
        dp[0][c] = dp[0][c - 1][0] * grid[0][c], dp[0][c - 1][0] * grid[0][c]
    for r in range(1, R):
        dp[r][0] = dp[r - 1][0][0] * grid[r][0], dp[r - 1][0][0] * grid[r][0]
    for r in range(1, R):
        for c in range(1, C):
                upper_neighbour_min = grid[r][c] * dp[r - 1][c][0]
                upper_neighbour_max = grid[r][c] * dp[r - 1][c][1]
                left_neighbour_min = grid[r][c] * dp[r][c - 1][0]
                left_neighbour_max = grid[r][c] * dp[r][c - 1][1]
                dp[r][c] = min(upper_neighbour_min, upper_neighbour_max, left_neighbour_min, left_neighbour_max), max(upper_neighbour_min, upper_neighbour_max, left_neighbour_min, left_neighbour_max)
    return dp[R - 1][C - 1][1] % 1000000007 if dp[R - 1][C - 1][1] >= 0 else -1


if __name__ == '__main__':
    grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    print(max_product_path_bottom_up(grid))
