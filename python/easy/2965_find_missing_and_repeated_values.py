# https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        maxVal = len(grid)
        expectedSum = 0
        actualSum = 0
        missingVal = 0
        for i in range(1, pow(maxVal, 2) + 1):
            expectedSum += i

        numSet = set()
        for group in grid:
            for val in group:
                if val in numSet:
                    missingVal = val
                else:
                    numSet.add(val)
                    actualSum += val

        return [missingVal, expectedSum - actualSum]
