class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        for key, value in hashmap.items():
            freq[value].append(key)
        
        res = []
        for n in range(len(freq) - 1, 0, -1):
            for i in freq[n]:
                res.append(i)
                if len(res) == k:
                    return res
            

        