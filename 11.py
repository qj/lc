from typing import List 

def maxArea(height: List[int]) -> int:
    left, right, max_area = 0, len(height) - 1, 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area