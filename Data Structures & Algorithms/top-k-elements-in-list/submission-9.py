class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        
        for key, value in hashmap.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res
        
        



        





        
            

        