from typing import List 

def knapsack(items: List[tuple], W: int) -> int:
    # Create dp array
    # dp[i][w] represents max value considering items up to item i with maximum allowed weight w
    # Note that item 0 means considering NO items
    dp = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]

    for i, item in enumerate(items):
        w_i, v_i = item
        for w in range(1, W + 1):
            if w_i > w:
                dp[i + 1][w] = dp[i][w]
            else:
                dp[i + 1][w] = max(dp[i][w - w_i] + v_i, dp[i][w])
    return dp[len(items)][W]


if __name__ == '__main__':
    items = [(1, 6), (2, 10), (3, 12)]
    W = 5
    print(knapsack(items, W))