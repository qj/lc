from typing import List    
    
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for c in coins:            
        for i in range(c, amount + 1):
            dp[i] = min(1 + dp[i - c], dp[i]) 
    return dp[amount] if dp[amount] != float('inf') else -1