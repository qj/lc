"""
1578. Minimum Deletion Cost to Avoid Repeating Letters
Medium

Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.


Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
"""

from typing import List 

def solve(s: str, cost: List[int]) -> int:
    min_cost, i = 0, 0

    while i < len(s) - 1:
        max_cost_for_letter = 0
        while i + 1 < len(s) and s[i] == s[i + 1]:
            max_cost_for_letter = max(max_cost_for_letter, cost[i])
            min_cost += cost[i]
            i += 1
        if max_cost_for_letter:
            min_cost = min_cost + cost[i] - max(max_cost_for_letter, cost[i])
        else:
            i += 1
    return min_cost



if __name__ == '__main__':
    s, cost = "abaac", [1, 2, 3, 4, 5]
    assert solve(s, cost) == 3 
    s, cost = "abc", [1, 2, 3]
    assert solve(s, cost) == 0 
    s, cost = "aabaa", [1, 2, 3, 4, 1]
    assert solve(s, cost) == 2
    solve("aaaab", [5,4,3,2,1])