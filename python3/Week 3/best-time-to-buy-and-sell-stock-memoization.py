class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        i = len(prices)
        lowest = prices[0]
        value = 0
        for p in prices[1:]:
            lowest = min(p, lowest)
            value = max(value, p-lowest)
        return value