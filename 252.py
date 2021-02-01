from typing import List 

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    if not intervals:
        return True
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    last = sorted_intervals[0]
    for (s, e) in sorted(intervals, key=lambda x: x[0])[1:]:
        if s < last[1]:
            return False
        last = s, e 
        
    return True 