from typing import List 

def permutations(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        for p in permutations(nums[:i] + nums[i + 1:]):
            p.append(nums[i])
            result.append(p)
    return result 