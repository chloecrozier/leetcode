# https://leetcode.com/problems/maximum-ice-cream-bars/description/?envType=problem-list-v2&envId=counting-sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        remainder = coins
        res = 0
        for i in range(len(costs)):
            if costs[i] <= remainder:
                remainder -= costs[i]
                res += 1
            else:
                return res
        return res
