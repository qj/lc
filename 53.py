from typing import List, Tuple

def maxSubArray(nums: List[int]) -> int:
    max_sum, current_sum = float('-inf'), 0

    for n in nums:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)

    return max_sum

def max_subarray_indices(nums: List[int]) -> Tuple[int, int, int]:
    max_sum, current_sum = float('-inf'), 0
    best_start, best_end = 0, 0
    
    for current_end, x in enumerate(nums):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x 
        
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = current_end + 1
    
    return max_sum, best_start, best_end

