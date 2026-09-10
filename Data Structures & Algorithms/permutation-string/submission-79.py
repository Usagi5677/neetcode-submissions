class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        s1count = [0] * 26
        s2count = [0] * 26
        
        for c1, c2 in zip(s1, s2):
            s1count[ord(c1) - 97] += 1
            s2count[ord(c2) - 97] += 1
            
        if s1count == s2count:
            return True

        for r in range(n1, n2):
            s2count[ord(s2[r]) - 97] += 1
            s2count[ord(s2[r - n1]) - 97] -= 1
            
            if s1count == s2count:
                return True
                
        return False