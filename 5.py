def longestPalindrome(s: str) -> str:

    def LP(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1 
        return s[l + 1: r]
    
    maxstr = ""

    for i in range(len(s)):
        lp = LP(i, i)
        if len(lp) > len(maxstr): maxstr = lp 
        lp = LP(i, i + 1)
        if len(lp) > len(maxstr): maxstr = lp 
    
    return maxstr