# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=daily-question&envId=2025-01-17
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
