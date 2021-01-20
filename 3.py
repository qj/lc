def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    max_len, i, j = 0, 0, 0
    
    while j < len(s):
        if s[j] in seen:
            seen.remove(s[i])
            i += 1
        else:
            seen.add(s[j])
            j += 1
            max_len = max(max_len, len(seen))
    
    return max_len
