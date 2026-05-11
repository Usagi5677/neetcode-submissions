class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in range(len(nums)):
            if hm.get(nums[i], 0):
                return True
            else:
                hm[nums[i]] = hm.get(nums[i], 0) + 1
        return False
