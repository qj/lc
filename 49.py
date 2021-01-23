from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for s in strs: 
        key = "".join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

"""
Time complexity: O(n k log k) where n is the number of strings and k is the length of the longest string
Space complexity: O(n * k) 
"""