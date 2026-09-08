class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in hm:
                return [hm.get(val), i]
            hm[n] = i
        