class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm, hm2 = {}, {}

        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
            hm2[t[i]] = hm2.get(t[i], 0) + 1
        
        return hm == hm2