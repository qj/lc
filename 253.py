from typing import List
import heapq 

def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    rooms = []
    intervals = sorted(intervals, key=lambda x: x[0])
    heapq.heappush(rooms, intervals[0][1])
    for intervals in intervals[1:]:
        if rooms[0] <= intervals[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, intervals[1])
    return len(rooms)