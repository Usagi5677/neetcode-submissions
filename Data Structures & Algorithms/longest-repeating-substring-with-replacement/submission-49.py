class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = maxf = res = 0
        for r in range(len(s)):
            c = s[r]
            hm[c] = hm.get(c, 0) + 1
            maxf = max(hm[c],maxf)
            if (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r -l + 1)
        return res