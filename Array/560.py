from typing import List
from collections import defaultdict 

def subarraySumBF(nums: List[List[int]], k: int) -> int:
    N, count = len(nums), 0
    for i in range(1, N + 1):
        for j in range(N - i + 1):
            if sum(nums[j: j + i]) == k:
                count += 1
    return count

def subarraySum(nums: List[List[int]], k: int) -> int:
    N, count, cache, current_sum = len(nums), 0, defaultdict(int), 0
    cache[0] = 1
    for i in range(N):
        current_sum += nums[i]
        count += cache[current_sum - k]
        cache[current_sum] += 1
    return count