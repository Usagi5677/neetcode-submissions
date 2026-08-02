class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hs = {}

        for r in range(len(s)):
            if s[r] in hs:
                l = max(l, hs[s[r]] + 1)
            hs[s[r]] = r
            res = max(res, r - l + 1)
        return res