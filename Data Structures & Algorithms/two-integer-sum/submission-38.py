class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in hm:
                return [hm.get(temp), i]
            hm[n] = i
        
        

        
        
        
        
        
        