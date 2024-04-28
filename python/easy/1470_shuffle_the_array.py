# https://leetcode.com/problems/shuffle-the-array/description/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = [None] * 2*n
        index = 0
        for i in range (0, 2*n, 2):
            newNums[i] = (nums[index])
            index += 1
        index = 0
        for i in range (1, 2*n, 2):
            newNums[i] = nums[n + index]
            index += 1
        nums = newNums
        return nums
