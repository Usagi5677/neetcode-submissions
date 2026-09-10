class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = l = maxf = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxf = max(maxf, hm[s[r]])
            if (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
        return len(s) - l