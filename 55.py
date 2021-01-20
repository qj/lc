from typing import List 

def canJump(nums: List[int]) -> bool:
    left_valid = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= left_valid:
            left_valid = i

    return left_valid == 0

