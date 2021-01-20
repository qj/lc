from typing import List 

def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged = []

    if not intervals:
        return merged 

    i, j, N = 0, 1, len(intervals)

    intervals = sorted(intervals, key=lambda i: i[0])

    while i < N:
        max_upper = intervals[i][1]

        while j < N and intervals[j][0] <= max_upper:
            max_upper = max(max_upper, intervals[j][1])
            j += 1
        
        merged.append([intervals[i][0], max_upper])
        i = j
        j = i + 1
    
    return merged

def merge2(intervals: List[List[int]]) -> List[List[int]]:
    merged = []

    for interval in sorted(intervals, key=lambda i: i[0]):
        if merged and merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged