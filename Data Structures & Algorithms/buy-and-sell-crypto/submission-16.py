class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(prices)):
            total = prices[r] - prices[l]
            res = max(res, total)
            if total < 0:
                l = r
            r += 1
        return res