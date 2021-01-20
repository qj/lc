from collections import defaultdict 
from typing import List 

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)

    for (a, b) in prerequisites:
        graph[b].append(a)

    state = [0] * numCourses

    def is_cycle(node):
        if state[node] == 1:
            return False 
        if state[node] == -1:
            return True
        for n in graph[node]:
            if is_cycle(n):
                return True 
        state[node] = 1
        return False 
          
    for n in range(numCourses):
        if is_cycle(n):
            return False 
    return True 

if __name__ == '__main__':
    # canFinish(3, [[1, 0], [2, 1], [2, 0]])
    # canFinish(3, [[1, 0], [0, 2], [2, 1]])
    canFinish(3, [[1, 0], [2, 1], [2, 0]])