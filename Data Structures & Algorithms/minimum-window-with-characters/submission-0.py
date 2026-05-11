class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        hashmapt = {}
        hashmapw = {}

        for c in t:
            hashmapt[c] = hashmapt.get(c,0) + 1
        
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        have = 0
        need = len(hashmapt)

        for r in range(len(s)):
            c = s[r]
            hashmapw[c] = hashmapw.get(c,0)+1

            if c in hashmapt and hashmapw[c] == hashmapt[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                hashmapw[s[l]] -= 1

                if s[l] in hashmapt and hashmapw[s[l]] < hashmapt[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""



