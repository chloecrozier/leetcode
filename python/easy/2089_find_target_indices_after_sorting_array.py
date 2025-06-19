# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []

        left = 0
        right = len(nums) - 1
        mid = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res.append(mid)
                break

        curr = mid - 1
        while curr >= 0 and nums[curr] == target:
            res = [curr] + res
            curr -= 1

        curr = mid + 1
        while curr < len(nums) and nums[curr] == target:
            res.append(curr)
            curr += 1

        return res

        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        # return res
