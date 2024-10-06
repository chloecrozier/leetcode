# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [nums[0]]
        postProd = [nums[-1]]
        for i in range(1, len(nums)):
            preProd.append(preProd[i - 1] * nums[i])
            postProd.append(postProd[i - 1] * nums[len(nums) - i - 1])
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postProd[-2]
            elif i == len(nums) - 1:
                nums[i] = preProd[-2]
            else:
                nums[i] = preProd[i - 1] * postProd[len(nums) - i - 2]
        return nums
