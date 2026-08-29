class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hm = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            if c in hm:
                l = max(l , hm[c] + 1)
            hm[s[r]] = r
            res = max(res, r - l + 1)
        return res
        