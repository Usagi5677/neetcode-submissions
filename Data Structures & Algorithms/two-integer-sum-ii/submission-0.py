class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(numbers, start = 1):
            temp = target - n
            if temp in hm:
                return [hm.get(temp), i]
            hm[n] = i
        