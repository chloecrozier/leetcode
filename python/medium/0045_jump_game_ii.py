# https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] >= (len(nums) - 1):
            return 1
        else:
            curr = 0
            jumps = 0
            while curr < len(nums) - 1:
                jumpLen = 1
                for i in range(2, nums[curr] + 1):
                    if i + curr >= len(nums) - 1:
                        return jumps + 1
                    else:
                        if (i + nums[curr + i]) >= (jumpLen + nums[curr + jumpLen]):
                            jumpLen = i
                curr += jumpLen
                jumps += 1

            return jumps
