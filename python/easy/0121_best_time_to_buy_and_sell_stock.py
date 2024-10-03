# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0
        for price in prices:
            minVal = min(minVal, price)
            maxProfit = max(maxProfit, price - minVal)
        return maxProfit
