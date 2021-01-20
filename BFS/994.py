from collections import deque
from typing import List 

EMPTY = 0
FRESH = 1
ROTTEN = 2


def orangesRotting(grid: List[List[int]]) -> int:
    # Determine number of fresh oranges and initialise queue to contain rotten oranges
    fresh = 0
    queue = deque()
    turns = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == FRESH:
                fresh += 1
            elif grid[r][c] == ROTTEN:
                queue.append((r, c))
    if not fresh:
        return 0
    while queue:
        for _ in range(len(queue)):
            rr, rc = queue.popleft()
            for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = rr + dr, rc + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == FRESH:
                        fresh -= 1
                        grid[nr][nc] = ROTTEN
                        queue.append((nr, nc))
        turns += 1
    return turns - 1 if fresh == 0 else -1


if __name__ == '__main__':
    pass