class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            p = prices[r] - prices[l]
            res = max(res, p)
            if p < 0:
                l = r
        return res