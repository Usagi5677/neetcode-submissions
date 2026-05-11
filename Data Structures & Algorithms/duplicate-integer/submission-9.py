class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            else:
                hashmap[n] = hashmap.get(n,0)+1
        return False
