class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        for n in hs:
            if (n - 1) not in hs:
                longest = 0
                while (n + longest) in hs:
                    longest += 1
                    res = max(res, longest)
        return res