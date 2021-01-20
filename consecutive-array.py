# Question from https://www.byte-by-byte.com/consecutivearray/

from typing import List

def maxConsecutiveArrayLength(nums: List[int]) -> int:
    dedup = set()
    max_length = 1
    for n in nums:
        dedup.add(n)

    for n in dedup:
        if (n - 1) in dedup: continue
        length = 1
        while (n + 1) in dedup:
            length += 1
            n += 1
        max_length = max(max_length, length)
    
    return max_length