# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = 1
        if nums[0] > nums[-1]:
            while nums[k] > nums[k - 1]:
                k += 1
        else:
            k = 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[(mid + k) % len(nums)]:
                left = mid + 1
            elif target < nums[(mid + k) % len(nums)]:
                right = mid - 1
            else:
                return (mid + k) % len(nums)
        return -1
