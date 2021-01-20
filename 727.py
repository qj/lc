class Solution:

    def minWindow(self, S: str, T: str) -> str:
        l, m, minLen, res = 0, 0, float("inf"), ""

        for r in range(len(S)):
            if S[r] == T[m]:
                m += 1

            while m == len(T):
                if len(S[l: r + 1]) < minLen:
                    minLen = len(S[l: r + 1])
                    res = S[l: r + 1]
                
        return res if minLen < float("inf") else ""