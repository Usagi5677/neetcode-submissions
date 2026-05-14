class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        res = []

        for key, val in hm.items():
            print(key, val)
            freq[val].append(key)
        print(freq)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
