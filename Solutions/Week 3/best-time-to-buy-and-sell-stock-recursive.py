class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, 0, 0)
        
    def helper(self, prices, index, lowest, value):
        if index>= len(prices):
            return value
        lowest = min(lowest, prices[index]) if index>0 else prices[0]
        value = max(prices[index]-lowest, value) if index>0 else 0
        return self.helper(prices, index+1, lowest, value)