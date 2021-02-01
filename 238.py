from typing import List 

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1 for _ in range(n)]
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    factor = 1
    for i in range(-1, -n - 1, -1):
        result[i] *= factor 
        factor *= nums[i]
    return result 