class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in hm:
                return [hm.get(t), i]
            hm[n] = i