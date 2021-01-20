from typing import List 

def length_of_LICS(nums: List[int]) -> int:
    if not nums:
        return 0
    curr_length, max_length = 1, 1

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 1
    
    return max_length