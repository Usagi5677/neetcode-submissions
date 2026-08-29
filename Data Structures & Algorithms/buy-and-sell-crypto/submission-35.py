class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(len(prices)):
            total = prices[r] - prices[l]
            res = max(res, total)
            if total < 0:
                l = r
        return res