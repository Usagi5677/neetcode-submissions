class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]]+1, l)
            hashmap[s[r]] = r
            res = max(r - l + 1, res)
        return res
