# https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2025-03-31
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        diff = [0] * (len(weights) - 1)
        for i in range(len(weights) - 1):
            diff[i] = weights[i] + weights[i + 1]
        diff.sort()

        res = 0
        for i in range(k - 1):
            res += diff[len(diff) - 1 - i] - diff[i]

        return res
