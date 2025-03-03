# https://leetcode.com/problems/set-mismatch/description/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupe = 0
        sumVals = 0
        actualSum = 0
        numSet = set()
        for i in range(len(nums)):
            if nums[i] not in numSet:
                numSet.add(nums[i])
            else:
                dupe = nums[i]
            sumVals += nums[i]
            actualSum += i + 1

        return [dupe, actualSum - sumVals + dupe]
