from typing import List 

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
"""

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def search(candidate: List[int], index: int):
        total = sum(candidate)
        if total > target:
            return
        if total == target:
            result.append(candidate)
        else:
            for j in range(index, len(candidates)):
                search(candidate + [candidates[j]], j)

    for i in range(len(candidates)):
        search([candidates[i]], i)

    return result

def combinationSumRefactor(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    dfs(result, 0, [], candidates, target)
    return result  

def dfs(result: List[List[int]], current_sum: int, candidate: List[int], candidates: List[int], target: int):
    if current_sum == target:
        result.append(candidate)
    else:
        for i, n in enumerate(candidates):
            if current_sum + n > target:
                return
            dfs(result, current_sum + n, candidate + [n], candidates[i:], target)

if __name__ == '__main__':
    print(combinationSum([2,3,6,7], 7))