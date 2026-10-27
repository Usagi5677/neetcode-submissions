class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = res = 0
        for r in range(len(prices)):
            t = prices[r] - prices[l]
            res = max(res, t)
            if t < 0:
                l = r
        return res