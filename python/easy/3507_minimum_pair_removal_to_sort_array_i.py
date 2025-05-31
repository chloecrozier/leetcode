# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=problem-list-v2&envId=doubly-linked-list
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(ls):
            for i in range(len(ls) - 1):
                if ls[i] > ls[i + 1]:
                    return False
            return True

        count = 0
        while not isSorted(nums):
            minIndex = 0
            minSum = (1000 * 50) + 1
            for i in range(len(nums) - 1):
                if (nums[i] + nums[i + 1]) < minSum:
                    minIndex = i
                    minSum = nums[i] + nums[i + 1]
            nums = nums[0:minIndex] + [minSum] + nums[minIndex + 2:] 
            count += 1
        return count
