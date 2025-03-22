# https://leetcode.com/problems/transform-array-by-parity/submissions/1578613302/
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        oddCount = 0
        evenCount = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                oddCount += 1
            else:
                evenCount += 1
        
        for i in range(len(nums)):
            if i < evenCount:
                nums[i] = 0
            else:
                nums[i] = 1
        return nums
