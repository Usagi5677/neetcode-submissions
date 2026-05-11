class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        hashmaptwo = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            hashmaptwo[t[i]] = hashmaptwo.get(t[i], 0) + 1

        return hashmap == hashmaptwo