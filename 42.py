from typing import List

def find_next_i(hgt: int, index: int, heights: List[int]) -> int:
    # return the index of the first block taller than or equal to given hgt
    # if this doesn't exist return the index of the first occurence of the max height
    current_max, max_index = float('-inf'), None 
    while index < len(heights):
        if heights[index] >= hgt:
            return index
        if heights[index] > current_max:
            current_max, max_index = heights[index], index
        index += 1
    return max_index

def trap(heights: List[int]) -> int:
    total, i = 0, 0

    # Skip any 0's at beginning of array
    while i < len(heights) and heights[i] == 0:
        i += 1

    while i < len(heights):
        next_i = find_next_i(heights[i], i + 1, heights)
        if next_i:
            total += min(heights[i], heights[next_i]) * (next_i - i - 1)
            for j in range(i + 1, next_i):
                total -= heights[j]
            i = next_i
        else:
            i += 1
    return total


if __name__ == '__main__':
    heights = [3, 2, 1, 2, 3]
    assert trap(heights) == 4