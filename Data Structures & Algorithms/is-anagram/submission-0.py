class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapx = {}
        hashmapy = {}
        
        for i in range(len(s)):
            hashmapx[s[i]] = hashmapx.get(s[i],0)+1
            hashmapy[t[i]] = hashmapy.get(t[i],0)+1
        
        return hashmapx == hashmapy
        

            