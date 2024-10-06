# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i = l // 2
        
        k = 1
        if nums[0] > nums[-1]:
            while nums[k] > nums[k - 1]:
                k += 1
        else:
            k = 0

        count = 0
        while count <= l:
            if target > nums[(i + k) % l]:
                i += 1
            elif target < nums[(i + k) % l]:
                i -= 1
            else:
                return (i + k) % l
            count += 1
        return -1
