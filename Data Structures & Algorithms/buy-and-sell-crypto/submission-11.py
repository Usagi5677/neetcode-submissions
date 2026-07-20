class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0

        for r in range(1,len(prices)):
            total = prices[r] - prices[l]
            profit = max(profit, total)
            if total < 0:
                l = r
            r += 1
        return profit