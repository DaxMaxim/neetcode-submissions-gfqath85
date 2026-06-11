class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        l = res = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[l] >= prices[r]: l = r
        return res