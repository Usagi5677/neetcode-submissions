class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        r = 1
        while r < len(prices):
            total = prices[r] - prices[l]
            profit = max(profit, total)
            if total < 0:
                l = r
            r += 1
        return profit