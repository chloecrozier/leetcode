# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=daily-question&envId=2025-03-12
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negCount = 0
        posCount = 0
        for n in nums:
            if n < 0:
                negCount += 1
            elif n > 0:
                posCount += 1
        return max(negCount, posCount)
