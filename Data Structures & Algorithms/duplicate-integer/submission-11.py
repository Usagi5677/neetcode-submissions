class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = n
        return False
