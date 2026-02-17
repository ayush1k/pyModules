#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]            
            elif prices[i] - low > max_profit:
                    max_profit = prices[i] - low
        return max_profit