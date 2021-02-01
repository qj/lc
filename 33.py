from typing import List 

def search(nums: List[int], target: int) -> int:
    start, end = 0, len(target) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid] > nums[end]:
            if target < nums[mid] and nums[start] > target:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > nums[mid] and target < nums[start]:
                start = mid + 1
            else:
                end = mid - 1

    return -1