class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        signatureone = [0] * 26
        signaturetwo = [0] * 26
        for i in range(len(s1)):
            signatureone[ord(s1[i]) - ord("a")] += 1
            signaturetwo[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if signatureone[i] == signaturetwo[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            signaturetwo[index] += 1

            if signatureone[index] == signaturetwo[index]:
                matches += 1
            elif signatureone[index] + 1 == signaturetwo[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            signaturetwo[index] -= 1

            if signatureone[index] == signaturetwo[index]:
                matches += 1
            elif signatureone[index] - 1 == signaturetwo[index]:
                matches -= 1
            
            l += 1
        return matches == 26
