class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for c in s:
                signature[ord(c) - ord("a")] += 1
            res[tuple(signature)].append(s)
        
        return list(res.values())